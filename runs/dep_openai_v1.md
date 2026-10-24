| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.67 | 1.00 | 0.50 | 0.08 | [0.05, 0.14] | 0.67 | 0.00 | 0.00 | 1.00 | 752 | [751, 753] | 1 |
| fib | 1.00 | [1.00, 1.00] | 0.67 | 1.00 | 0.50 | 0.08 | [0.05, 0.14] | 0.67 | 0.00 | 0.00 | 1.00 | 752 | [751, 753] | 1 |
| full | 1.00 | [1.00, 1.00] | 0.92 | 1.00 | 0.48 | 0.08 | [0.05, 0.15] | 0.92 | 0.00 | 0.00 | 1.00 | 1104 | [1029, 1153] | 12.06 |

recall by attack family
| strategy | dependent | dependent_span |
|---|---|---|
| per_message | 1.00 | 1.00 |
| fib | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | dependent | dependent_span |
|---|---|---|
| per_message | 0.67 | 0.67 |
| fib | 0.67 | 0.67 |
| full | 0.92 | 0.92 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | dependent_twin | dependent_span_twin | benign |
|---|---|---|---|
| per_message | 1.00 | 1.00 | 0.00 |
| fib | 1.00 | 1.00 | 0.00 |
| full | 1.00 | 1.00 | 0.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | tokens_per_output | -352 | [-400, -276] | yes |