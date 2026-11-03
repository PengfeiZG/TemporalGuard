| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.12, 0.88] | 0.25 | 0.25 | [0.00, 0.50] | 0.50 | 0.60 | 0.02 | [0.00565, 0.04] | 0.50 | 0.00 | 0.00 | 1.00 | 522 | [521, 523] | 1 |
| fib | 0.50 | [0.12, 0.88] | 0.25 | 0.25 | [0.00, 0.50] | 0.50 | 0.60 | 0.02 | [0.00565, 0.04] | 0.50 | 0.00 | 0.00 | 1.00 | 522 | [521, 523] | 1 |
| full | 1.00 | [1.00, 1.00] | 0.83 | 1 | [1.00, 1.00] | 1.00 | 0.78 | 0.02 | [0.00641, 0.04] | 0.75 | 0.00 | 0.00 | 1.00 | 956 | [863, 1018] | 12.06 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.50 | 0.50 |
| fib | 0.50 | 0.50 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib | 0.25 | 0.25 |
| full | 0.92 | 0.75 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fib | 0.25 | 0.25 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.50 | 0.50 | 0.00 |
| fib | 0.50 | 0.50 | 0.00 |
| full | 0.25 | 0.75 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fib | 0.00 | 0.00 | 0.00 |
| full | 0.75 | 0.25 | 0.50 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | -0.50 | [-0.88, -0.12] | yes |
| fib vs full | root_recall | -0.75 | [-1.00, -0.50] | yes |
| fib vs full | tokens_per_output | -435 | [-496, -340] | yes |
| full vs per_message | recall | 0.50 | [0.12, 0.88] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 1.00] | yes |
| full vs per_message | tokens_per_output | 435 | [342, 497] | yes |