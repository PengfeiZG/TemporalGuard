| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.94 | [0.86, 1.00] | 0.64 | 0.33 | [0.17, 0.47] | 0.53 | 0.82 | n/a | [n/a, n/a] | 0.65 | 0.00 | 0.00 | 1.00 | 1663 | [1643, 1684] | 0.00539 | 1 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 0.64 | 0.87 | n/a | [n/a, n/a] | 0.95 | 0.00400 | 0.00 | 1.00 | 2267 | [2145, 2360] | 0.00696 | 10.73 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.99 | 1 | [1.00, 1.00] | 0.64 | 0.84 | n/a | [n/a, n/a] | 0.94 | 0.00200 | 0.00 | 1.30 | 2458 | [2368, 2559] | 0.00795 | 5.53 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.92 | 0.92 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.44 | 0.47 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.97 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| full | 1 | 1 | 1 |
| fib_min3_fallback_confirm | 1 | 1 | 1 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| full vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| full vs per_message | tokens_per_output | 604 | [487, 700] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 795 | [698, 901] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 191 | [54.94, 372] | yes |