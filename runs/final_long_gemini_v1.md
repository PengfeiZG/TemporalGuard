| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 522 | [521, 522] | 1 |
| fixed5 | 0.88 | [0.69, 1.00] | 0.38 | 0.25 | [0.06, 0.50] | 0.88 | 0.95 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.00 | 669 | [667, 671] | 4.64 |
| fixed5_fallback_confirm | 0.88 | [0.69, 1.00] | 0.58 | 0.88 | [0.69, 1.00] | 0.88 | 0.95 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.03 | 707 | [698, 715] | 5.15 |
| pow2_min3_fallback_confirm | 0.88 | [0.69, 1.00] | 0.58 | 0.88 | [0.69, 1.00] | 0.88 | 1.00 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.03 | 669 | [662, 674] | 4.25 |
| fib_min3_fallback_confirm | 0.75 | [0.56, 0.94] | 0.50 | 0.75 | [0.56, 0.94] | 0.75 | 0.94 | n/a | [n/a, n/a] | 0.62 | 0.00 | 0.00 | 1.03 | 629 | [619, 639] | 3.32 |
| fib_min3 | 0.75 | [0.56, 0.94] | 0.33 | 0.25 | [0.06, 0.50] | 0.75 | 0.94 | n/a | [n/a, n/a] | 0.41 | 0.00 | 0.00 | 1.00 | 597 | [596, 599] | 2.89 |
| full | 1.00 | [1.00, 1.00] | 0.73 | 1 | [1.00, 1.00] | 1.00 | 0.68 | n/a | [n/a, n/a] | 0.73 | 0.00 | 0.00 | 1.00 | 1059 | [1021, 1094] | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.69 |
| fixed5 | 0.88 |
| fixed5_fallback_confirm | 0.88 |
| pow2_min3_fallback_confirm | 0.88 |
| fib_min3_fallback_confirm | 0.75 |
| fib_min3 | 0.75 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.31 |
| fixed5 | 0.38 |
| fixed5_fallback_confirm | 0.58 |
| pow2_min3_fallback_confirm | 0.58 |
| fib_min3_fallback_confirm | 0.50 |
| fib_min3 | 0.33 |
| full | 0.73 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.25 |
| fixed5_fallback_confirm | 0.88 |
| pow2_min3_fallback_confirm | 0.88 |
| fib_min3_fallback_confirm | 0.75 |
| fib_min3 | 0.25 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3 vs full | recall | -0.25 | [-0.44, -0.06] | yes |
| fib_min3 vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib_min3 vs full | tokens_per_output | -461 | [-496, -425] | yes |
| full vs per_message | recall | 0.31 | [0.12, 0.56] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 537 | [500, 572] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.19 | [0.00, 0.38] | no (CI contains 0) |
| fixed5_fallback_confirm vs per_message | root_recall | 0.62 | [0.38, 0.88] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 185 | [177, 192] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 108 | [97.31, 117] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.19 | [0.00, 0.38] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.62 | [0.38, 0.88] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 147 | [140, 152] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.25 | [-0.44, -0.06] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.25 | [-0.44, -0.06] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -429 | [-463, -393] | yes |
| pow2_min3_fallback_confirm vs full | recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -390 | [-421, -355] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -39.68 | [-48.16, -31.35] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -77.25 | [-87.33, -68.33] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -37.57 | [-43.09, -34.34] | yes |