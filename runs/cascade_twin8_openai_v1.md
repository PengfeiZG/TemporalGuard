| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.25, 0.75] | 0.17 | 0.19 | [0.00, 0.44] | 0.50 | 0.62 | 0.02 | [0.00458, 0.03] | 0.33 | 0.00 | 0.00 | 1.02 | 767 | [760, 777] | 0.00016 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.81 | 1 | [1.00, 1.00] | 1.00 | 0.81 | 0.02 | [0.00789, 0.03] | 0.81 | 0.00 | 0.00 | 1.19 | 990 | [946, 1051] | 0.00044 | 3.47 |
| full | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.81 | 0.02 | [0.00441, 0.04] | 0.83 | 0.00 | 0.00 | 1.07 | 1163 | [1121, 1196] | 0.00034 | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.75 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.08 | 0.25 |
| fib_min3_fallback_confirm | 0.96 | 0.67 |
| full | 1.00 | 0.67 |

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
| fib_min3_fallback_confirm | 0.00 | 0.75 | 0.00 |
| full | 0.12 | 0.50 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.12 | 0.38 | 0.25 |
| fib_min3_fallback_confirm | 1.00 | 0.25 | 0.62 |
| full | 0.88 | 0.50 | 0.69 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| full vs per_message | root_recall | 0.81 | [0.62, 1.00] | yes |
| full vs per_message | tokens_per_output | 395 | [350, 431] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.81 | [0.62, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 223 | [180, 279] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -172 | [-218, -104] | yes |