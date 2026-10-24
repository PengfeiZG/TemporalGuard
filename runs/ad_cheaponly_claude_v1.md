| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.85 | [0.70, 0.96] | 0.56 | 0.48 | [0.30, 0.67] | 0.78 | 0.94 | n/a | [n/a, n/a] | 0.64 | 0.00 | 0.00 | 1.00 | 1746 | [1729, 1764] | 1 |
| fib_min3_fallback_confirm | 0.93 | [0.81, 1.00] | 0.79 | 0.74 | [0.56, 0.89] | 0.89 | 0.84 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.18 | 2321 | [2235, 2410] | 5.29 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.85 |
| fib_min3_fallback_confirm | 0.93 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.56 |
| fib_min3_fallback_confirm | 0.79 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.48 |
| fib_min3_fallback_confirm | 0.74 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.07 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.26 | [0.11, 0.44] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 575 | [491, 661] | yes |