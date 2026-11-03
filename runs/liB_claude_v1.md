| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.75, 0.97] | 0.55 | 0.33 | [0.17, 0.47] | 0.36 | 0.78 | n/a | [n/a, n/a] | 0.61 | 0.00 | 0.00 | 1.00 | 1756 | [1736, 1778] | 0.00028 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.95 | 1 | [1.00, 1.00] | 0.58 | 0.68 | n/a | [n/a, n/a] | 0.79 | 0.00 | 0.00 | 1.21 | 2387 | [2300, 2482] | 0.00038 | 4.88 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 0.61 | 0.57 | n/a | [n/a, n/a] | 0.84 | 0.00 | 0.00 | 1.00 | 2346 | [2231, 2438] | 0.00035 | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.75 | 0.83 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.31 | 0.33 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.86 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| fib_min3_fallback_confirm | 1 | 1 | 1 |
| full | 1 | 1 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| full vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| full vs per_message | tokens_per_output | 590 | [480, 682] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 632 | [551, 730] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 41.21 | [-94.80, 221] | no (CI contains 0) |