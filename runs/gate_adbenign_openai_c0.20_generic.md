| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.03 | [0.02, 0.04] | n/a | 0.00 | n/a | 1.06 | 927 | [878, 986] | 0.00013 | 3.30 |
| fib_min3_fallback_confirm_semgated | n/a | [n/a, n/a] | n/a | n/a | [n/a, n/a] | n/a | 0.00 | 0.01 | [0.00493, 0.02] | n/a | 0.00 | n/a | 0.25 | 219 | [159, 286] | 0.00003 | 0.77 |

recall by attack family
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_semgated |

fragment recall by attack family
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_semgated |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy |
|---|
| fib_min3_fallback_confirm |
| fib_min3_fallback_confirm_semgated |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | agentdojo_benign |
|---|---|
| fib_min3_fallback_confirm | 0.35 |
| fib_min3_fallback_confirm_semgated | 0.17 |