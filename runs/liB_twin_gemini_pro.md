| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.75, 0.97] | 0.55 | 0.33 | [0.17, 0.47] | 0.50 | 0.61 | 0.03 | [0.01, 0.04] | 0.61 | 0.00 | 0.00 | 1.00 | 738 | [724, 751] | 1 |
| fib_min3_fallback_confirm | 0.89 | [0.78, 0.97] | 0.82 | 0.89 | [0.78, 0.97] | 0.50 | 0.65 | 0.03 | [0.01, 0.05] | 0.90 | 0.00 | 0.00 | 1.06 | 995 | [954, 1041] | 3.48 |
| full | 0.92 | [0.83, 1.00] | 0.92 | 0.92 | [0.83, 1.00] | 0.50 | 0.71 | 0.03 | [0.00990, 0.05] | 0.97 | 0.00 | 0.00 | 1.00 | 1255 | [1192, 1304] | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.75 | 0.83 | 1.00 |
| fib_min3_fallback_confirm | 0.92 | 0.83 | 0.92 |
| full | 0.92 | 0.92 | 0.92 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.28 | 0.36 | 1.00 |
| fib_min3_fallback_confirm | 0.92 | 0.64 | 0.92 |
| full | 0.92 | 0.92 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| fib_min3_fallback_confirm | 0.92 | 0.83 | 0.92 |
| full | 0.92 | 0.92 | 0.92 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.17 | 0.50 | 0.08 |
| fib_min3_fallback_confirm | 0.17 | 0.42 | 0.17 |
| full | 0.17 | 0.25 | 0.17 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.58 | 0.33 | 0.92 | 0.61 |
| fib_min3_fallback_confirm | 0.75 | 0.42 | 0.75 | 0.64 |
| full | 0.75 | 0.67 | 0.75 | 0.72 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.06 | [-0.06, 0.17] | no (CI contains 0) |
| full vs per_message | root_recall | 0.58 | [0.42, 0.75] | yes |
| full vs per_message | tokens_per_output | 517 | [459, 567] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.03 | [-0.06, 0.14] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.56 | [0.36, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 257 | [225, 295] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -260 | [-319, -187] | yes |