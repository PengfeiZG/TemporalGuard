| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.89 | [0.80, 0.96] | 0.56 | 0.39 | [0.26, 0.52] | 0.78 | 0.92 | n/a | [n/a, n/a] | 0.61 | 0.00 | 0.00 | 1.00 | 1748 | [1736, 1762] | 1 |
| full | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.75 | n/a | [n/a, n/a] | 0.84 | 0.00 | 0.00 | 1.00 | 2381 | [2303, 2456] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.93 | 0.85 |
| full | 1.00 | 0.96 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.58 | 0.54 |
| full | 1.00 | 0.85 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.41 | 0.37 |
| full | 1 | 0.85 |