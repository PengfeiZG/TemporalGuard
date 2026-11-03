| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.01 | [0.00493, 0.03] | n/a | 0.00 | n/a | 1.02 | 584 | [569, 603] | 0.00043 | 1 |
| fib_min3_fallback_confirm | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.01 | [0.00521, 0.03] | n/a | 0.00 | n/a | 1.05 | 695 | [663, 733] | 0.00055 | 2.93 |
| full | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.01 | [0.00357, 0.02] | n/a | 0.00 | n/a | 1.02 | 919 | [866, 986] | 0.00053 | 8.51 |

recall by attack family
| strategy |
|---|
| per_message |
| fib_min3_fallback_confirm |
| full |

fragment recall by attack family
| strategy |
|---|
| per_message |
| fib_min3_fallback_confirm |
| full |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy |
|---|
| per_message |
| fib_min3_fallback_confirm |
| full |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | agentdojo_benign |
|---|---|
| per_message | 0.17 |
| fib_min3_fallback_confirm | 0.17 |
| full | 0.15 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | n/a | [n/a, n/a] | yes |
| full vs per_message | root_recall | n/a | [n/a, n/a] | yes |
| full vs per_message | tokens_per_output | 335 | [278, 400] | yes |
| fib_min3_fallback_confirm vs per_message | recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 111 | [89.93, 136] | yes |
| fib_min3_fallback_confirm vs full | recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs full | root_recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -224 | [-289, -165] | yes |