| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.25 | [0.00, 0.62] | 0.08 | 0 | [0.00, 0.00] | 0.25 | 0.50 | 0.01 | [0.00, 0.03] | 0.33 | 0.00 | 0.00 | 1.00 | 1690 | [1688, 1692] | 1 |
| fixed5 | 1.00 | [1.00, 1.00] | 0.67 | 0.50 | [0.12, 0.88] | 1.00 | 0.63 | 0.04 | [0.02, 0.06] | 0.67 | 0.00 | 0.00 | 1.00 | 1874 | [1863, 1881] | 4.38 |
| pow2 | 0.75 | [0.50, 1.00] | 0.46 | 0.62 | [0.25, 1.00] | 0.75 | 0.55 | 0.03 | [0.01, 0.05] | 0.61 | 0.00 | 0.00 | 1.13 | 1939 | [1881, 1996] | 1.55 |
| fib | 1.00 | [1.00, 1.00] | 0.62 | 0.88 | [0.62, 1.00] | 1.00 | 0.53 | 0.04 | [0.02, 0.06] | 0.62 | 0.00 | 0.00 | 1.18 | 2052 | [1973, 2126] | 1.91 |
| fib_fallback | 1.00 | [1.00, 1.00] | 0.67 | 1 | [1.00, 1.00] | 1.00 | 0.53 | 0.04 | [0.02, 0.06] | 0.67 | 0.00 | 0.00 | 1.20 | 2090 | [2003, 2167] | 2.12 |
| full | 1.00 | [1.00, 1.00] | 0.88 | 1 | [1.00, 1.00] | 1.00 | 0.43 | 0.05 | [0.02, 0.08] | 0.85 | 0.00 | 0.00 | 1.00 | 2269 | [2148, 2348] | 12.06 |

recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.25 | 0.25 |
| fixed5 | 1.00 | 1.00 |
| pow2 | 1.00 | 0.50 |
| fib | 1.00 | 1.00 |
| fib_fallback | 1.00 | 1.00 |
| full | 1.00 | 1.00 |

fragment recall by attack family
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0.08 | 0.08 |
| fixed5 | 1.00 | 0.33 |
| pow2 | 0.67 | 0.25 |
| fib | 0.67 | 0.58 |
| fib_fallback | 0.67 | 0.67 |
| full | 1.00 | 0.75 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | referential | referential_span |
|---|---|---|
| per_message | 0 | 0 |
| fixed5 | 1 | 0 |
| pow2 | 1 | 0.25 |
| fib | 1 | 0.75 |
| fib_fallback | 1 | 1 |
| full | 1 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | referential_twin | referential_span_twin | benign |
|---|---|---|---|
| per_message | 0.25 | 0.25 | 0.00 |
| fixed5 | 0.75 | 1.00 | 0.00 |
| pow2 | 0.75 | 0.50 | 0.00 |
| fib | 0.75 | 1.00 | 0.00 |
| fib_fallback | 0.75 | 1.00 | 0.00 |
| full | 0.75 | 1.00 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | referential | referential_span | all pairs |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 |
| fixed5 | 0.25 | 0.00 | 0.12 |
| pow2 | 0.25 | 0.00 | 0.12 |
| fib | 0.25 | 0.00 | 0.12 |
| fib_fallback | 0.25 | 0.00 | 0.12 |
| full | 0.25 | 0.00 | 0.12 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| fib vs pow2 | recall | 0.25 | [0.00, 0.62] | no (CI contains 0) |
| fib vs pow2 | root_recall | 0.25 | [-0.25, 0.62] | no (CI contains 0) |
| fib vs pow2 | tokens_per_output | 114 | [74.71, 145] | yes |
| fib vs fixed5 | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs fixed5 | root_recall | 0.38 | [0.00, 0.75] | no (CI contains 0) |
| fib vs fixed5 | tokens_per_output | 178 | [103, 253] | yes |
| fib vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib vs full | root_recall | -0.12 | [-0.38, 0.00] | no (CI contains 0) |
| fib vs full | tokens_per_output | -216 | [-295, -91.84] | yes |
| fib_fallback vs fib | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_fallback vs fib | root_recall | 0.12 | [0.00, 0.38] | no (CI contains 0) |
| fib_fallback vs fib | tokens_per_output | 37.23 | [13.86, 61.14] | yes |