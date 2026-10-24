| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 750 | [749, 750] | 1 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 856 | [852, 860] | 4.31 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 835 | [831, 842] | 3.60 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 811 | [807, 818] | 2.81 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 994 | [966, 1018] | 8.80 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -183 | [-209, -152] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -158 | [-184, -128] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -24.58 | [-25.32, -23.66] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -45.21 | [-48.17, -40.04] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -20.63 | [-23.08, -16.11] | yes |