| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.72, 0.97] | 0.60 | 0.33 | [0.17, 0.47] | 0.47 | 0.80 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.00 | 1658 | [1639, 1679] | 0.00538 | 1 |
| full | 1.00 | [1.00, 1.00] | 0.94 | 0.81 | [0.67, 0.92] | 0.58 | 0.85 | n/a | [n/a, n/a] | 0.89 | 0.00200 | 0.00 | 1.01 | 2262 | [2144, 2356] | 0.00694 | 10.74 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.91 | 0.81 | [0.67, 0.92] | 0.58 | 0.82 | n/a | [n/a, n/a] | 0.86 | 0.00 | 0.00 | 1.32 | 2515 | [2387, 2638] | 0.00818 | 5.69 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.83 | 0.75 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.42 | 0.39 | 1.00 |
| full | 0.97 | 0.83 | 1.00 |
| fib_min3_fallback_confirm | 0.97 | 0.75 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| full | 0.92 | 0.50 | 1 |
| fib_min3_fallback_confirm | 0.92 | 0.50 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| full vs per_message | root_recall | 0.47 | [0.33, 0.64] | yes |
| full vs per_message | tokens_per_output | 603 | [486, 694] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.47 | [0.33, 0.64] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 857 | [733, 982] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 254 | [115, 421] | yes |