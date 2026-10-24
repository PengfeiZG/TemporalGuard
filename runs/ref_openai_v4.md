| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.62 | [0.25, 1.00] | 0.25 | 0.25 | [0.00, 0.50] | 0.62 | 0.60 | 0.02 | [0.01, 0.04] | 0.40 | 0.00 | 0.00 | 1.00 | 749 | [748, 750] | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.71 | 0.62 | [0.25, 0.88] | 1.00 | 0.58 | 0.04 | [0.02, 0.06] | 0.70 | 0.00 | 0.00 | 1.00 | 860 | [852, 864] | 4.38 |
| pow2 | 1.00 | [1.00, 1.00] | 0.54 | 0.62 | [0.25, 0.88] | 1.00 | 0.71 | 0.02 | [0.01, 0.03] | 0.54 | 0.00 | 0.00 | 1.04 | 778 | [764, 799] | 1.07 |
| fib | 1.00 | [1.00, 1.00] | 0.54 | 0.62 | [0.25, 0.88] | 1.00 | 0.71 | 0.02 | [0.01, 0.03] | 0.54 | 0.00 | 0.00 | 1.04 | 778 | [764, 799] | 1.07 |
| fib_fallback | 1.00 | [1.00, 1.00] | 0.54 | 0.62 | [0.25, 0.88] | 1.00 | 0.71 | 0.02 | [0.01, 0.03] | 0.54 | 0.00 | 0.00 | 1.04 | 778 | [764, 799] | 1.07 |
| full | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.74 | 0.03 | [0.01, 0.04] | 0.83 | 0.00 | 0.00 | 1.00 | 1100 | [1026, 1148] | 12.06 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.75 |
| fixed5 | 1.00 | 1.00 |
| pow2 | 1.00 | 1.00 |
| fib | 1.00 | 1.00 |
| fib_fallback | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.17 | 0.33 |
| fixed5 | 1.00 | 0.42 |
| pow2 | 0.67 | 0.42 |
| fib | 0.67 | 0.42 |
| fib_fallback | 0.67 | 0.42 |
| full | 1.00 | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fixed5 | 1 | 0.25 |
| pow2 | 1 | 0.25 |
| fib | 1 | 0.25 |
| fib_fallback | 1 | 0.25 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.75 | 0.00 |
| fixed5 | 0.50 | 1.00 | 0.00 |
| pow2 | 0.00 | 1.00 | 0.00 |
| fib | 0.00 | 1.00 | 0.00 |
| fib_fallback | 0.00 | 1.00 | 0.00 |
| full | 0.25 | 1.00 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.25 | 0.00 | 0.12 |
| fixed5 | 0.50 | 0.00 | 0.25 |
| pow2 | 1.00 | 0.00 | 0.50 |
| fib | 1.00 | 0.00 | 0.50 |
| fib_fallback | 1.00 | 0.00 | 0.50 |
| full | 0.75 | 0.00 | 0.38 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | tokens_per_output | -81.22 | [-98.15, -53.59] | yes |
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | root_recall | -0.38 | [-0.75, -0.12] | yes |
| fib vs full | tokens_per_output | -322 | [-377, -230] | yes |
| fib_fallback vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |