| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.38 | [0.12, 0.62] | 0.17 | 0.12 | [0.00, 0.31] | 0.38 | 1.00 | n/a | [n/a, n/a] | 0.44 | 0.00 | 0.00 | 1.00 | 526 | [524, 528] | 1 |
| fib | 0.38 | [0.12, 0.62] | 0.17 | 0.12 | [0.00, 0.31] | 0.38 | 1.00 | n/a | [n/a, n/a] | 0.44 | 0.00 | 0.00 | 1.00 | 526 | [524, 528] | 1 |
| fib_min3 | 0.88 | [0.69, 1.00] | 0.67 | 0.88 | [0.69, 1.00] | 0.88 | 1.00 | n/a | [n/a, n/a] | 0.69 | 0.00 | 0.00 | 1.00 | 589 | [587, 592] | 2.45 |
| pow2 | 0.38 | [0.12, 0.62] | 0.17 | 0.12 | [0.00, 0.31] | 0.38 | 1.00 | n/a | [n/a, n/a] | 0.44 | 0.00 | 0.00 | 1.00 | 526 | [524, 528] | 1 |
| pow2_min3 | 0.88 | [0.69, 1.00] | 0.73 | 0.88 | [0.69, 1.00] | 0.88 | 0.92 | n/a | [n/a, n/a] | 0.71 | 0.00 | 0.00 | 1.00 | 602 | [598, 607] | 2.73 |
| fixed5 | 0.88 | [0.69, 1.00] | 0.77 | 0.88 | [0.69, 1.00] | 0.88 | 0.83 | n/a | [n/a, n/a] | 0.71 | 0.00 | 0.00 | 1.00 | 624 | [618, 630] | 3.18 |
| fib_confirm | 0.38 | [0.12, 0.62] | 0.25 | 0.38 | [0.12, 0.62] | 0.38 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.08 | 578 | [543, 618] | 1.28 |
| full | 0.88 | [0.69, 1.00] | 0.75 | 0.88 | [0.69, 1.00] | 0.88 | 0.83 | n/a | [n/a, n/a] | 0.74 | 0.00 | 0.00 | 1.00 | 631 | [622, 641] | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.25 | 0.50 |
| fib | 0.25 | 0.50 |
| fib_min3 | 0.75 | 1.00 |
| pow2 | 0.25 | 0.50 |
| pow2_min3 | 0.75 | 1.00 |
| fixed5 | 0.75 | 1.00 |
| fib_confirm | 0.25 | 0.50 |
| full | 0.75 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.08 | 0.25 |
| fib | 0.08 | 0.25 |
| fib_min3 | 0.58 | 0.75 |
| pow2 | 0.08 | 0.25 |
| pow2_min3 | 0.58 | 0.88 |
| fixed5 | 0.62 | 0.92 |
| fib_confirm | 0.17 | 0.33 |
| full | 0.58 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0.25 |
| fib | 0 | 0.25 |
| fib_min3 | 0.75 | 1 |
| pow2 | 0 | 0.25 |
| pow2_min3 | 0.75 | 1 |
| fixed5 | 0.75 | 1 |
| fib_confirm | 0.25 | 0.50 |
| full | 0.75 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | recall | -0.50 | [-0.75, -0.25] | yes |
| fib vs fixed5 | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib vs fixed5 | tokens_per_output | -98.33 | [-104, -92.13] | yes |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.25 | [0.06, 0.50] | yes |
| fib_confirm vs fib | tokens_per_output | 52.50 | [17.01, 91.65] | yes |
| fib vs full | recall | -0.50 | [-0.75, -0.25] | yes |
| fib vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib vs full | tokens_per_output | -105 | [-114, -95.25] | yes |
| fib_confirm vs full | recall | -0.50 | [-0.75, -0.25] | yes |
| fib_confirm vs full | root_recall | -0.50 | [-0.75, -0.25] | yes |
| fib_confirm vs full | tokens_per_output | -52.44 | [-84.70, -16.08] | yes |
| fib_min3 vs fib | recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3 vs fib | root_recall | 0.75 | [0.50, 0.94] | yes |
| fib_min3 vs fib | tokens_per_output | 63.64 | [61.88, 65.38] | yes |
| pow2_min3 vs pow2 | recall | 0.50 | [0.25, 0.75] | yes |
| pow2_min3 vs pow2 | root_recall | 0.75 | [0.50, 0.94] | yes |
| pow2_min3 vs pow2 | tokens_per_output | 76.48 | [72.22, 80.48] | yes |
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | tokens_per_output | -41.31 | [-50.24, -32.44] | yes |
| fib_min3 vs fib_confirm | recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3 vs fib_confirm | root_recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3 vs fib_confirm | tokens_per_output | 11.14 | [-27.50, 46.61] | no (CI contains 0) |
| full vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 105 | [95.27, 114] | yes |