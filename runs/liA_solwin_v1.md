| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.67 | [0.50, 0.81] | 0.46 | 0.31 | [0.17, 0.44] | 0.36 | 0.80 | n/a | [n/a, n/a] | 0.68 | 0.00 | 0.00 | 1.00 | 789 | [775, 804] | 0.00221 | 1 |
| fib_min3_fallback_confirm | 0.75 | [0.58, 0.89] | 0.64 | 0.53 | [0.36, 0.69] | 0.36 | 0.82 | n/a | [n/a, n/a] | 0.83 | 0.00 | 0.00 | 1.09 | 963 | [920, 1010] | 0.00269 | 3.65 |
| full | 0.86 | [0.75, 0.97] | 0.77 | 0.58 | [0.42, 0.75] | 0.44 | 0.84 | n/a | [n/a, n/a] | 0.86 | 0.00 | 0.00 | 1.00 | 1136 | [1065, 1193] | 0.00295 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.50 | 0.58 | 0.92 |
| fib_min3_fallback_confirm | 0.92 | 0.50 | 0.83 |
| full | 0.92 | 0.83 | 0.83 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.22 | 0.25 | 0.92 |
| fib_min3_fallback_confirm | 0.83 | 0.25 | 0.83 |
| full | 0.81 | 0.67 | 0.83 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.92 |
| fib_min3_fallback_confirm | 0.67 | 0.08 | 0.83 |
| full | 0.58 | 0.33 | 0.83 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.19 | [0.00, 0.39] | no (CI contains 0) |
| full vs per_message | root_recall | 0.28 | [0.08, 0.44] | yes |
| full vs per_message | tokens_per_output | 348 | [281, 404] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.08 | [-0.08, 0.25] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.22 | [0.06, 0.39] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 174 | [139, 220] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.11 | [-0.25, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.06 | [-0.17, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -174 | [-245, -79.68] | yes |