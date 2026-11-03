| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.56 | [0.31, 0.81] | 0.27 | 0.25 | [0.06, 0.50] | 0.56 | 0.59 | 0.03 | [0.01, 0.04] | 0.48 | 0.00 | 0.00 | 1.00 | 522 | [521, 523] | 0.00025 | 1 |
| fib_min3_fallback_confirm | 0.81 | [0.62, 1.00] | 0.58 | 0.81 | [0.62, 1.00] | 0.81 | 0.66 | 0.03 | [0.02, 0.05] | 0.66 | 0.00 | 0.00 | 1.03 | 625 | [615, 638] | 0.00029 | 3.14 |
| full | 1.00 | [1.00, 1.00] | 0.77 | 1 | [1.00, 1.00] | 1.00 | 0.64 | 0.02 | [0.00664, 0.03] | 0.71 | 0.00 | 0.00 | 1.00 | 950 | [892, 989] | 0.00037 | 12.02 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.62 |
| fib_min3_fallback_confirm | 1.00 | 0.62 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.29 |
| fib_min3_fallback_confirm | 0.75 | 0.42 |
| full | 0.83 | 0.71 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib_min3_fallback_confirm | 1 | 0.62 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.50 | 0.62 | 0.00 |
| fib_min3_fallback_confirm | 0.62 | 0.62 | 0.00 |
| full | 0.38 | 0.38 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 0.38 | 0.00 | 0.19 |
| full | 0.62 | 0.62 | 0.62 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.44 | [0.19, 0.69] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 429 | [370, 467] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.25 | [0.00, 0.50] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.56 | [0.31, 0.81] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 103 | [93.42, 116] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -325 | [-365, -265] | yes |