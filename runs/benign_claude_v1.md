| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 1685 | [1684, 1686] | 1 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 1864 | [1857, 1873] | 4.31 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 0.67 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.01 | 1836 | [1822, 1859] | 3.61 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 0.67 | 0.00 | [0.00, 0.00] | 0.75 | 0.00 | 0.00 | 1.01 | 1801 | [1785, 1832] | 2.83 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 2084 | [2039, 2124] | 8.80 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -283 | [-333, -220] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -248 | [-294, -192] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -35.00 | [-39.44, -25.78] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -63.75 | [-76.78, -36.28] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -28.75 | [-37.52, -10.15] | yes |