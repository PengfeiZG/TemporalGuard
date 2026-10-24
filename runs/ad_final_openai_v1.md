| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.98 | [0.94, 1.00] | 0.77 | 0.67 | [0.54, 0.80] | 0.87 | 0.93 | n/a | [n/a, n/a] | 0.75 | 0.00 | 0.00 | 1.00 | 789 | [779, 798] | 1 |
| fixed5_fallback_confirm | 0.96 | [0.91, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.89 | 0.76 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.13 | 1080 | [1043, 1120] | 6.41 |
| pow2_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.91 | 0.77 | n/a | [n/a, n/a] | 0.75 | 0.00 | 0.00 | 1.16 | 1083 | [1049, 1124] | 5.75 |
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.90 | 0.85 | [0.76, 0.94] | 0.87 | 0.81 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.16 | 1042 | [1012, 1076] | 4.69 |
| full | 0.94 | [0.87, 1.00] | 0.86 | 0.83 | [0.72, 0.93] | 0.87 | 0.82 | n/a | [n/a, n/a] | 0.81 | 0.00 | 0.00 | 1.00 | 1178 | [1127, 1227] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.96 | 1.00 |
| fixed5_fallback_confirm | 0.96 | 0.96 |
| pow2_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| full | 0.96 | 0.93 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.77 | 0.77 |
| fixed5_fallback_confirm | 1.00 | 0.80 |
| pow2_min3_fallback_confirm | 0.98 | 0.81 |
| fib_min3_fallback_confirm | 1.00 | 0.80 |
| full | 0.96 | 0.77 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.67 | 0.67 |
| fixed5_fallback_confirm | 1 | 0.70 |
| pow2_min3_fallback_confirm | 1 | 0.70 |
| fib_min3_fallback_confirm | 1 | 0.70 |
| full | 0.96 | 0.70 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | -0.04 | [-0.09, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.17 | [0.07, 0.28] | yes |
| full vs per_message | tokens_per_output | 390 | [338, 437] | yes |
| fixed5_fallback_confirm vs per_message | recall | -0.02 | [-0.07, 0.04] | no (CI contains 0) |
| fixed5_fallback_confirm vs per_message | root_recall | 0.19 | [0.07, 0.30] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 292 | [258, 325] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.00 | [-0.06, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.19 | [0.07, 0.30] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 254 | [227, 283] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.00 | [-0.06, 0.06] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.19 | [0.07, 0.30] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 294 | [264, 329] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.04 | [0.00, 0.09] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -136 | [-187, -69.82] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.04 | [0.00, 0.09] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -95.44 | [-140, -35.50] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -40.91 | [-61.66, -19.11] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -38.36 | [-65.86, -5.41] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.02 | [0.00, 0.06] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 2.54 | [-18.37, 27.38] | no (CI contains 0) |