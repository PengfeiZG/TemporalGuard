| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.67 | 0 | [0.00, 0.00] | 1.00 | 0.57 | 0.06 | [0.03, 0.12] | 0.67 | 0.00 | 0.00 | 1.00 | 522 | [521, 524] | 1 |
| fib | 1.00 | [1.00, 1.00] | 0.67 | 0 | [0.00, 0.00] | 1.00 | 0.57 | 0.06 | [0.03, 0.12] | 0.67 | 0.00 | 0.00 | 1.00 | 522 | [521, 524] | 1 |
| full | 1.00 | [1.00, 1.00] | 0.79 | 0.38 | [0.12, 0.75] | 1.00 | 0.42 | 0.09 | [0.05, 0.16] | 0.79 | 0.00 | 0.00 | 1.00 | 962 | [869, 1024] | 12.06 |

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
| full | 0.67 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | dependent | dependent_span |
|---|---|---|
| per_message | 0 | 0 |
| fib | 0 | 0 |
| full | 0 | 0.75 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | dependent_twin | dependent_span_twin | benign |
|---|---|---|---|
| per_message | 1.00 | 1.00 | 0.00 |
| fib | 1.00 | 1.00 | 0.00 |
| full | 1.00 | 1.00 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | dependent | dependent_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib | 0.00 | 0.00 | 0.00 |
| full | 0.00 | 0.00 | 0.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | root_recall | -0.38 | [-0.75, -0.12] | yes |
| fib vs full | tokens_per_output | -439 | [-501, -344] | yes |
| full vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.38 | [0.12, 0.75] | yes |
| full vs per_message | tokens_per_output | 439 | [345, 502] | yes |