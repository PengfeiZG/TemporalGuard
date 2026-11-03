| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.89 | 0.85 | [0.74, 0.94] | 0.87 | 0.71 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.16 | 827 | [793, 866] | 4.77 |
| fib_min3_fallback_confirm_semgated | 0.81 | [0.70, 0.93] | 0.67 | 0.63 | [0.50, 0.76] | 0.61 | 0.91 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.36 | 0.24 | 199 | [150, 255] | 1.46 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm_semgated | 0.81 | 0.81 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 0.99 | 0.79 |
| fib_min3_fallback_confirm_semgated | 0.75 | 0.58 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| fib_min3_fallback_confirm | 0.96 | 0.74 |
| fib_min3_fallback_confirm_semgated | 0.78 | 0.48 |