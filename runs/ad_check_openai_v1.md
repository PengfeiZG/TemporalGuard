| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.98 | [0.94, 1.00] | 0.77 | 0.67 | [0.54, 0.80] | 0.87 | 0.93 | n/a | [n/a, n/a] | 0.75 | 0.00 | 0.00 | 1.00 | 789 | [779, 798] | 1 |
| full | 0.94 | [0.87, 1.00] | 0.86 | 0.83 | [0.72, 0.93] | 0.87 | 0.82 | n/a | [n/a, n/a] | 0.81 | 0.00 | 0.00 | 1.00 | 1178 | [1127, 1227] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.96 | 1.00 |
| full | 0.96 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.77 | 0.77 |
| full | 0.96 | 0.77 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.67 | 0.67 |
| full | 0.96 | 0.70 |