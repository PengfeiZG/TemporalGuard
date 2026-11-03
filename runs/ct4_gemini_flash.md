| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.42 | [0.25, 0.58] | 0.28 | 0.33 | [0.17, 0.50] | 0.25 | 0.60 | 0.02 | [0.00785, 0.03] | 0.65 | 0.00 | 0.00 | 1.00 | 561 | [557, 564] | 1 |
| fib_min3_fallback_confirm | 0.36 | [0.19, 0.53] | 0.29 | 0.36 | [0.19, 0.53] | 0.19 | 0.67 | 0.01 | [0.00421, 0.02] | 0.79 | 0.00 | 0.00 | 1.02 | 671 | [660, 683] | 2.89 |
| full | 0.50 | [0.33, 0.67] | 0.38 | 0.47 | [0.31, 0.64] | 0.33 | 0.72 | 0.01 | [0.00584, 0.02] | 0.75 | 0.00 | 0.00 | 1.00 | 1067 | [985, 1136] | 10.72 |

recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.42 | 0.33 | 0.50 |
| fib_min3_fallback_confirm | 0.42 | 0.17 | 0.50 |
| full | 0.42 | 0.58 | 0.50 |

fragment recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.17 | 0.17 | 0.50 |
| fib_min3_fallback_confirm | 0.28 | 0.08 | 0.50 |
| full | 0.28 | 0.36 | 0.50 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.25 | 0.25 | 0.50 |
| fib_min3_fallback_confirm | 0.42 | 0.17 | 0.50 |
| full | 0.42 | 0.50 | 0.50 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct4_twin | ct4_span_twin | ct4_concat_twin |
|---|---|---|---|
| per_message | 0.25 | 0.42 | 0.00 |
| fib_min3_fallback_confirm | 0.17 | 0.33 | 0.00 |
| full | 0.25 | 0.33 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct4 | ct4_span | ct4_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.17 | 0.00 | 0.50 | 0.22 |
| fib_min3_fallback_confirm | 0.25 | 0.00 | 0.50 | 0.25 |
| full | 0.17 | 0.33 | 0.50 | 0.33 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.08 | [-0.08, 0.25] | no (CI contains 0) |
| full vs per_message | root_recall | 0.14 | [-0.03, 0.33] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 507 | [425, 575] | yes |
| fib_min3_fallback_confirm vs per_message | recall | -0.06 | [-0.19, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.03 | [-0.11, 0.17] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 111 | [102, 121] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.14 | [-0.28, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.11 | [-0.25, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -396 | [-462, -313] | yes |