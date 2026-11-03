| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.80 | 0.72 | [0.59, 0.85] | 0.89 | 0.96 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.00 | 566 | [556, 577] | 1 |
| fixed5_fallback_confirm | 0.96 | [0.91, 1.00] | 0.87 | 0.83 | [0.72, 0.93] | 0.89 | 0.69 | n/a | [n/a, n/a] | 0.79 | 0.00 | 0.00 | 1.13 | 870 | [834, 912] | 6.21 |
| pow2_min3_fallback_confirm | 0.96 | [0.91, 1.00] | 0.87 | 0.83 | [0.72, 0.93] | 0.87 | 0.70 | n/a | [n/a, n/a] | 0.79 | 0.00 | 0.00 | 1.15 | 852 | [818, 893] | 5.54 |
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.89 | 0.85 | [0.74, 0.94] | 0.87 | 0.71 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.16 | 827 | [793, 866] | 4.77 |
| full | 0.96 | [0.91, 1.00] | 0.89 | 0.83 | [0.72, 0.93] | 0.87 | 0.61 | n/a | [n/a, n/a] | 0.82 | 0.00 | 0.00 | 1.00 | 1052 | [990, 1107] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 1.00 | 1.00 |
| fixed5_fallback_confirm | 1.00 | 0.93 |
| pow2_min3_fallback_confirm | 1.00 | 0.93 |
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| full | 1.00 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.80 | 0.80 |
| fixed5_fallback_confirm | 0.98 | 0.77 |
| pow2_min3_fallback_confirm | 0.98 | 0.77 |
| fib_min3_fallback_confirm | 0.99 | 0.79 |
| full | 0.98 | 0.80 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.74 | 0.70 |
| fixed5_fallback_confirm | 0.93 | 0.74 |
| pow2_min3_fallback_confirm | 0.93 | 0.74 |
| fib_min3_fallback_confirm | 0.96 | 0.74 |
| full | 0.93 | 0.74 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | -0.04 | [-0.09, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.11 | [0.04, 0.20] | yes |
| full vs per_message | tokens_per_output | 486 | [423, 540] | yes |
| fixed5_fallback_confirm vs per_message | recall | -0.04 | [-0.09, 0.00] | no (CI contains 0) |
| fixed5_fallback_confirm vs per_message | root_recall | 0.11 | [0.04, 0.20] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 305 | [274, 339] | yes |
| fib_min3_fallback_confirm vs per_message | recall | -0.02 | [-0.06, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.13 | [0.06, 0.22] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 261 | [232, 294] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | -0.04 | [-0.09, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.11 | [0.04, 0.20] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 286 | [256, 323] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.02 | [0.00, 0.07] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -225 | [-281, -149] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [-0.06, 0.06] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -200 | [-253, -129] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.02 | [0.00, 0.07] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -25.35 | [-39.48, -10.41] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.02 | [0.00, 0.07] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -43.61 | [-59.97, -23.03] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [-0.06, 0.06] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -18.26 | [-33.01, -0.58] | yes |