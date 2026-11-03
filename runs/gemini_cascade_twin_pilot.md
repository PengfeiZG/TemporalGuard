| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.12, 0.88] | 0.25 | 0.25 | [0.00, 0.50] | 0.50 | 0.60 | 0.02 | [0.00565, 0.04] | 0.50 | 0.00 | 0.00 | 1.03 | 550 | [533, 573] | 0.00046 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.71 | 0.02 | [0.00741, 0.03] | 0.67 | 0.00 | 0.00 | 1.11 | 729 | [691, 767] | 0.00100 | 3.21 |
| full | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.91 | 0.00529 | [0.00, 0.02] | 0.67 | 0.00 | 0.00 | 1.06 | 1036 | [951, 1098] | 0.00091 | 12.06 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.50 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 0.67 | 0.67 |
| full | 0.67 | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1 | 1 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.50 | 0.50 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 1.00 | 0.00 |
| full | 0.00 | 0.25 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 1.00 | 0.00 | 0.50 |
| full | 1.00 | 0.75 | 0.88 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.50 | [0.12, 0.88] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 1.00] | yes |
| full vs per_message | tokens_per_output | 486 | [400, 547] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.50 | [0.12, 0.88] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 179 | [147, 210] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -307 | [-361, -227] | yes |