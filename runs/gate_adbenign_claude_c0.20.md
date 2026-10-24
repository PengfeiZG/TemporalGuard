| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.02 | [0.01, 0.04] | n/a | 0.00 | n/a | 1.02 | 1907 | [1870, 1949] | 0.00030 | 3.00 |
| fib_min3_fallback_confirm_kwgated | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.00697 | [0.00167, 0.01] | n/a | 0.00 | n/a | 0.04 | 77.77 | [35.65, 128] | 0.00001 | 0.14 |
| fib_min3_fallback_confirm_semgated | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.02 | [0.01, 0.04] | n/a | 0.00 | n/a | 0.57 | 1076 | [934, 1213] | 0.00017 | 1.72 |

recall by attack family
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_kwgated |
| fib_min3_fallback_confirm_semgated |

fragment recall by attack family
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_kwgated |
| fib_min3_fallback_confirm_semgated |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_kwgated |
| fib_min3_fallback_confirm_semgated |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | agentdojo_benign |
|---|---|
| fib_min3_fallback_confirm | 0.28 |
| fib_min3_fallback_confirm_kwgated | 0.10 |
| fib_min3_fallback_confirm_semgated | 0.28 |