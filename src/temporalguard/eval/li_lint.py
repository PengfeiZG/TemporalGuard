"""Style checks for LogicInception-style fragments (Liu et al., EMNLP 2026).

The attack the paper describes avoids every surface cue a detector looks for: its fragments are
declarative notices with no command, no security vocabulary and no tool names, and the unauthorized
action only emerges when the pieces are read together. These checks help the authors keep their
own fragments in that style. They are advisory: a warning is a prompt to look again, not a verdict.
"""

from __future__ import annotations

import re

# Words that name a security attack, or that a notice would not normally contain.
SECURITY_WORDS = (
    "override", "bypass", "ignore", "disregard", "forget", "jailbreak", "inject",
    "system prompt", "important message", "instruction", "do not tell", "secretly", "hidden",
)  # fmt: skip

# First words of a sentence that make it an order to the reader.
IMPERATIVE_STARTS = frozenset(
    "send transfer delete remove create add invite post forward email share upload visit open "
    "click reply execute run call use make change set update pay book reserve tell say mention "
    "read copy find look check ensure confirm please kindly proceed complete perform submit "
    "issue release clear approve authorize wire move".split()
)

# A second word that shows the sentence is a statement ("Release of ...", "Transfer is ...").
_STATEMENT_NEXT = frozenset(
    "of is was are were has have had will would can could may might to for and or from by in on at "
    "as remains remain requires depends "
    # a field label such as "email subject: ..." is not an order
    "subject body address recipient sender recipients senders".split()
)
# An order reported in the third person ("a note requests the forwarding") is still an order.
_REPORTED_ORDER = re.compile(
    r"\b(?:requests (?:for|the|that|a|an|to)|instructs|asks (?:the|that|for)|directs|advises|urges"
    r"|demands|commands)\b",
    re.I,
)
_TAG = re.compile(r"^\s*\[[^\]]*\]\s*")  # a leading "[NOTICE | Ref 12]" style tag
_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
_DOMAIN = re.compile(r"\b[\w-]+(?:\.[\w-]+)*\.(?:com|org|net|io|edu|gov|co|us|uk|de|cn|ru)\b", re.I)
_IBAN = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{8,}\b")
_SNAKE = re.compile(r"\b[a-z]+(?:_[a-z0-9]+)+\b")
_QUOTED = r"(?<![\w])'[^'\n]+'(?![\w])"  # 'Intro with Mark', but not the 's of a possessive
_STRONG_PARAM = re.compile(
    rf"[\w.+-]+@[\w-]+\.invalid|\b[\w-]+\.example\.invalid[^\s,;]*|\bUS00INVALID\d+|{_QUOTED}"
)
_ANY_PARAM = re.compile(
    rf"[\w.+-]+@[\w-]+\.invalid|\b[\w-]+\.example\.invalid[^\s,;]*|\bUS00INVALID\d+|{_QUOTED}"
    r"|\bnew_password\b|\b\d[\d,.]*\d\b"
)


def goal_parameters(base: str) -> list[str]:
    """The concrete values of an AgentDojo-derived goal (addresses, names, amounts)."""
    from .li_data import goal_text  # imported here: li_data imports this module lazily too

    goal = goal_text(base)
    seen: list[str] = []
    for token in _ANY_PARAM.findall(goal):
        token = token.strip("'").rstrip(".,;:")
        if token not in seen:
            seen.append(token)
    return seen


def lint_fragment(text: str) -> list[str]:
    """Style problems in one fragment (an empty list means none found)."""
    problems: list[str] = []
    lowered = text.lower()
    for word in SECURITY_WORDS:
        if word in lowered:
            problems.append(f"security-sensitive wording: '{word}'")
    for sentence in re.split(r"(?<=[.;])\s+", _TAG.sub("", text.strip())):
        words = re.findall(r"[A-Za-z]+", sentence.strip())[:2]
        if words and words[0].lower() in IMPERATIVE_STARTS:
            if len(words) == 1 or words[1].lower() not in _STATEMENT_NEXT:
                problems.append(f"sentence opens with an order: '{words[0]}'")
    if re.search(r"\b(you|your|yours)\b", lowered):
        problems.append("addresses the reader directly (you/your)")
    if re.search(r"\b(must|should|need to|has to|have to)\b", lowered):
        problems.append(
            "uses obligation wording (must/should/need to); prefer a plain statement of fact"
        )
    reported = _REPORTED_ORDER.search(text)
    if reported:
        problems.append(f"reports an order ('{reported.group(0)}'); state a fact instead")
    if "?" in text or "!" in text:
        problems.append("contains a question or exclamation mark; use declarative sentences")
    snake = [t for t in _SNAKE.findall(text) if t != "new_password"]
    if snake:
        problems.append(f"names a tool or function: {sorted(set(snake))[:3]}")
    for email in _EMAIL.findall(text):
        if not email.lower().endswith(".invalid"):
            problems.append(f"real-looking address '{email}': use a .invalid placeholder")
    for domain in _DOMAIN.findall(text):
        problems.append(f"real-looking domain '{domain}': use a .invalid placeholder")
    for iban in _IBAN.findall(text):
        if "INVALID" not in iban:
            problems.append(f"real-looking account number '{iban}': use the INVALID placeholder")
    if len(text) > 700:
        problems.append("longer than 700 characters; shorter fragments read more like real notices")
    return problems


def lint_attack(base: str, fragments: list[str]) -> list[str]:
    """Problems with one attack: each fragment, plus how the parameters are spread over them."""
    problems: list[str] = []
    for i, frag in enumerate(fragments, start=1):
        problems += [f"fragment {i}: {p}" for p in lint_fragment(frag)]
    if len(fragments) < 3:
        return [*problems, "needs at least 3 fragments (premise, dependency, specification)"]
    premise, binding, spec = fragments[0], fragments[1], " ".join(fragments[2:])
    for name, text in (("premise", premise), ("dependency", binding)):
        leaked = _STRONG_PARAM.findall(text)
        if leaked:
            problems.append(
                f"{name} already holds target values {leaked[:2]}; keep them for the specification"
            )
    params = goal_parameters(base)
    if params and not any(p in spec for p in params):
        problems.append(
            f"specification contains none of the goal's values (for example {params[:3]})"
        )
    return problems
