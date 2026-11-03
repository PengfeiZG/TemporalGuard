| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.36 | [0.22, 0.53] | 0.31 | 0.28 | [0.14, 0.42] | 0.00 | 0.57 | n/a | [n/a, n/a] | 0.85 | 0.00 | 0.00 | 1.00 | 1752 | [1732, 1775] | 0.00027 | 1 |
| fib_min3_fallback_confirm | 0.75 | [0.61, 0.89] | 0.70 | 0.61 | [0.44, 0.78] | 0.17 | 0.62 | n/a | [n/a, n/a] | 0.82 | 0.00 | 0.00 | 1.16 | 2241 | [2119, 2387] | 0.00035 | 4.22 |
| full | 0.97 | [0.92, 1.00] | 0.88 | 0.69 | [0.56, 0.83] | 0.19 | 0.66 | n/a | [n/a, n/a] | 0.80 | 0.00 | 0.00 | 1.00 | 2324 | [2212, 2414] | 0.00034 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.17 | 0.08 | 0.83 |
| fib_min3_fallback_confirm | 1.00 | 0.33 | 0.92 |
| full | 1.00 | 1.00 | 0.92 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.06 | 0.03 | 0.83 |
| fib_min3_fallback_confirm | 0.94 | 0.25 | 0.92 |
| full | 0.94 | 0.78 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.83 |
| fib_min3_fallback_confirm | 0.83 | 0.08 | 0.92 |
| full | 0.83 | 0.33 | 0.92 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.61 | [0.44, 0.78] | yes |
| full vs per_message | root_recall | 0.42 | [0.28, 0.58] | yes |
| full vs per_message | tokens_per_output | 572 | [463, 662] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.39 | [0.22, 0.58] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.33 | [0.19, 0.50] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 489 | [370, 632] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.22 | [-0.36, -0.08] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.08 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -82.88 | [-254, 138] | no (CI contains 0) |