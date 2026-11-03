| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.69 | [0.53, 0.83] | 0.46 | 0.31 | [0.17, 0.44] | 0.28 | 0.60 | 0.02 | [0.00601, 0.04] | 0.65 | 0.00 | 0.00 | 1.00 | 737 | [722, 752] | 1 |
| fib_min3_fallback_confirm | 0.89 | [0.78, 0.97] | 0.74 | 0.58 | [0.42, 0.72] | 0.36 | 0.69 | 0.02 | [0.00402, 0.04] | 0.82 | 0.00 | 0.00 | 1.06 | 976 | [938, 1019] | 3.42 |
| full | 0.92 | [0.83, 1.00] | 0.82 | 0.64 | [0.47, 0.78] | 0.33 | 0.69 | 0.02 | [0.00594, 0.05] | 0.86 | 0.00 | 0.00 | 1.00 | 1227 | [1166, 1273] | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.58 | 0.58 | 0.92 |
| fib_min3_fallback_confirm | 0.92 | 0.75 | 1.00 |
| full | 0.92 | 0.92 | 0.92 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.25 | 0.22 | 0.92 |
| fib_min3_fallback_confirm | 0.81 | 0.42 | 1.00 |
| full | 0.78 | 0.78 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.92 |
| fib_min3_fallback_confirm | 0.58 | 0.17 | 1 |
| full | 0.50 | 0.50 | 0.92 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.08 | 0.33 | 0.08 |
| fib_min3_fallback_confirm | 0.17 | 0.17 | 0.08 |
| full | 0.17 | 0.25 | 0.08 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.50 | 0.33 | 0.83 | 0.56 |
| fib_min3_fallback_confirm | 0.75 | 0.58 | 0.92 | 0.75 |
| full | 0.75 | 0.67 | 0.83 | 0.75 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.22 | [0.08, 0.36] | yes |
| full vs per_message | root_recall | 0.33 | [0.19, 0.50] | yes |
| full vs per_message | tokens_per_output | 490 | [430, 538] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.19 | [0.06, 0.36] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.28 | [0.14, 0.42] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 239 | [209, 273] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.03 | [-0.14, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.06 | [-0.22, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -251 | [-308, -184] | yes |