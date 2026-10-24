| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.96 | [0.89, 1.00] | 0.74 | 0.63 | [0.44, 0.81] | 0.89 | 0.95 | n/a | [n/a, n/a] | 0.75 | 0.00 | 0.00 | 1.09 | 862 | [844, 880] | 0.00034 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.88 | 0.89 | [0.78, 1.00] | 0.85 | 0.91 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.28 | 1182 | [1146, 1219] | 0.00067 | 4.48 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.96 |
| fib_min3_fallback_confirm | 1.00 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.74 |
| fib_min3_fallback_confirm | 0.88 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.63 |
| fib_min3_fallback_confirm | 0.89 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.04 | [0.00, 0.11] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.26 | [0.04, 0.48] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 320 | [292, 350] | yes |