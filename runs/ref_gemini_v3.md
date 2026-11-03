| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 522 | [521, 522] | 1 |
| fixed5 | 0.88 | [0.69, 1.00] | 0.38 | 0.25 | [0.06, 0.50] | 0.88 | 0.95 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.00 | 669 | [667, 671] | 4.64 |
| pow2 | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 523 | [521, 526] | 1.00 |
| fib | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 523 | [521, 526] | 1.00 |
| fixed5_fallback | 0.88 | [0.69, 1.00] | 0.38 | 0.25 | [0.06, 0.50] | 0.88 | 0.95 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.00 | 669 | [667, 671] | 4.64 |
| pow2_fallback | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 523 | [521, 526] | 1.00 |
| fib_fallback | 0.69 | [0.44, 0.88] | 0.31 | 0.25 | [0.06, 0.50] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.45 | 0.00 | 0.00 | 1.00 | 523 | [521, 526] | 1.00 |
| fixed5_confirm | 0.88 | [0.69, 1.00] | 0.58 | 0.88 | [0.69, 1.00] | 0.88 | 0.95 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.03 | 707 | [698, 715] | 5.15 |
| pow2_confirm | 0.69 | [0.44, 0.88] | 0.46 | 0.69 | [0.44, 0.88] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.03 | 554 | [543, 565] | 1.38 |
| fib_confirm | 0.69 | [0.44, 0.88] | 0.46 | 0.69 | [0.44, 0.88] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.03 | 554 | [543, 565] | 1.38 |
| pow2_fallback_confirm | 0.69 | [0.44, 0.88] | 0.46 | 0.69 | [0.44, 0.88] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.03 | 554 | [543, 565] | 1.38 |
| fib_fallback_confirm | 0.69 | [0.44, 0.88] | 0.46 | 0.69 | [0.44, 0.88] | 0.69 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.03 | 554 | [543, 565] | 1.38 |
| full | 1.00 | [1.00, 1.00] | 0.73 | 1 | [1.00, 1.00] | 1.00 | 0.68 | n/a | [n/a, n/a] | 0.73 | 0.00 | 0.00 | 1.00 | 1059 | [1021, 1094] | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.69 |
| fixed5 | 0.88 |
| pow2 | 0.69 |
| fib | 0.69 |
| fixed5_fallback | 0.88 |
| pow2_fallback | 0.69 |
| fib_fallback | 0.69 |
| fixed5_confirm | 0.88 |
| pow2_confirm | 0.69 |
| fib_confirm | 0.69 |
| pow2_fallback_confirm | 0.69 |
| fib_fallback_confirm | 0.69 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.31 |
| fixed5 | 0.38 |
| pow2 | 0.31 |
| fib | 0.31 |
| fixed5_fallback | 0.38 |
| pow2_fallback | 0.31 |
| fib_fallback | 0.31 |
| fixed5_confirm | 0.58 |
| pow2_confirm | 0.46 |
| fib_confirm | 0.46 |
| pow2_fallback_confirm | 0.46 |
| fib_fallback_confirm | 0.46 |
| full | 0.73 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.25 |
| pow2 | 0.25 |
| fib | 0.25 |
| fixed5_fallback | 0.25 |
| pow2_fallback | 0.25 |
| fib_fallback | 0.25 |
| fixed5_confirm | 0.88 |
| pow2_confirm | 0.69 |
| fib_confirm | 0.69 |
| pow2_fallback_confirm | 0.69 |
| fib_fallback_confirm | 0.69 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib vs fixed5 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | tokens_per_output | -146 | [-149, -142] | yes |
| fib_fallback vs pow2_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | tokens_per_output | -146 | [-149, -142] | yes |
| pow2_fallback vs fixed5_fallback | recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | tokens_per_output | -146 | [-149, -142] | yes |
| fib_confirm vs pow2_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | root_recall | -0.19 | [-0.38, 0.00] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | tokens_per_output | -152 | [-164, -142] | yes |
| fib_fallback_confirm vs pow2_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.44 | [0.19, 0.69] | yes |
| fib_confirm vs fib | tokens_per_output | 31.17 | [19.89, 42.69] | yes |
| fib_fallback_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs fib | root_recall | 0.44 | [0.19, 0.69] | yes |
| fib_fallback_confirm vs fib | tokens_per_output | 31.17 | [19.89, 42.69] | yes |
| fib vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib vs full | tokens_per_output | -535 | [-571, -497] | yes |
| fib_fallback vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib_fallback vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib_fallback vs full | tokens_per_output | -535 | [-571, -497] | yes |
| fib_confirm vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib_confirm vs full | root_recall | -0.31 | [-0.56, -0.12] | yes |
| fib_confirm vs full | tokens_per_output | -504 | [-537, -466] | yes |
| fib_fallback_confirm vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| fib_fallback_confirm vs full | root_recall | -0.31 | [-0.56, -0.12] | yes |
| fib_fallback_confirm vs full | tokens_per_output | -504 | [-537, -466] | yes |
| pow2_fallback_confirm vs full | recall | -0.31 | [-0.56, -0.12] | yes |
| pow2_fallback_confirm vs full | root_recall | -0.31 | [-0.56, -0.12] | yes |
| pow2_fallback_confirm vs full | tokens_per_output | -504 | [-537, -466] | yes |
| fixed5_fallback vs full | recall | -0.12 | [-0.31, 0.00] | no (CI contains 0) |
| fixed5_fallback vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fixed5_fallback vs full | tokens_per_output | -389 | [-423, -353] | yes |
| full vs per_message | recall | 0.31 | [0.12, 0.56] | yes |
| full vs per_message | root_recall | 0.75 | [0.50, 0.94] | yes |
| full vs per_message | tokens_per_output | 537 | [500, 572] | yes |