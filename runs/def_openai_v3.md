| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.38 | [0.00, 0.75] | 0.12 | 0.38 | 0.50 | 0.02 | [0.00, 0.03] | 0.33 | 0.00 | 0.00 | 1.00 | 749 | [749, 750] | 1 |
| fib | 0.25 | [0.00, 0.62] | 0.08 | 0.25 | 0.50 | 0.01 | [0.00, 0.03] | 0.33 | 0.00 | 0.00 | 1.01 | 759 | [752, 766] | 1.02 |
| full | 1.00 | [1.00, 1.00] | 0.79 | 1.00 | 0.52 | 0.05 | [0.02, 0.10] | 0.77 | 0.00 | 0.00 | 1.00 | 1102 | [1029, 1151] | 12.06 |

recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.25 | 0.50 |
| fib | 0.25 | 0.25 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | definitional_span |
|---|---|---|
| per_message | 0.08 | 0.17 |
| fib | 0.08 | 0.08 |
| full | 0.92 | 0.67 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | definitional_twin | definitional_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.50 | 0.00 |
| fib | 0.25 | 0.25 | 0.00 |
| full | 0.75 | 0.75 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | definitional | definitional_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib | 0.00 | 0.00 | 0.00 |
| full | 0.25 | 0.25 | 0.25 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | -0.75 | [-1.00, -0.38] | yes |
| fib vs full | tokens_per_output | -343 | [-386, -274] | yes |