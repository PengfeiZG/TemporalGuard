| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.12 | [0.00, 0.38] | 0.04 | 0 | [0.00, 0.00] | 0.12 | 0.50 | 0.00529 | [0.00, 0.02] | 0.33 | 0.00 | 0.00 | 1.00 | 523 | [521, 525] | 1 |
| fib | 0.12 | [0.00, 0.38] | 0.04 | 0 | [0.00, 0.00] | 0.12 | 0.50 | 0.00529 | [0.00, 0.02] | 0.33 | 0.00 | 0.00 | 1.00 | 523 | [521, 525] | 1 |
| full | 0.62 | [0.25, 1.00] | 0.46 | 0.62 | [0.25, 1.00] | 0.62 | 0.67 | 0.01 | [0.00, 0.03] | 0.67 | 0.00 | 0.00 | 1.00 | 957 | [862, 1019] | 12.06 |

recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.25 | 0.00 |
| fib | 0.25 | 0.00 |
| full | 0.75 | 0.50 |

fragment recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.08 | 0.00 |
| fib | 0.08 | 0.00 |
| full | 0.58 | 0.33 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0 | 0 |
| fib | 0 | 0 |
| full | 0.75 | 0.50 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | definitional_twin | definitional_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.00 | 0.00 |
| fib | 0.25 | 0.00 | 0.00 |
| full | 0.25 | 0.25 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | definitional | definitional_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib | 0.00 | 0.00 | 0.00 |
| full | 0.50 | 0.25 | 0.38 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | -0.50 | [-0.88, -0.12] | yes |
| fib vs full | root_recall | -0.62 | [-1.00, -0.25] | yes |
| fib vs full | tokens_per_output | -434 | [-494, -340] | yes |
| full vs per_message | recall | 0.50 | [0.12, 0.88] | yes |
| full vs per_message | root_recall | 0.62 | [0.25, 1.00] | yes |
| full vs per_message | tokens_per_output | 434 | [341, 494] | yes |