| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.25 | [0.06, 0.50] | 0.08 | 0 | [0.00, 0.00] | 0.25 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1689 | [1688, 1691] | 1 |
| fixed5 | 0.62 | [0.38, 0.88] | 0.23 | 0 | [0.00, 0.00] | 0.62 | 0.91 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1884 | [1881, 1886] | 4.64 |
| pow2 | 0.94 | [0.81, 1.00] | 0.46 | 0.44 | [0.19, 0.69] | 0.94 | 1.00 | n/a | [n/a, n/a] | 0.48 | 0.00 | 0.00 | 1.15 | 1981 | [1961, 1998] | 1.80 |
| fib | 0.75 | [0.50, 0.94] | 0.31 | 0.19 | [0.06, 0.38] | 0.75 | 1.00 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.20 | 2080 | [2061, 2099] | 2.03 |
| fixed5_fallback | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.04 | 1992 | [1973, 2014] | 5.29 |
| pow2_fallback | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.17 | 2040 | [2021, 2061] | 2.07 |
| fib_fallback | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.23 | 2151 | [2132, 2172] | 2.46 |
| fixed5_confirm | 0.62 | [0.38, 0.88] | 0.44 | 0.62 | [0.38, 0.88] | 0.62 | 0.91 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.02 | 1943 | [1924, 1961] | 5.00 |
| pow2_confirm | 0.94 | [0.81, 1.00] | 0.62 | 0.94 | [0.81, 1.00] | 0.94 | 1.00 | n/a | [n/a, n/a] | 0.66 | 0.00 | 0.00 | 1.18 | 2056 | [2029, 2081] | 2.22 |
| fib_confirm | 0.75 | [0.50, 0.94] | 0.50 | 0.75 | [0.50, 0.94] | 0.75 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.22 | 2139 | [2116, 2164] | 2.37 |
| pow2_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.19 | 2069 | [2046, 2092] | 2.26 |
| fib_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.23 | 2161 | [2141, 2183] | 2.52 |
| full | 1.00 | [1.00, 1.00] | 0.71 | 1 | [1.00, 1.00] | 1.00 | 0.32 | n/a | [n/a, n/a] | 0.62 | 0.00 | 0.00 | 1.00 | 2406 | [2356, 2452] | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.62 |
| pow2 | 0.94 |
| fib | 0.75 |
| fixed5_fallback | 1.00 |
| pow2_fallback | 1.00 |
| fib_fallback | 1.00 |
| fixed5_confirm | 0.62 |
| pow2_confirm | 0.94 |
| fib_confirm | 0.75 |
| pow2_fallback_confirm | 1.00 |
| fib_fallback_confirm | 1.00 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.08 |
| fixed5 | 0.23 |
| pow2 | 0.46 |
| fib | 0.31 |
| fixed5_fallback | 0.67 |
| pow2_fallback | 0.67 |
| fib_fallback | 0.67 |
| fixed5_confirm | 0.44 |
| pow2_confirm | 0.62 |
| fib_confirm | 0.50 |
| pow2_fallback_confirm | 0.67 |
| fib_fallback_confirm | 0.67 |
| full | 0.71 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0 |
| fixed5 | 0 |
| pow2 | 0.44 |
| fib | 0.19 |
| fixed5_fallback | 1 |
| pow2_fallback | 1 |
| fib_fallback | 1 |
| fixed5_confirm | 0.62 |
| pow2_confirm | 0.94 |
| fib_confirm | 0.75 |
| pow2_fallback_confirm | 1 |
| fib_fallback_confirm | 1 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | -0.19 | [-0.44, 0.06] | no (CI contains 0) |
| fib vs pow2 | root_recall | -0.25 | [-0.62, 0.12] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 98.73 | [79.61, 117] | yes |
| fib vs fixed5 | recall | 0.12 | [-0.19, 0.44] | no (CI contains 0) |
| fib vs fixed5 | root_recall | 0.19 | [0.06, 0.38] | yes |
| fib vs fixed5 | tokens_per_output | 196 | [176, 216] | yes |
| fib_fallback vs pow2_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | tokens_per_output | 111 | [95.25, 124] | yes |
| fib_fallback vs fixed5_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | tokens_per_output | 159 | [127, 190] | yes |
| pow2_fallback vs fixed5_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | tokens_per_output | 48.02 | [19.80, 76.35] | yes |
| fib_confirm vs pow2_confirm | recall | -0.19 | [-0.44, 0.06] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | root_recall | -0.19 | [-0.44, 0.06] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | tokens_per_output | 83.17 | [53.49, 110] | yes |
| fib_confirm vs fixed5_confirm | recall | 0.12 | [-0.19, 0.44] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | root_recall | 0.12 | [-0.19, 0.44] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | tokens_per_output | 195 | [166, 223] | yes |
| fib_fallback_confirm vs pow2_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | tokens_per_output | 92.52 | [74.43, 113] | yes |
| fib_fallback vs fib | recall | 0.25 | [0.06, 0.50] | yes |
| fib_fallback vs fib | root_recall | 0.81 | [0.62, 0.94] | yes |
| fib_fallback vs fib | tokens_per_output | 71.12 | [54.03, 84.65] | yes |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.56 | [0.31, 0.81] | yes |
| fib_confirm vs fib | tokens_per_output | 59.08 | [36.83, 78.82] | yes |
| fib_fallback_confirm vs fib | recall | 0.25 | [0.06, 0.50] | yes |
| fib_fallback_confirm vs fib | root_recall | 0.81 | [0.62, 0.94] | yes |
| fib_fallback_confirm vs fib | tokens_per_output | 81.83 | [70.73, 90.14] | yes |
| fib vs full | recall | -0.25 | [-0.50, -0.06] | yes |
| fib vs full | root_recall | -0.81 | [-0.94, -0.62] | yes |
| fib vs full | tokens_per_output | -327 | [-373, -278] | yes |
| fib_fallback vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs full | tokens_per_output | -255 | [-302, -206] | yes |
| fib_confirm vs full | recall | -0.25 | [-0.50, -0.06] | yes |
| fib_confirm vs full | root_recall | -0.25 | [-0.50, -0.06] | yes |
| fib_confirm vs full | tokens_per_output | -268 | [-329, -207] | yes |
| fib_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs full | tokens_per_output | -245 | [-294, -191] | yes |
| pow2_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback_confirm vs full | tokens_per_output | -337 | [-384, -287] | yes |
| fixed5_fallback vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fixed5_fallback vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fixed5_fallback vs full | tokens_per_output | -414 | [-474, -352] | yes |