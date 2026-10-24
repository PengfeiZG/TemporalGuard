| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.62 | [0.38, 0.88] | 0.21 | 0.25 | [0.06, 0.50] | 0.62 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 748 | [748, 749] | 0.00011 | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.38 | 0.12 | [0.00, 0.31] | 1.00 | 0.78 | n/a | [n/a, n/a] | 0.35 | 0.00 | 0.00 | 1.00 | 866 | [865, 868] | 0.00012 | 4.64 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.82 | n/a | [n/a, n/a] | 0.64 | 0.00 | 0.00 | 1.05 | 928 | [916, 943] | 0.00013 | 5.41 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.82 | n/a | [n/a, n/a] | 0.62 | 0.00 | 0.00 | 1.06 | 904 | [892, 917] | 0.00013 | 4.54 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.90 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.05 | 867 | [856, 879] | 0.00012 | 3.53 |
| fib_min3 | 1.00 | [1.00, 1.00] | 0.38 | 0.12 | [0.00, 0.31] | 1.00 | 0.90 | n/a | [n/a, n/a] | 0.36 | 0.00 | 0.00 | 1.01 | 818 | [810, 831] | 0.00011 | 2.94 |
| full | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.86 | n/a | [n/a, n/a] | 0.66 | 0.00 | 0.00 | 1.00 | 1179 | [1149, 1208] | 0.00015 | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.62 |
| fixed5 | 1.00 |
| fixed5_fallback_confirm | 1.00 |
| pow2_min3_fallback_confirm | 1.00 |
| fib_min3_fallback_confirm | 1.00 |
| fib_min3 | 1.00 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.21 |
| fixed5 | 0.38 |
| fixed5_fallback_confirm | 0.67 |
| pow2_min3_fallback_confirm | 0.67 |
| fib_min3_fallback_confirm | 0.67 |
| fib_min3 | 0.38 |
| full | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.12 |
| fixed5_fallback_confirm | 1 |
| pow2_min3_fallback_confirm | 1 |
| fib_min3_fallback_confirm | 1 |
| fib_min3 | 0.12 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | -0.88 | [-1.00, -0.69] | yes |
| fib_min3 vs full | tokens_per_output | -360 | [-390, -327] | yes |
| full vs per_message | recall | 0.38 | [0.12, 0.62] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 431 | [400, 459] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.38 | [0.12, 0.62] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 180 | [167, 195] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.38 | [0.12, 0.62] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 118 | [108, 131] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.38 | [0.12, 0.62] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 156 | [144, 169] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -312 | [-344, -277] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -275 | [-308, -239] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -37.39 | [-53.88, -18.28] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -61.61 | [-75.63, -47.34] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -24.23 | [-38.04, -9.98] | yes |