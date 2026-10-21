| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | [1.00, 1.00] | 0.94 | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 0.94 | 0.00 | 0.00 | 1.00 | 1698 | [1694, 1703] | 1 |
| fib | 1.00 | [1.00, 1.00] | 0.92 | 1.00 | 1.00 | 0.00 | [0.00, 0.00] | 0.90 | 0.00 | 0.00 | 1.15 | 1984 | [1883, 2104] | 1.46 |
| full | 1.00 | [1.00, 1.00] | 0.99 | 1.00 | 0.78 | 0.00 | [0.00, 0.00] | 0.93 | 0.00 | 0.00 | 1.00 | 2108 | [2028, 2179] | 8.80 |
| gated_full | 0.88 | [0.71, 1.00] | 0.86 | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 0.98 | 0.00 | 0.12 | 0.18 | 374 | [299, 462] | 1.38 |

recall by attack family
| strategy | adjacent | spaced | fib_gaps | pow2_gaps | random_gaps | paraphrased | long_context | long_span |
|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| fib | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| gated_full | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | adjacent | spaced | fib_gaps | pow2_gaps | random_gaps | paraphrased | long_context | long_span |
|---|---|---|---|---|---|---|---|---|
| per_message | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.56 | 1.00 | 1.00 |
| fib | 0.89 | 1.00 | 1.00 | 0.89 | 0.89 | 0.78 | 0.89 | 1.00 |
| full | 1.00 | 1.00 | 1.00 | 1.00 | 0.89 | 1.00 | 1.00 | 1.00 |
| gated_full | 1.00 | 1.00 | 1.00 | 1.00 | 0.89 | 0.00 | 1.00 | 1.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | tokens_per_output | -124 | [-266, 43.20] | no (CI contains 0) |