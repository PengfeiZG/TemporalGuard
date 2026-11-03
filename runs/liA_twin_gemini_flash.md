| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.19 | [0.08, 0.33] | 0.16 | 0.14 | [0.03, 0.25] | 0.00 | 0.28 | 0.02 | [0.00205, 0.04] | 0.81 | 0.00 | 0.00 | 1.00 | 564 | [554, 575] | 1 |
| fib_min3_fallback_confirm | 0.31 | [0.17, 0.44] | 0.27 | 0.22 | [0.08, 0.36] | 0.06 | 0.36 | 0.02 | [0.00466, 0.04] | 0.87 | 0.00 | 0.00 | 1.03 | 680 | [659, 700] | 3.13 |
| full | 0.42 | [0.25, 0.58] | 0.33 | 0.17 | [0.06, 0.31] | 0.06 | 0.46 | 0.02 | [0.00205, 0.04] | 0.72 | 0.00 | 0.00 | 1.00 | 980 | [924, 1028] | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.17 | 0.00 | 0.42 |
| fib_min3_fallback_confirm | 0.25 | 0.08 | 0.58 |
| full | 0.33 | 0.50 | 0.42 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.06 | 0.00 | 0.42 |
| fib_min3_fallback_confirm | 0.19 | 0.03 | 0.58 |
| full | 0.25 | 0.33 | 0.42 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.42 |
| fib_min3_fallback_confirm | 0.08 | 0 | 0.58 |
| full | 0.08 | 0 | 0.42 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.08 | 0.25 | 0.00 |
| fib_min3_fallback_confirm | 0.08 | 0.42 | 0.00 |
| full | 0.08 | 0.25 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.17 | 0.00 | 0.42 | 0.19 |
| fib_min3_fallback_confirm | 0.25 | 0.00 | 0.58 | 0.28 |
| full | 0.33 | 0.33 | 0.42 | 0.36 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.22 | [0.06, 0.42] | yes |
| full vs per_message | root_recall | 0.03 | [-0.08, 0.14] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 416 | [360, 462] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.11 | [-0.03, 0.25] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.08 | [-0.03, 0.19] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 116 | [97.86, 134] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.11 | [-0.28, 0.03] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.06 | [-0.06, 0.17] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -300 | [-348, -246] | yes |