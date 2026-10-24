| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.83 | 0.74 | [0.56, 0.89] | 0.89 | 0.96 | n/a | [n/a, n/a] | 0.80 | 0.00 | 0.00 | 1.00 | 785 | [773, 798] | 0.00219 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 0.89 | 0.89 | n/a | [n/a, n/a] | 0.81 | 0.00 | 0.00 | 1.08 | 963 | [944, 982] | 0.00267 | 4.33 |

recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 1.00 |
| fib_min3_fallback_confirm | 1.00 |

fragment recall by attack family
| strategy | agentdojo_span |
|---|---|
| per_message | 0.83 |
| fib_min3_fallback_confirm | 0.94 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo_span |
|---|---|
| per_message | 0.74 |
| fib_min3_fallback_confirm | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.26 | [0.11, 0.44] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 178 | [164, 193] | yes |