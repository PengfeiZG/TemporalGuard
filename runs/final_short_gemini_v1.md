| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.38 | [0.12, 0.62] | 0.17 | 0.12 | [0.00, 0.31] | 0.38 | 1.00 | n/a | [n/a, n/a] | 0.44 | 0.00 | 0.00 | 1.00 | 526 | [524, 528] | 1 |
| fixed5 | 0.88 | [0.69, 1.00] | 0.77 | 0.88 | [0.69, 1.00] | 0.88 | 0.83 | n/a | [n/a, n/a] | 0.71 | 0.00 | 0.00 | 1.00 | 624 | [618, 630] | 3.18 |
| fixed5_fallback_confirm | 0.88 | [0.69, 1.00] | 0.77 | 0.88 | [0.69, 1.00] | 0.88 | 0.83 | n/a | [n/a, n/a] | 0.74 | 0.00 | 0.00 | 1.06 | 668 | [628, 714] | 3.53 |
| pow2_min3_fallback_confirm | 0.88 | [0.69, 1.00] | 0.77 | 0.88 | [0.69, 1.00] | 0.88 | 0.93 | n/a | [n/a, n/a] | 0.74 | 0.00 | 0.00 | 1.09 | 678 | [628, 728] | 3.40 |
| fib_min3_fallback_confirm | 0.88 | [0.69, 1.00] | 0.67 | 0.88 | [0.69, 1.00] | 0.88 | 1.00 | n/a | [n/a, n/a] | 0.69 | 0.00 | 0.00 | 1.10 | 663 | [615, 716] | 2.95 |
| fib_min3 | 0.88 | [0.69, 1.00] | 0.67 | 0.88 | [0.69, 1.00] | 0.88 | 1.00 | n/a | [n/a, n/a] | 0.69 | 0.00 | 0.00 | 1.00 | 589 | [587, 592] | 2.45 |
| full | 0.88 | [0.69, 1.00] | 0.75 | 0.88 | [0.69, 1.00] | 0.88 | 0.83 | n/a | [n/a, n/a] | 0.74 | 0.00 | 0.00 | 1.00 | 631 | [622, 641] | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.25 | 0.50 |
| fixed5 | 0.75 | 1.00 |
| fixed5_fallback_confirm | 0.75 | 1.00 |
| pow2_min3_fallback_confirm | 0.75 | 1.00 |
| fib_min3_fallback_confirm | 0.75 | 1.00 |
| fib_min3 | 0.75 | 1.00 |
| full | 0.75 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.08 | 0.25 |
| fixed5 | 0.62 | 0.92 |
| fixed5_fallback_confirm | 0.62 | 0.92 |
| pow2_min3_fallback_confirm | 0.62 | 0.92 |
| fib_min3_fallback_confirm | 0.58 | 0.75 |
| fib_min3 | 0.58 | 0.75 |
| full | 0.58 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0.25 |
| fixed5 | 0.75 | 1 |
| fixed5_fallback_confirm | 0.75 | 1 |
| pow2_min3_fallback_confirm | 0.75 | 1 |
| fib_min3_fallback_confirm | 0.75 | 1 |
| fib_min3 | 0.75 | 1 |
| full | 0.75 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | tokens_per_output | -41.31 | [-50.24, -32.44] | yes |
| full vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 105 | [95.27, 114] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 142 | [102, 189] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 137 | [88.90, 191] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.50 | [0.25, 0.75] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 152 | [102, 202] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 32.00 | [-8.08, 78.73] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | 46.92 | [6.54, 88.76] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -14.92 | [-47.01, 13.10] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -5.19 | [-28.81, 19.64] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 9.73 | [-12.09, 33.72] | no (CI contains 0) |