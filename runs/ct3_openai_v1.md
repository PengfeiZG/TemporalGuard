| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.75, 0.97] | 0.51 | 0.86 | [0.75, 0.97] | 0.53 | 0.54 | 0.03 | [0.01, 0.04] | 0.57 | 0.00 | 0.00 | 1.00 | 782 | [779, 785] | 0.00011 | 1 |
| fib_min3_fallback_confirm | 0.72 | [0.58, 0.86] | 0.51 | 0.72 | [0.58, 0.86] | 0.50 | 0.75 | 0.01 | [0.00, 0.03] | 0.69 | 0.00 | 0.00 | 1.04 | 906 | [888, 926] | 0.00013 | 3.09 |
| full | 0.78 | [0.64, 0.92] | 0.59 | 0.78 | [0.64, 0.92] | 0.53 | 0.86 | 0.00813 | [0.00, 0.02] | 0.76 | 0.00 | 0.00 | 1.00 | 1190 | [1122, 1248] | 0.00015 | 10.72 |

recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.83 | 0.75 | 1.00 |
| fib_min3_fallback_confirm | 0.83 | 0.67 | 0.67 |
| full | 0.83 | 0.75 | 0.75 |

fragment recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.28 | 0.25 | 1.00 |
| fib_min3_fallback_confirm | 0.64 | 0.22 | 0.67 |
| full | 0.72 | 0.31 | 0.75 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.83 | 0.75 | 1 |
| fib_min3_fallback_confirm | 0.83 | 0.67 | 0.67 |
| full | 0.83 | 0.75 | 0.75 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct3_twin | ct3_span_twin | ct3_concat_twin |
|---|---|---|---|
| per_message | 0.00 | 0.67 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.25 | 0.00 |
| full | 0.00 | 0.25 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct3 | ct3_span | ct3_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.83 | 0.33 | 1.00 | 0.72 |
| fib_min3_fallback_confirm | 0.83 | 0.50 | 0.67 | 0.67 |
| full | 0.83 | 0.58 | 0.75 | 0.72 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | -0.08 | [-0.25, 0.08] | no (CI contains 0) |
| full vs per_message | root_recall | -0.08 | [-0.25, 0.08] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 407 | [340, 465] | yes |
| fib_min3_fallback_confirm vs per_message | recall | -0.14 | [-0.31, 0.03] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | -0.14 | [-0.31, 0.03] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 123 | [107, 142] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.06 | [-0.17, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.06 | [-0.17, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -284 | [-345, -212] | yes |