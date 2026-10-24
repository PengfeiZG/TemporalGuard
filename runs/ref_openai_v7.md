| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.62 | [0.38, 0.88] | 0.21 | 0.25 | [0.06, 0.50] | 0.62 | 1.00 | n/a | [n/a, n/a] | 0.33 | 0.00 | 0.00 | 1.00 | 748 | [748, 749] | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.38 | 0.12 | [0.00, 0.31] | 1.00 | 0.78 | n/a | [n/a, n/a] | 0.35 | 0.00 | 0.00 | 1.00 | 866 | [865, 868] | 4.64 |
| pow2 | 1.00 | [1.00, 1.00] | 0.42 | 0.25 | [0.06, 0.50] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.03 | 773 | [761, 787] | 1.08 |
| fib | 1.00 | [1.00, 1.00] | 0.42 | 0.25 | [0.06, 0.50] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.03 | 772 | [761, 785] | 1.07 |
| fixed5_fallback | 1.00 | [1.00, 1.00] | 0.42 | 0.25 | [0.06, 0.50] | 1.00 | 0.82 | n/a | [n/a, n/a] | 0.40 | 0.00 | 0.00 | 1.01 | 880 | [871, 890] | 4.83 |
| pow2_fallback | 1.00 | [1.00, 1.00] | 0.42 | 0.25 | [0.06, 0.50] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.03 | 773 | [761, 787] | 1.08 |
| fib_fallback | 1.00 | [1.00, 1.00] | 0.42 | 0.25 | [0.06, 0.50] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.42 | 0.00 | 0.00 | 1.03 | 772 | [761, 785] | 1.07 |
| fixed5_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.78 | n/a | [n/a, n/a] | 0.63 | 0.00 | 0.00 | 1.05 | 923 | [911, 937] | 5.34 |
| pow2_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.07 | 821 | [808, 836] | 1.62 |
| fib_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.07 | 821 | [808, 835] | 1.60 |
| pow2_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.07 | 821 | [808, 836] | 1.62 |
| fib_fallback_confirm | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 1.00 | n/a | [n/a, n/a] | 0.67 | 0.00 | 0.00 | 1.07 | 821 | [808, 835] | 1.60 |
| full | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.86 | n/a | [n/a, n/a] | 0.66 | 0.00 | 0.00 | 1.00 | 1179 | [1149, 1208] | 14.76 |

recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.62 |
| fixed5 | 1.00 |
| pow2 | 1.00 |
| fib | 1.00 |
| fixed5_fallback | 1.00 |
| pow2_fallback | 1.00 |
| fib_fallback | 1.00 |
| fixed5_confirm | 1.00 |
| pow2_confirm | 1.00 |
| fib_confirm | 1.00 |
| pow2_fallback_confirm | 1.00 |
| fib_fallback_confirm | 1.00 |
| full | 1.00 |

fragment recall by attack family
| strategy | referential_span |
|---|---|
| per_message | 0.21 |
| fixed5 | 0.38 |
| pow2 | 0.42 |
| fib | 0.42 |
| fixed5_fallback | 0.42 |
| pow2_fallback | 0.42 |
| fib_fallback | 0.42 |
| fixed5_confirm | 0.67 |
| pow2_confirm | 0.67 |
| fib_confirm | 0.67 |
| pow2_fallback_confirm | 0.67 |
| fib_fallback_confirm | 0.67 |
| full | 0.67 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential_span |
|---|---|
| per_message | 0.25 |
| fixed5 | 0.12 |
| pow2 | 0.25 |
| fib | 0.25 |
| fixed5_fallback | 0.25 |
| pow2_fallback | 0.25 |
| fib_fallback | 0.25 |
| fixed5_confirm | 1 |
| pow2_confirm | 1 |
| fib_confirm | 1 |
| pow2_fallback_confirm | 1 |
| fib_fallback_confirm | 1 |
| full | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | -0.36 | [-6.95, 5.77] | no (CI contains 0) |
| fib vs fixed5 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | root_recall | 0.12 | [0.00, 0.31] | no (CI contains 0) |
| fib vs fixed5 | tokens_per_output | -93.98 | [-105, -81.00] | yes |
| fib_fallback vs pow2_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs pow2_fallback | tokens_per_output | -0.36 | [-6.95, 5.77] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | root_recall | 0.00 | [-0.25, 0.25] | no (CI contains 0) |
| fib_fallback vs fixed5_fallback | tokens_per_output | -108 | [-124, -91.76] | yes |
| pow2_fallback vs fixed5_fallback | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | root_recall | 0.00 | [-0.25, 0.25] | no (CI contains 0) |
| pow2_fallback vs fixed5_fallback | tokens_per_output | -108 | [-123, -93.91] | yes |
| fib_confirm vs pow2_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs pow2_confirm | tokens_per_output | -0.36 | [-6.95, 5.77] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fixed5_confirm | tokens_per_output | -102 | [-119, -84.74] | yes |
| fib_fallback_confirm vs pow2_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs pow2_fallback_confirm | tokens_per_output | -0.36 | [-6.95, 5.77] | no (CI contains 0) |
| fib_fallback vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs fib | root_recall | 0.75 | [0.50, 0.94] | yes |
| fib_confirm vs fib | tokens_per_output | 48.43 | [43.99, 53.96] | yes |
| fib_fallback_confirm vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs fib | root_recall | 0.75 | [0.50, 0.94] | yes |
| fib_fallback_confirm vs fib | tokens_per_output | 48.43 | [43.99, 53.96] | yes |
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib vs full | tokens_per_output | -407 | [-437, -374] | yes |
| fib_fallback vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fib_fallback vs full | tokens_per_output | -407 | [-437, -374] | yes |
| fib_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_confirm vs full | tokens_per_output | -358 | [-387, -325] | yes |
| fib_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback_confirm vs full | tokens_per_output | -358 | [-387, -325] | yes |
| pow2_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_fallback_confirm vs full | tokens_per_output | -358 | [-387, -323] | yes |
| fixed5_fallback vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fixed5_fallback vs full | root_recall | -0.75 | [-0.94, -0.50] | yes |
| fixed5_fallback vs full | tokens_per_output | -299 | [-323, -271] | yes |