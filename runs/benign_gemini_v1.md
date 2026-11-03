| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.67 | 0 | [0.00, 0.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 0.67 | 0.00 | 0.00 | 1.00 | 518 | [518, 518] | 1 |
| fixed5_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 0 | [0.00, 0.00] | 1.00 | 0.67 | 0.00 | [0.00, 0.00] | 0.67 | 0.00 | 0.00 | 1.00 | 652 | [646, 658] | 4.32 |
| pow2_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 623 | [619, 630] | 3.60 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.00 | 1.00 | 592 | [588, 598] | 2.81 |
| full | 1.00 | [1.00, 1.00] | 0.67 | 0 | [0.00, 0.00] | 1.00 | 0.67 | 0.00 | [0.00, 0.00] | 0.67 | 0.00 | 0.00 | 1.00 | 821 | [786, 852] | 8.80 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| full vs per_message | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 303 | [268, 334] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fixed5_fallback_confirm vs per_message | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 134 | [128, 140] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 74.19 | [70.78, 79.77] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs per_message | root_recall | 1.00 | [1.00, 1.00] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 105 | [101, 111] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -228 | [-260, -192] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 1.00 | [1.00, 1.00] | yes |
| pow2_min3_fallback_confirm vs full | tokens_per_output | -197 | [-228, -162] | yes |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | -31.22 | [-32.42, -29.73] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 1.00 | [1.00, 1.00] | yes |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -59.48 | [-61.88, -56.59] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 1.00 | [1.00, 1.00] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | -28.27 | [-29.60, -26.67] | yes |