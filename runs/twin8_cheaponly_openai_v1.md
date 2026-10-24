| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.25, 0.75] | 0.17 | 0.19 | [0.00, 0.44] | 0.50 | 0.62 | 0.02 | [0.00458, 0.03] | 0.33 | 0.00 | 0.00 | 1.00 | 749 | [748, 749] | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.75 | 0.03 | [0.02, 0.04] | 0.82 | 0.00 | 0.00 | 1.07 | 877 | [860, 898] | 3.40 |
| full | 1.00 | [1.00, 1.00] | 0.85 | 1 | [1.00, 1.00] | 1.00 | 0.72 | 0.03 | [0.01, 0.05] | 0.82 | 0.00 | 0.00 | 1.00 | 1095 | [1048, 1125] | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.38 | 0.62 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.12 | 0.21 |
| fib_min3_fallback_confirm | 1.00 | 0.67 |
| full | 1.00 | 0.71 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.12 | 0.25 |
| fib_min3_fallback_confirm | 1 | 1 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.38 | 0.00 |
| fib_min3_fallback_confirm | 0.25 | 0.88 | 0.00 |
| full | 0.25 | 0.75 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.12 | 0.25 | 0.19 |
| fib_min3_fallback_confirm | 0.75 | 0.12 | 0.44 |
| full | 0.75 | 0.25 | 0.50 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| full vs per_message | root_recall | 0.81 | [0.62, 1.00] | yes |
| full vs per_message | tokens_per_output | 346 | [299, 377] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.81 | [0.62, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 128 | [111, 149] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -218 | [-256, -162] | yes |