| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.96 | [0.89, 1.00] | 0.78 | 0.70 | [0.56, 0.89] | 0.89 | 0.93 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.00 | 788 | [775, 801] | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.80 | 0.67 | [0.52, 0.85] | 0.85 | 0.81 | n/a | [n/a, n/a] | 0.64 | 0.00 | 0.00 | 1.12 | 1015 | [989, 1042] | 4.76 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.96 |
| fib_min3_fallback_confirm | 1.00 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.78 |
| fib_min3_fallback_confirm | 0.80 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.70 |
| fib_min3_fallback_confirm | 0.67 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.04 | [0.00, 0.11] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | -0.04 | [-0.15, 0.07] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 227 | [206, 251] | yes |