| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.25 | [0.06, 0.50] | 0.08 | 0 | [0.00, 0.00] | 0.25 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1689 | [1688, 1691] | 0.00026 | 1 |
| fixed5 | 0.62 | [0.38, 0.88] | 0.23 | 0 | [0.00, 0.00] | 0.62 | 0.91 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1884 | [1881, 1886] | 0.00029 | 4.64 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.04 | 1992 | [1973, 2014] | 0.00031 | 5.29 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.08 | 2036 | [2019, 2052] | 0.00032 | 4.78 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.14 | 2101 | [2078, 2140] | 0.00033 | 4.25 |
| fib_min3 | 0.75 | [0.50, 0.94] | 0.31 | 0.19 | [0.06, 0.38] | 0.75 | 0.92 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.10 | 2014 | [1990, 2053] | 0.00032 | 3.73 |
| full | 1.00 | [1.00, 1.00] | 0.71 | 1 | [1.00, 1.00] | 1.00 | 0.32 | n/a | [n/a, n/a] | 0.62 | 0.00 | 0.00 | 1.00 | 2406 | [2356, 2452] | 0.00035 | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.62 |
| fixed5_fallback_confirm | 1.00 |
| pow2_min3_fallback_confirm | 1.00 |
| fib_min3_fallback_confirm | 1.00 |
| fib_min3 | 0.75 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.08 |
| fixed5 | 0.23 |
| fixed5_fallback_confirm | 0.67 |
| pow2_min3_fallback_confirm | 0.67 |
| fib_min3_fallback_confirm | 0.67 |
| fib_min3 | 0.31 |
| full | 0.71 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0 |
| fixed5 | 0 |
| fixed5_fallback_confirm | 1 |
| pow2_min3_fallback_confirm | 1 |
| fib_min3_fallback_confirm | 1 |
| fib_min3 | 0.19 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3 vs full | recall | -0.25 | [-0.50, -0.06] | yes |
| fib_min3 vs full | root_recall | -0.81 | [-0.94, -0.62] | yes |
| fib_min3 vs full | tokens_per_output | -392 | [-446, -330] | yes |
| full vs per_message | recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| full vs per_message | tokens_per_output | 717 | [666, 763] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.75 | [0.50, 0.94] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 303 | [285, 324] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.75 | [0.50, 0.94] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 412 | [389, 451] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.75 | [0.50, 0.94] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 347 | [329, 363] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -305 | [-363, -239] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -370 | [-414, -317] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | 65.42 | [29.93, 108] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 109 | [81.20, 142] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 43.88 | [17.58, 67.34] | yes |