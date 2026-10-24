| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.02 | [0.01, 0.04] | n/a | 0.00 | n/a | 1.00 | 787 | [776, 798] | 1 |
| fib_min3_fallback_confirm | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.03 | [0.02, 0.04] | n/a | 0.00 | n/a | 1.06 | 927 | [878, 986] | 3.30 |
| full | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.02 | [0.01, 0.03] | n/a | 0.00 | n/a | 1.00 | 1057 | [1011, 1107] | 8.51 |

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
| per_message | 0.28 |
| fib_min3_fallback_confirm | 0.35 |
| full | 0.28 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | n/a | [n/a, n/a] | yes |
| full vs per_message | root_recall | n/a | [n/a, n/a] | yes |
| full vs per_message | tokens_per_output | 270 | [223, 321] | yes |
| fib_min3_fallback_confirm vs per_message | recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 140 | [95.06, 196] | yes |
| fib_min3_fallback_confirm vs full | recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs full | root_recall | n/a | [n/a, n/a] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -130 | [-169, -88.51] | yes |