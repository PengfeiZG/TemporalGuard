| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.62 | [0.25, 1.00] | 0.25 | 0.25 | [0.00, 0.50] | 0.62 | 0.67 | 0.02 | [0.00, 0.03] | 0.40 | 0.00 | 0.00 | 1.03 | 773 | [761, 786] | 0.00018 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.79 | 1 | [1.00, 1.00] | 1.00 | 0.80 | 0.02 | [0.00, 0.03] | 0.79 | 0.00 | 0.00 | 1.17 | 978 | [921, 1047] | 0.00045 | 3.36 |
| full | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.81 | 0.02 | [0.00, 0.03] | 0.83 | 0.00 | 0.00 | 1.06 | 1159 | [1093, 1206] | 0.00031 | 12.06 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.75 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.17 | 0.33 |
| fib_min3_fallback_confirm | 0.92 | 0.67 |
| full | 1.00 | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1 | 1 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.50 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.75 | 0.00 |
| full | 0.00 | 0.75 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.25 | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1.00 | 0.25 | 0.62 |
| full | 1.00 | 0.25 | 0.62 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.38 | [0.00, 0.75] | no (CI contains 0) |
| full vs per_message | root_recall | 0.75 | [0.50, 1.00] | yes |
| full vs per_message | tokens_per_output | 386 | [322, 431] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.38 | [0.00, 0.75] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 205 | [153, 268] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -181 | [-236, -101] | yes |