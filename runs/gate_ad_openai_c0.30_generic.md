| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.87 | 0.81 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.16 | 1042 | [1012, 1076] | 0.00015 | 4.69 |
| fib_min3_fallback_confirm_semgated | 0.81 | [0.70, 0.93] | 0.68 | 0.65 | [0.50, 0.78] | 0.63 | 0.92 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.36 | 0.24 | 243 | [187, 306] | 0.00003 | 1.52 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_semgated | 0.81 | 0.81 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.80 |
| fib_min3_fallback_confirm_semgated | 0.75 | 0.60 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1 | 0.70 |
| fib_min3_fallback_confirm_semgated | 0.78 | 0.52 |