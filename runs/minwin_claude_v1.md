| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.12 | [0.00, 0.31] | 0.04 | 0 | [0.00, 0.00] | 0.12 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1698 | [1695, 1701] | 1 |
| fib | 0.94 | [0.81, 1.00] | 0.62 | 0.94 | [0.81, 1.00] | 0.94 | 1.00 | n/a | [n/a, n/a] | 0.66 | 0.00 | 0.00 | 1.25 | 2149 | [2031, 2260] | 1.52 |
| fib_min3 | 1.00 | [1.00, 1.00] | 0.98 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.01 | 1820 | [1795, 1869] | 2.51 |
| pow2 | 0.94 | [0.81, 1.00] | 0.62 | 0.94 | [0.81, 1.00] | 0.94 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.25 | 2151 | [2031, 2263] | 1.55 |
| pow2_min3 | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.92 | 0.00 | 0.00 | 1.00 | 1812 | [1806, 1818] | 2.73 |
| fixed5 | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.00 | 1836 | [1830, 1843] | 3.18 |
| fib_confirm | 0.94 | [0.81, 1.00] | 0.62 | 0.94 | [0.81, 1.00] | 0.94 | 1.00 | n/a | [n/a, n/a] | 0.66 | 0.00 | 0.00 | 1.39 | 2408 | [2246, 2545] | 2.03 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 0.94 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.00 | 1848 | [1836, 1861] | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.12 | 0.12 |
| fib | 0.88 | 1.00 |
| fib_min3 | 1.00 | 1.00 |
| pow2 | 0.88 | 1.00 |
| pow2_min3 | 1.00 | 1.00 |
| fixed5 | 1.00 | 1.00 |
| fib_confirm | 0.88 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.04 | 0.04 |
| fib | 0.58 | 0.67 |
| fib_min3 | 0.96 | 1.00 |
| pow2 | 0.58 | 0.67 |
| pow2_min3 | 0.92 | 0.96 |
| fixed5 | 1.00 | 1.00 |
| fib_confirm | 0.58 | 0.67 |
| full | 1.00 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0 |
| fib | 0.88 | 1 |
| fib_min3 | 1 | 1 |
| pow2 | 0.88 | 1 |
| pow2_min3 | 1 | 1 |
| fixed5 | 1 | 1 |
| fib_confirm | 0.88 | 1 |
| full | 1 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | -1.73 | [-4.14, 0.00] | no (CI contains 0) |
| fib vs fixed5 | recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib vs fixed5 | root_recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib vs fixed5 | tokens_per_output | 313 | [193, 428] | yes |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | tokens_per_output | 259 | [187, 318] | yes |
| fib vs full | recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib vs full | root_recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib vs full | tokens_per_output | 301 | [180, 420] | yes |
| fib_confirm vs full | recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib_confirm vs full | root_recall | -0.06 | [-0.19, 0.00] | no (CI contains 0) |
| fib_confirm vs full | tokens_per_output | 559 | [395, 704] | yes |
| fib_min3 vs fib | recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3 vs fib | root_recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3 vs fib | tokens_per_output | -329 | [-454, -211] | yes |
| pow2_min3 vs pow2 | recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| pow2_min3 vs pow2 | root_recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| pow2_min3 vs pow2 | tokens_per_output | -339 | [-451, -217] | yes |
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | tokens_per_output | -28.47 | [-59.53, 22.86] | no (CI contains 0) |
| fib_min3 vs fib_confirm | recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3 vs fib_confirm | root_recall | 0.06 | [0.00, 0.19] | no (CI contains 0) |
| fib_min3 vs fib_confirm | tokens_per_output | -588 | [-741, -427] | yes |