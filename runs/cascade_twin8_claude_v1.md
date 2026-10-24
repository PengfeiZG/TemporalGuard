| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.00 | [0.00, 0.00] | 0.00 | 0 | [0.00, 0.00] | 0.00 | n/a | 0.00 | [0.00, 0.00] | n/a | 0.00 | 0.00 | 1.01 | 1712 | [1699, 1730] | 0.00034 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 0.83 | 0.00 | 0.00 | 1.29 | 2377 | [2264, 2521] | 0.00135 | 3.92 |
| full | 1.00 | [1.00, 1.00] | 0.90 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 0.90 | 0.00 | 0.00 | 1.14 | 2581 | [2442, 2719] | 0.00131 | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 1.00 | 0.67 |
| full | 1.00 | 0.79 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0 | 0 |
| fib_min3_fallback_confirm | 1 | 1 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.00 | 0.00 |
| full | 0.00 | 0.00 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 1.00 | [1.00, 1.00] | yes |
| full vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| full vs per_message | tokens_per_output | 869 | [731, 1008] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 665 | [556, 794] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -204 | [-351, -16.21] | yes |