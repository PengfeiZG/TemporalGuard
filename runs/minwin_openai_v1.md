| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.25, 0.75] | 0.17 | 0.12 | [0.00, 0.31] | 0.50 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 753 | [751, 754] | 1 |
| fib | 0.69 | [0.44, 0.88] | 0.33 | 0.31 | [0.06, 0.56] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.48 | 0.00 | 0.00 | 1.07 | 808 | [771, 841] | 1.14 |
| fib_min3 | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.94 | 0.00 | 0.00 | 1.00 | 807 | [805, 809] | 2.45 |
| pow2 | 0.69 | [0.44, 0.88] | 0.33 | 0.31 | [0.06, 0.56] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.48 | 0.00 | 0.00 | 1.07 | 808 | [771, 841] | 1.14 |
| pow2_min3 | 1.00 | [1.00, 1.00] | 0.90 | 1 | [1.00, 1.00] | 1.00 | 0.94 | n/a | [n/a, n/a] | 0.90 | 0.00 | 0.00 | 1.00 | 816 | [813, 820] | 2.73 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.96 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.00 | 833 | [828, 837] | 3.18 |
| fib_confirm | 0.69 | [0.44, 0.88] | 0.46 | 0.69 | [0.44, 0.88] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.19 | 916 | [855, 975] | 1.62 |
| full | 1.00 | [1.00, 1.00] | 0.98 | 1 | [1.00, 1.00] | 1.00 | 0.97 | n/a | [n/a, n/a] | 0.98 | 0.00 | 0.00 | 1.00 | 839 | [831, 846] | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.25 | 0.75 |
| fib | 0.38 | 1.00 |
| fib_min3 | 1.00 | 1.00 |
| pow2 | 0.38 | 1.00 |
| pow2_min3 | 1.00 | 1.00 |
| fixed5 | 1.00 | 1.00 |
| fib_confirm | 0.38 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.08 | 0.25 |
| fib | 0.17 | 0.50 |
| fib_min3 | 0.88 | 1.00 |
| pow2 | 0.17 | 0.50 |
| pow2_min3 | 0.83 | 0.96 |
| fixed5 | 0.92 | 1.00 |
| fib_confirm | 0.25 | 0.67 |
| full | 0.96 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0.25 |
| fib | 0.12 | 0.50 |
| fib_min3 | 1 | 1 |
| pow2 | 0.12 | 0.50 |
| pow2_min3 | 1 | 1 |
| fixed5 | 1 | 1 |
| fib_confirm | 0.38 | 1 |
| full | 1 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | recall | -0.31 | [-0.56, -0.12] | yes |
| fib vs fixed5 | root_recall | -0.69 | [-0.94, -0.44] | yes |
| fib vs fixed5 | tokens_per_output | -25.18 | [-58.76, 8.01] | no (CI contains 0) |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.38 | [0.12, 0.56] | yes |
| fib_confirm vs fib | tokens_per_output | 109 | [71.01, 151] | yes |
| fib vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib vs full | root_recall | -0.69 | [-0.94, -0.44] | yes |
| fib vs full | tokens_per_output | -31.40 | [-64.31, 0.94] | no (CI contains 0) |
| fib_confirm vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib_confirm vs full | root_recall | -0.31 | [-0.56, -0.12] | yes |
| fib_confirm vs full | tokens_per_output | 77.48 | [17.78, 135] | yes |
| fib_min3 vs fib | recall | 0.31 | [0.12, 0.56] | yes |
| fib_min3 vs fib | root_recall | 0.69 | [0.44, 0.94] | yes |
| fib_min3 vs fib | tokens_per_output | -0.23 | [-33.95, 35.75] | no (CI contains 0) |
| pow2_min3 vs pow2 | recall | 0.31 | [0.12, 0.56] | yes |
| pow2_min3 vs pow2 | root_recall | 0.69 | [0.44, 0.94] | yes |
| pow2_min3 vs pow2 | tokens_per_output | 8.93 | [-25.25, 44.55] | no (CI contains 0) |
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | tokens_per_output | -31.62 | [-39.09, -24.59] | yes |
| fib_min3 vs fib_confirm | recall | 0.31 | [0.12, 0.56] | yes |
| fib_min3 vs fib_confirm | root_recall | 0.31 | [0.12, 0.56] | yes |
| fib_min3 vs fib_confirm | tokens_per_output | -109 | [-167, -47.80] | yes |