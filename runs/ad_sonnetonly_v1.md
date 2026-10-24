| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.93 | [0.81, 1.00] | 0.72 | 0.70 | [0.56, 0.85] | 0.89 | 0.97 | n/a | [n/a, n/a] | 0.75 | 0.00 | 0.00 | 1.00 | 1652 | [1637, 1670] | 0.00536 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.94 | 0.96 | [0.89, 1.00] | 0.93 | 0.96 | n/a | [n/a, n/a] | 0.87 | 0.00 | 0.00 | 1.20 | 2245 | [2146, 2353] | 0.00729 | 5.31 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.93 |
| fib_min3_fallback_confirm | 1.00 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.72 |
| fib_min3_fallback_confirm | 0.94 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.70 |
| fib_min3_fallback_confirm | 0.96 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.07 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.26 | [0.11, 0.41] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 592 | [493, 703] | yes |