| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.63 | 0.33 | [0.17, 0.47] | 0.53 | 0.81 | n/a | [n/a, n/a] | 0.61 | 0.00 | 0.00 | 1.00 | 793 | [778, 808] | 0.00011 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.92 | 0.89 | [0.78, 0.97] | 0.61 | 0.71 | n/a | [n/a, n/a] | 0.80 | 0.00 | 0.00 | 1.16 | 1059 | [1017, 1113] | 0.00015 | 4.55 |
| full | 1.00 | [1.00, 1.00] | 0.97 | 0.92 | [0.81, 1.00] | 0.67 | 0.78 | n/a | [n/a, n/a] | 0.88 | 0.00 | 0.00 | 1.00 | 1146 | [1075, 1203] | 0.00015 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 1.00 | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.42 | 0.47 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.75 | 1.00 |
| full | 1.00 | 0.92 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| fib_min3_fallback_confirm | 1 | 0.67 | 1 |
| full | 1 | 0.75 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.58 | [0.42, 0.75] | yes |
| full vs per_message | tokens_per_output | 354 | [286, 411] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.56 | [0.39, 0.72] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 267 | [225, 321] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -86.98 | [-157, 9.30] | no (CI contains 0) |