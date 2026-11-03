| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.67 | [0.50, 0.81] | 0.46 | 0.31 | [0.17, 0.44] | 0.36 | 0.80 | n/a | [n/a, n/a] | 0.68 | 0.00 | 0.00 | 1.00 | 789 | [775, 804] | 0.00221 | 1 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.50 | 0.58 | 0.92 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.22 | 0.25 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.92 |