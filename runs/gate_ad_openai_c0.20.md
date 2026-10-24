| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.87 | 0.81 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.16 | 1042 | [1012, 1076] | 0.00015 | 4.69 |
| fib_min3_fallback_confirm_kwgated | 0.30 | [0.19, 0.41] | 0.20 | 0.22 | [0.11, 0.33] | 0.19 | 0.87 | n/a | [n/a, n/a] | 0.61 | 0.00 | 0.84 | 0.06 | 65.08 | [39.08, 92.59] | 0.00001 | 0.38 |
| fib_min3_fallback_confirm_semgated | 0.98 | [0.94, 1.00] | 0.89 | 0.85 | [0.76, 0.94] | 0.85 | 0.83 | n/a | [n/a, n/a] | 0.79 | 0.00 | 0.04 | 0.76 | 707 | [640, 779] | 0.00010 | 3.47 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_kwgated | 0.30 | 0.30 |
| fib_min3_fallback_confirm_semgated | 1.00 | 0.96 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.80 |
| fib_min3_fallback_confirm_kwgated | 0.23 | 0.16 |
| fib_min3_fallback_confirm_semgated | 0.99 | 0.79 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1 | 0.70 |
| fib_min3_fallback_confirm_kwgated | 0.26 | 0.19 |
| fib_min3_fallback_confirm_semgated | 1 | 0.70 |