| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.12 | [0.00, 0.31] | 0.04 | 0 | [0.00, 0.00] | 0.12 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 1698 | [1695, 1701] | 0.00027 | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.00 | 1836 | [1830, 1843] | 0.00030 | 3.18 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.05 | 1929 | [1856, 2008] | 0.00031 | 3.45 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.12 | 2071 | [1942, 2203] | 0.00034 | 3.58 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.98 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.24 | 2265 | [2146, 2398] | 0.00037 | 3.57 |
| fib_min3 | 1.00 | [1.00, 1.00] | 0.98 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.96 | 0.00 | 0.00 | 1.01 | 1820 | [1795, 1869] | 0.00030 | 2.51 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 0.94 | n/a | [n/a, n/a] | 1.00 | 0.00 | 0.00 | 1.00 | 1848 | [1836, 1861] | 0.00030 | 3.35 |

recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.12 | 0.12 |
| fixed5 | 1.00 | 1.00 |
| fixed5_fallback_confirm | 1.00 | 1.00 |
| pow2_min3_fallback_confirm | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 |
| fib_min3 | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | definitional | referential |
|---|---|---|
| per_message | 0.04 | 0.04 |
| fixed5 | 1.00 | 1.00 |
| fixed5_fallback_confirm | 1.00 | 1.00 |
| pow2_min3_fallback_confirm | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 0.96 | 1.00 |
| fib_min3 | 0.96 | 1.00 |
| full | 1.00 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | definitional | referential |
|---|---|---|
| per_message | 0 | 0 |
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
| fib_min3 vs full | tokens_per_output | -28.47 | [-59.53, 22.86] | no (CI contains 0) |
| full vs per_message | recall | 0.88 | [0.69, 1.00] | yes |
| full vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| full vs per_message | tokens_per_output | 150 | [137, 164] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.88 | [0.69, 1.00] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 231 | [156, 313] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.88 | [0.69, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 567 | [450, 701] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.88 | [0.69, 1.00] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 374 | [243, 505] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 417 | [308, 539] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | 223 | [105, 343] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | 193 | [84.12, 288] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 336 | [231, 443] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 143 | [66.77, 210] | yes |