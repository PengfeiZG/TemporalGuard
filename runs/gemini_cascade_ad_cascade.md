| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.93 | [0.81, 1.00] | 0.74 | 0.67 | [0.52, 0.85] | 0.89 | 0.97 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.09 | 649 | [629, 667] | 0.00083 | 1 |
| fib_min3_fallback_confirm | 0.89 | [0.78, 1.00] | 0.75 | 0.85 | [0.70, 0.96] | 0.89 | 0.95 | n/a | [n/a, n/a] | 0.82 | 0.00 | 0.00 | 1.24 | 952 | [883, 1022] | 0.00171 | 3.91 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.93 |
| fib_min3_fallback_confirm | 0.89 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.74 |
| fib_min3_fallback_confirm | 0.75 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.67 |
| fib_min3_fallback_confirm | 0.85 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | -0.04 | [-0.11, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.19 | [0.04, 0.33] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 303 | [243, 363] | yes |