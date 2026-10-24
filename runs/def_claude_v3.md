| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.12 | [0.00, 0.38] | 0.04 | 0.12 | 0.50 | 0.01 | [0.00, 0.02] | 0.33 | 0.00 | 0.00 | 1.00 | 1691 | [1689, 1692] | 1 |
| fib | 0.62 | [0.25, 1.00] | 0.38 | 0.62 | 0.56 | 0.02 | [0.01, 0.04] | 0.60 | 0.00 | 0.00 | 1.12 | 1918 | [1846, 1989] | 1.56 |
| full | 1.00 | [1.00, 1.00] | 0.88 | 1.00 | 0.59 | 0.03 | [0.01, 0.06] | 0.85 | 0.00 | 0.00 | 1.00 | 2270 | [2150, 2349] | 12.06 |

recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.25 | 0.00 |
| fib | 0.75 | 0.50 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.08 | 0.00 |
| fib | 0.50 | 0.25 |
| full | 1.00 | 0.75 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | definitional_twin | definitional_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.00 | 0.00 |
| fib | 0.50 | 0.50 | 0.00 |
| full | 0.50 | 0.75 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | definitional | definitional_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib | 0.25 | 0.00 | 0.12 |
| full | 0.50 | 0.25 | 0.38 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | -0.38 | [-0.75, 0.00] | no (CI contains 0) |
| fib vs full | tokens_per_output | -352 | [-427, -235] | yes |