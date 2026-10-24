| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.76 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.27 | 2500 | [2424, 2587] | 0.00039 | 5.76 |
| fib_min3_fallback_confirm_kwgated | 0.30 | [0.19, 0.43] | 0.24 | 0.26 | [0.15, 0.37] | 0.19 | 0.81 | n/a | [n/a, n/a] | 0.71 | 0.00 | 0.84 | 0.07 | 157 | [91.78, 229] | 0.00002 | 0.45 |
| fib_min3_fallback_confirm_semgated | 0.98 | [0.94, 1.00] | 0.91 | 0.91 | [0.81, 0.98] | 0.91 | 0.81 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.04 | 0.85 | 1723 | [1581, 1875] | 0.00027 | 4.37 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_kwgated | 0.30 | 0.30 |
| fib_min3_fallback_confirm_semgated | 1.00 | 0.96 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.85 |
| fib_min3_fallback_confirm_kwgated | 0.30 | 0.19 |
| fib_min3_fallback_confirm_semgated | 0.99 | 0.84 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1 | 0.85 |
| fib_min3_fallback_confirm_kwgated | 0.33 | 0.19 |
| fib_min3_fallback_confirm_semgated | 1 | 0.81 |