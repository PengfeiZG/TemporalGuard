| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.96 | [0.89, 1.00] | 0.80 | 0.81 | [0.67, 0.96] | 0.93 | 0.97 | n/a | [n/a, n/a] | 0.81 | 0.00 | 0.00 | 1.00 | 729 | [712, 748] | 1 |
| fib_min3_fallback_confirm | 0.93 | [0.81, 1.00] | 0.85 | 0.89 | [0.78, 1.00] | 0.89 | 0.95 | n/a | [n/a, n/a] | 0.89 | 0.00 | 0.00 | 1.07 | 1007 | [973, 1038] | 4.10 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.96 |
| fib_min3_fallback_confirm | 0.93 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.80 |
| fib_min3_fallback_confirm | 0.85 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.81 |
| fib_min3_fallback_confirm | 0.89 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | -0.04 | [-0.11, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.07 | [-0.07, 0.22] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 278 | [248, 309] | yes |