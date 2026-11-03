| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.80 | 0.70 | [0.52, 0.89] | 0.89 | 0.96 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.00 | 566 | [552, 580] | 0.00027 | 1 |
| fib_min3_fallback_confirm | 0.93 | [0.81, 1.00] | 0.75 | 0.74 | [0.59, 0.89] | 0.89 | 0.66 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.09 | 773 | [737, 810] | 0.00034 | 4.53 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 1.00 |
| fib_min3_fallback_confirm | 0.93 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.80 |
| fib_min3_fallback_confirm | 0.75 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.70 |
| fib_min3_fallback_confirm | 0.74 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | -0.07 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.04 | [0.00, 0.11] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 207 | [176, 241] | yes |