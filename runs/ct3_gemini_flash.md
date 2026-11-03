| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.61 | [0.44, 0.75] | 0.35 | 0.61 | [0.44, 0.75] | 0.39 | 0.79 | 0.00610 | [0.00, 0.01] | 0.57 | 0.00 | 0.00 | 1.00 | 561 | [557, 564] | 1 |
| fib_min3_fallback_confirm | 0.47 | [0.31, 0.64] | 0.25 | 0.47 | [0.31, 0.64] | 0.36 | 0.83 | 0.00407 | [0.00, 0.01] | 0.52 | 0.00 | 0.00 | 1.01 | 665 | [655, 676] | 2.86 |
| full | 0.47 | [0.31, 0.64] | 0.25 | 0.47 | [0.31, 0.64] | 0.33 | 0.81 | 0.00407 | [0.00, 0.01] | 0.52 | 0.00 | 0.00 | 1.00 | 1051 | [971, 1119] | 10.72 |

recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.58 | 0.58 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.58 | 0.33 |
| full | 0.42 | 0.58 | 0.42 |

fragment recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.19 | 0.19 | 0.67 |
| fib_min3_fallback_confirm | 0.22 | 0.19 | 0.33 |
| full | 0.14 | 0.19 | 0.42 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.58 | 0.58 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.58 | 0.33 |
| full | 0.42 | 0.58 | 0.42 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct3_twin | ct3_span_twin | ct3_concat_twin |
|---|---|---|---|
| per_message | 0.00 | 0.25 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.17 | 0.00 |
| full | 0.00 | 0.17 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct3 | ct3_span | ct3_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.58 | 0.42 | 0.67 | 0.56 |
| fib_min3_fallback_confirm | 0.50 | 0.50 | 0.33 | 0.44 |
| full | 0.42 | 0.50 | 0.42 | 0.44 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | -0.14 | [-0.28, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | -0.14 | [-0.28, 0.00] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 491 | [411, 558] | yes |
| fib_min3_fallback_confirm vs per_message | recall | -0.14 | [-0.31, 0.03] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | -0.14 | [-0.31, 0.03] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 105 | [96.94, 114] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [-0.11, 0.11] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [-0.11, 0.11] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -386 | [-451, -308] | yes |