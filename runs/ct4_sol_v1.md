| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.56 | [0.39, 0.72] | 0.42 | 0.47 | [0.31, 0.61] | 0.25 | 0.66 | 0.02 | [0.00766, 0.03] | 0.74 | 0.00 | 0.00 | 1.00 | 782 | [779, 785] | 0.00219 | 1 |
| fib_min3_fallback_confirm | 0.69 | [0.53, 0.83] | 0.60 | 0.69 | [0.53, 0.83] | 0.42 | 0.74 | 0.02 | [0.01, 0.04] | 0.86 | 0.00 | 0.00 | 1.04 | 907 | [890, 926] | 0.00253 | 3.06 |
| full | 0.89 | [0.78, 0.97] | 0.77 | 0.89 | [0.78, 0.97] | 0.61 | 0.82 | 0.02 | [0.00941, 0.04] | 0.86 | 0.00 | 0.00 | 1.00 | 1202 | [1133, 1261] | 0.00308 | 10.72 |

recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.50 | 0.25 | 0.92 |
| fib_min3_fallback_confirm | 0.83 | 0.42 | 0.83 |
| full | 0.92 | 0.92 | 0.83 |

fragment recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.22 | 0.11 | 0.92 |
| fib_min3_fallback_confirm | 0.69 | 0.28 | 0.83 |
| full | 0.75 | 0.72 | 0.83 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.33 | 0.17 | 0.92 |
| fib_min3_fallback_confirm | 0.83 | 0.42 | 0.83 |
| full | 0.92 | 0.92 | 0.83 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct4_twin | ct4_span_twin | ct4_concat_twin |
|---|---|---|---|
| per_message | 0.33 | 0.33 | 0.00 |
| fib_min3_fallback_confirm | 0.58 | 0.42 | 0.00 |
| full | 0.42 | 0.33 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct4 | ct4_span | ct4_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.17 | 0.00 | 0.92 | 0.36 |
| fib_min3_fallback_confirm | 0.25 | 0.08 | 0.83 | 0.39 |
| full | 0.50 | 0.58 | 0.83 | 0.64 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.33 | [0.17, 0.53] | yes |
| full vs per_message | root_recall | 0.42 | [0.25, 0.61] | yes |
| full vs per_message | tokens_per_output | 420 | [353, 478] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.00, 0.31] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.22 | [0.06, 0.39] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 125 | [110, 143] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.19 | [-0.33, -0.06] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.19 | [-0.33, -0.06] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -294 | [-356, -219] | yes |