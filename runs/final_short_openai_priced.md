| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.50 | [0.25, 0.75] | 0.17 | 0.12 | [0.00, 0.31] | 0.50 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 753 | [751, 754] | 0.00011 | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.96 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.00 | 833 | [828, 837] | 0.00012 | 3.18 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 0.96 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.03 | 865 | [831, 898] | 0.00013 | 3.39 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 1.00 | 0.94 | n/a | [n/a, n/a] | 0.94 | 0.00 | 0.00 | 1.12 | 937 | [887, 988] | 0.00014 | 3.56 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.94 | 0.00 | 0.00 | 1.20 | 991 | [946, 1035] | 0.00015 | 3.40 |
| fib_min3 | 1.00 | [1.00, 1.00] | 0.94 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.94 | 0.00 | 0.00 | 1.00 | 807 | [805, 809] | 0.00012 | 2.45 |
| full | 1.00 | [1.00, 1.00] | 0.98 | 1 | [1.00, 1.00] | 1.00 | 0.97 | n/a | [n/a, n/a] | 0.98 | 0.00 | 0.00 | 1.00 | 839 | [831, 846] | 0.00012 | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.25 | 0.75 |
| fixed5 | 1.00 | 1.00 |
| fixed5_fallback_confirm | 1.00 | 1.00 |
| pow2_min3_fallback_confirm | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| fib_min3 | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.08 | 0.25 |
| fixed5 | 0.92 | 1.00 |
| fixed5_fallback_confirm | 0.92 | 1.00 |
| pow2_min3_fallback_confirm | 0.88 | 1.00 |
| fib_min3_fallback_confirm | 0.88 | 1.00 |
| fib_min3 | 0.88 | 1.00 |
| full | 0.96 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0.25 |
| fixed5 | 1 | 1 |
| fixed5_fallback_confirm | 1 | 1 |
| pow2_min3_fallback_confirm | 1 | 1 |
| fib_min3_fallback_confirm | 1 | 1 |
| fib_min3 | 1 | 1 |
| full | 1 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3 vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3 vs full | tokens_per_output | -31.62 | [-39.09, -24.59] | yes |
| full vs per_message | recall | 0.50 | [0.31, 0.75] | yes |
| full vs per_message | root_recall | 0.88 | [0.69, 1.00] | yes |
| full vs per_message | tokens_per_output | 85.94 | [78.57, 92.96] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.50 | [0.31, 0.75] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 0.88 | [0.69, 1.00] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 112 | [78.57, 144] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.50 | [0.31, 0.75] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.88 | [0.69, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 238 | [195, 281] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.50 | [0.31, 0.75] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.88 | [0.69, 1.00] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 184 | [136, 235] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 152 | [111, 192] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | 98.16 | [53.48, 144] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | 53.89 | [12.49, 94.93] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 126 | [78.08, 173] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 72.12 | [38.03, 107] | yes |