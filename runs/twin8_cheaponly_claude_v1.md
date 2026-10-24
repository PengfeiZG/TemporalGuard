| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.25 | [0.06, 0.50] | 0.08 | 0 | [0.00, 0.00] | 0.25 | 0.50 | 0.01 | [0.00276, 0.03] | 0.33 | 0.00 | 0.00 | 1.00 | 1690 | [1689, 1692] | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.67 | 0.04 | [0.02, 0.07] | 0.82 | 0.00 | 0.00 | 1.13 | 2070 | [2027, 2112] | 3.91 |
| full | 1.00 | [1.00, 1.00] | 0.90 | 1 | [1.00, 1.00] | 1.00 | 0.38 | 0.06 | [0.03, 0.09] | 0.79 | 0.00 | 0.00 | 1.00 | 2261 | [2186, 2311] | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.08 | 0.08 |
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
| per_message | 0.25 | 0.25 | 0.00 |
| fib_min3_fallback_confirm | 0.75 | 0.50 | 0.00 |
| full | 0.75 | 0.62 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 0.25 | 0.50 | 0.38 |
| full | 0.25 | 0.38 | 0.31 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.75 | [0.56, 0.94] | yes |
| full vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| full vs per_message | tokens_per_output | 571 | [496, 622] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.75 | [0.56, 0.94] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 380 | [338, 421] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -191 | [-244, -104] | yes |