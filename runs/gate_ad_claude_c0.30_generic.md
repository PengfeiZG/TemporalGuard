| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.76 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.27 | 2500 | [2424, 2587] | 0.00039 | 5.76 |
| fib_min3_fallback_confirm_semgated | 0.80 | [0.69, 0.91] | 0.70 | 0.70 | [0.57, 0.83] | 0.67 | 0.91 | n/a | [n/a, n/a] | 0.79 | 0.00 | 0.36 | 0.29 | 633 | [501, 778] | 0.00010 | 2.05 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_semgated | 0.81 | 0.78 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.85 |
| fib_min3_fallback_confirm_semgated | 0.77 | 0.64 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1 | 0.85 |
| fib_min3_fallback_confirm_semgated | 0.81 | 0.59 |