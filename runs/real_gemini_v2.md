| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gated_full | 0.88 | [0.71, 1.00] | 0.76 | 0.54 | [0.33, 0.75] | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 0.87 | 0.00 | 0.12 | 0.18 | 145 | [117, 177] | 1.38 |
| fib_gated | 0.88 | [0.71, 1.00] | 0.81 | 0.67 | [0.46, 0.88] | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 0.92 | 0.00 | 0.12 | 0.18 | 97.24 | [75.70, 124] | 0.18 |
| gated_full_stateful | 0.88 | [0.71, 1.00] | 0.76 | 0.54 | [0.33, 0.75] | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 0.87 | 0.00 | 0.12 | 0.18 | 145 | [117, 177] | 1.38 |
| fib_stateful | 0.88 | [0.71, 1.00] | 0.81 | 0.67 | [0.46, 0.88] | 0.88 | 1.00 | 0.00 | [0.00, 0.00] | 0.92 | 0.00 | 0.12 | 0.18 | 97.24 | [75.70, 124] | 0.18 |

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
| gated_full | 0.78 | 0.89 | 0.89 | 0.78 | 0.89 | 0.00 | 0.89 | 1.00 |
| fib_gated | 0.89 | 0.89 | 0.89 | 0.89 | 1.00 | 0.00 | 0.89 | 1.00 |
| gated_full_stateful | 0.78 | 0.89 | 0.89 | 0.78 | 0.89 | 0.00 | 0.89 | 1.00 |
| fib_stateful | 0.89 | 0.89 | 0.89 | 0.89 | 1.00 | 0.00 | 0.89 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | adjacent | spaced | fib_gaps | pow2_gaps | random_gaps | paraphrased | long_context | long_span |
|---|---|---|---|---|---|---|---|---|
| gated_full | 0.33 | 0.67 | 0.67 | 0.33 | 0.67 | 0 | 0.67 | 1 |
| fib_gated | 0.67 | 0.67 | 0.67 | 0.67 | 1 | 0 | 0.67 | 1 |
| gated_full_stateful | 0.33 | 0.67 | 0.67 | 0.33 | 0.67 | 0 | 0.67 | 1 |
| fib_stateful | 0.67 | 0.67 | 0.67 | 0.67 | 1 | 0 | 0.67 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | benign |
|---|---|
| gated_full | 0.00 |
| fib_gated | 0.00 |
| gated_full_stateful | 0.00 |
| fib_stateful | 0.00 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib_gated vs gated_full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_gated vs gated_full | root_recall | 0.12 | [-0.04, 0.29] | no (CI contains 0) |
| fib_gated vs gated_full | tokens_per_output | -47.63 | [-58.92, -36.06] | yes |
| fib_stateful vs fib_gated | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_stateful vs fib_gated | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_stateful vs fib_gated | tokens_per_output | 0.00 | [0.00, 0.00] | no (CI contains 0) |