| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.83 | [0.69, 0.94] | 0.51 | 0.33 | [0.17, 0.47] | 0.50 | 0.53 | 0.04 | [0.02, 0.06] | 0.60 | 0.00 | 0.00 | 1.00 | 789 | [779, 799] | 0.00220 | 1 |
| fib_min3_fallback_confirm | 0.97 | [0.92, 1.00] | 0.85 | 0.89 | [0.78, 0.97] | 0.56 | 0.60 | 0.04 | [0.02, 0.07] | 0.85 | 0.00 | 0.00 | 1.08 | 952 | [929, 979] | 0.00265 | 3.56 |
| full | 0.97 | [0.92, 1.00] | 0.97 | 0.97 | [0.92, 1.00] | 0.56 | 0.58 | 0.06 | [0.04, 0.09] | 0.95 | 0.00 | 0.00 | 1.00 | 1142 | [1093, 1181] | 0.00296 | 10.78 |

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

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.42 | 0.33 | 0.42 |
| fib_min3_fallback_confirm | 0.42 | 0.50 | 0.33 |
| full | 0.58 | 0.58 | 0.42 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.33 | 0.42 | 0.58 | 0.44 |
| fib_min3_fallback_confirm | 0.58 | 0.42 | 0.67 | 0.56 |
| full | 0.42 | 0.42 | 0.58 | 0.47 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| full vs per_message | root_recall | 0.64 | [0.47, 0.81] | yes |
| full vs per_message | tokens_per_output | 353 | [306, 393] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.56 | [0.39, 0.72] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 163 | [141, 187] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [-0.08, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.08 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -190 | [-237, -133] | yes |