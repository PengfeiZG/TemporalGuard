| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.78 | [0.64, 0.89] | 0.50 | 0.33 | [0.17, 0.47] | 0.39 | 0.76 | n/a | [n/a, n/a] | 0.62 | 0.00 | 0.00 | 1.00 | 791 | [777, 807] | 0.00011 | 1 |
| fib_min3_fallback_confirm | 0.92 | [0.81, 1.00] | 0.78 | 0.61 | [0.44, 0.78] | 0.50 | 0.66 | n/a | [n/a, n/a] | 0.73 | 0.00 | 0.00 | 1.16 | 1046 | [998, 1105] | 0.00015 | 4.35 |
| full | 1.00 | [1.00, 1.00] | 0.86 | 0.61 | [0.44, 0.78] | 0.53 | 0.74 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.00 | 1139 | [1066, 1195] | 0.00015 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.75 | 0.67 | 0.92 |
| fib_min3_fallback_confirm | 1.00 | 0.75 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.31 | 0.28 | 0.92 |
| fib_min3_fallback_confirm | 0.92 | 0.42 | 1.00 |
| full | 0.89 | 0.69 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.08 | 0 | 0.92 |
| fib_min3_fallback_confirm | 0.75 | 0.08 | 1 |
| full | 0.67 | 0.17 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.22 | [0.11, 0.36] | yes |
| full vs per_message | root_recall | 0.28 | [0.14, 0.42] | yes |
| full vs per_message | tokens_per_output | 348 | [282, 404] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.28 | [0.14, 0.42] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 255 | [210, 312] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.08 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [-0.08, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -92.99 | [-164, 6.12] | no (CI contains 0) |