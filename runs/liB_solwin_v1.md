| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.83 | [0.69, 0.94] | 0.51 | 0.33 | [0.17, 0.47] | 0.50 | 0.82 | n/a | [n/a, n/a] | 0.60 | 0.00 | 0.00 | 1.00 | 790 | [776, 805] | 0.00221 | 1 |
| fib_min3_fallback_confirm | 0.97 | [0.92, 1.00] | 0.85 | 0.89 | [0.78, 0.97] | 0.56 | 0.84 | n/a | [n/a, n/a] | 0.85 | 0.00 | 0.00 | 1.11 | 993 | [960, 1032] | 0.00278 | 3.88 |
| full | 0.97 | [0.92, 1.00] | 0.97 | 0.97 | [0.92, 1.00] | 0.56 | 0.85 | n/a | [n/a, n/a] | 0.95 | 0.00 | 0.00 | 1.00 | 1144 | [1073, 1200] | 0.00298 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.75 | 0.75 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.92 | 1.00 |
| full | 1.00 | 0.92 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.28 | 0.25 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.56 | 1.00 |
| full | 1.00 | 0.92 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| fib_min3_fallback_confirm | 1 | 0.67 | 1 |
| full | 1 | 0.92 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| full vs per_message | root_recall | 0.64 | [0.47, 0.81] | yes |
| full vs per_message | tokens_per_output | 355 | [288, 412] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.56 | [0.39, 0.72] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 203 | [173, 238] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [-0.08, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.08 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -152 | [-220, -59.67] | yes |