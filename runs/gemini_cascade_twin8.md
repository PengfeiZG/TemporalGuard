| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.56 | [0.31, 0.81] | 0.25 | 0.25 | [0.06, 0.50] | 0.56 | 0.60 | 0.02 | [0.01, 0.04] | 0.44 | 0.00 | 0.00 | 1.04 | 557 | [544, 573] | 0.00051 | 1 |
| fib_min3_fallback_confirm | 0.75 | [0.56, 0.94] | 0.48 | 0.75 | [0.56, 0.94] | 0.75 | 0.75 | 0.02 | [0.00340, 0.03] | 0.64 | 0.00 | 0.00 | 1.09 | 697 | [661, 746] | 0.00090 | 3.02 |
| full | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.87 | 0.00917 | [0.00, 0.02] | 0.67 | 0.00 | 0.00 | 1.07 | 1042 | [969, 1117] | 0.00095 | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.62 |
| fib_min3_fallback_confirm | 1.00 | 0.50 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 0.67 | 0.29 |
| full | 0.67 | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1 | 0.50 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.50 | 0.50 | 0.00 |
| fib_min3_fallback_confirm | 0.25 | 0.38 | 0.00 |
| full | 0.25 | 0.12 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.12 | 0.06 |
| fib_min3_fallback_confirm | 0.75 | 0.12 | 0.44 |
| full | 0.75 | 0.88 | 0.81 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.44 | [0.19, 0.69] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 485 | [410, 554] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.19 | [-0.12, 0.50] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 140 | [109, 179] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.25 | [-0.44, -0.06] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.25 | [-0.44, -0.06] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -345 | [-417, -259] | yes |