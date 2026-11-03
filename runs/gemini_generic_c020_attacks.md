| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.89 | 0.85 | [0.74, 0.94] | 0.87 | 0.71 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.16 | 827 | [793, 866] | 4.77 |
| fib_min3_fallback_confirm_semgated | 0.96 | [0.91, 1.00] | 0.83 | 0.80 | [0.69, 0.89] | 0.83 | 0.90 | n/a | [n/a, n/a] | 0.81 | 0.00 | 0.15 | 0.43 | 333 | [284, 386] | 2.26 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_semgated | 1.00 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 0.99 | 0.79 |
| fib_min3_fallback_confirm_semgated | 0.94 | 0.72 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 0.96 | 0.74 |
| fib_min3_fallback_confirm_semgated | 0.96 | 0.63 |