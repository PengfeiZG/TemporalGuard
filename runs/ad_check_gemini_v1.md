| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.80 | 0.72 | [0.59, 0.85] | 0.89 | 0.96 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.00 | 566 | [556, 577] | 1 |
| full | 0.96 | [0.91, 1.00] | 0.89 | 0.83 | [0.72, 0.93] | 0.87 | 0.61 | n/a | [n/a, n/a] | 0.82 | 0.00 | 0.00 | 1.00 | 1052 | [990, 1107] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 1.00 | 1.00 |
| full | 1.00 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.80 | 0.80 |
| full | 0.98 | 0.80 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.74 | 0.70 |
| full | 0.93 | 0.74 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | -0.04 | [-0.09, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.11 | [0.04, 0.20] | yes |
| full vs per_message | tokens_per_output | 486 | [423, 540] | yes |