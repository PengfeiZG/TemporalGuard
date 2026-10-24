| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.85 | [0.70, 0.96] | 0.54 | 0.48 | [0.30, 0.67] | 0.78 | 0.96 | n/a | [n/a, n/a] | 0.63 | 0.00 | 0.00 | 1.06 | 1857 | [1825, 1890] | 0.00066 | 1 |
| fib_min3_fallback_confirm | 0.93 | [0.81, 1.00] | 0.84 | 0.85 | [0.70, 0.96] | 0.85 | 0.95 | n/a | [n/a, n/a] | 0.83 | 0.00 | 0.00 | 1.34 | 2655 | [2555, 2760] | 0.00183 | 4.74 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.85 |
| fib_min3_fallback_confirm | 0.93 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.54 |
| fib_min3_fallback_confirm | 0.84 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.48 |
| fib_min3_fallback_confirm | 0.85 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.07 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.37 | [0.19, 0.56] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 798 | [706, 898] | yes |