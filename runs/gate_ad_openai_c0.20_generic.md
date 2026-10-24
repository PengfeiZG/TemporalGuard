| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.87 | 0.81 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.16 | 1042 | [1012, 1076] | 0.00015 | 4.69 |
| fib_min3_fallback_confirm_semgated | 0.94 | [0.87, 1.00] | 0.83 | 0.78 | [0.67, 0.89] | 0.80 | 0.91 | n/a | [n/a, n/a] | 0.80 | 0.00 | 0.15 | 0.43 | 415 | [359, 476] | 0.00006 | 2.36 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_semgated | 0.96 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.80 |
| fib_min3_fallback_confirm_semgated | 0.94 | 0.72 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1 | 0.70 |
| fib_min3_fallback_confirm_semgated | 0.96 | 0.59 |