| strategy | recall | recall 95% CI | frag_rec | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gated_full | 0.88 | [0.71, 1.00] | 0.88 | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.12 | 0.18 | 176 | [141, 216] | 1.38 |
| fib_gated | 0.88 | [0.71, 1.00] | 0.88 | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.12 | 0.18 | 138 | [107, 175] | 0.18 |
| gated_full_stateful | 0.88 | [0.71, 1.00] | 0.88 | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.12 | 0.18 | 176 | [141, 216] | 1.38 |
| fib_stateful | 0.88 | [0.71, 1.00] | 0.88 | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 1.00 | 0.00 | 0.12 | 0.18 | 138 | [107, 175] | 0.18 |

recall by attack family
| strategy | adjacent | spaced | fib_gaps | pow2_gaps | random_gaps | paraphrased | long_context | long_span |
|---|---|---|---|---|---|---|---|---|
| gated_full | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| fib_gated | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| gated_full_stateful | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| fib_stateful | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | adjacent | spaced | fib_gaps | pow2_gaps | random_gaps | paraphrased | long_context | long_span |
|---|---|---|---|---|---|---|---|---|
| gated_full | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| fib_gated | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| gated_full_stateful | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| fib_stateful | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_gated vs gated_full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_gated vs gated_full | tokens_per_output | -38.01 | [-47.10, -28.89] | yes |
| fib_stateful vs fib_gated | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_stateful vs fib_gated | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |