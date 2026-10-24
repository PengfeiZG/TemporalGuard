| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.67 | 1.00 | 0.59 | 0.06 | [0.03, 0.09] | 0.67 | 0.00 | 0.00 | 1.00 | 1692 | [1690, 1695] | 1 |
| fib | 1.00 | [1.00, 1.00] | 0.71 | 1.00 | 0.52 | 0.08 | [0.04, 0.13] | 0.71 | 0.00 | 0.00 | 1.17 | 2029 | [1892, 2178] | 1.85 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1.00 | 0.36 | 0.11 | [0.06, 0.17] | 0.97 | 0.00 | 0.00 | 1.00 | 2276 | [2156, 2355] | 12.06 |

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
| fib | 0.75 | 0.67 |
| full | 1.00 | 1.00 |

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
| fib vs full | tokens_per_output | -246 | [-395, -40.33] | yes |