| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.75, 0.97] | 0.55 | 0.33 | [0.17, 0.47] | 0.36 | 0.61 | 0.02 | [0.00735, 0.05] | 0.61 | 0.00 | 0.00 | 1.00 | 1753 | [1740, 1769] | 0.00027 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.95 | 1 | [1.00, 1.00] | 0.58 | 0.51 | 0.05 | [0.03, 0.07] | 0.79 | 0.00 | 0.00 | 1.16 | 2250 | [2182, 2319] | 0.00035 | 4.28 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 0.61 | 0.41 | 0.08 | [0.05, 0.10] | 0.84 | 0.00 | 0.00 | 1.00 | 2339 | [2262, 2405] | 0.00035 | 10.78 |

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

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.08 | 0.33 | 0.17 |
| fib_min3_fallback_confirm | 0.58 | 0.58 | 0.33 |
| full | 0.75 | 0.83 | 0.33 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.67 | 0.50 | 0.83 | 0.67 |
| fib_min3_fallback_confirm | 0.42 | 0.42 | 0.67 | 0.50 |
| full | 0.25 | 0.17 | 0.67 | 0.36 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| full vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| full vs per_message | tokens_per_output | 586 | [508, 649] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.25] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 497 | [433, 567] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -89.21 | [-188, 34.05] | no (CI contains 0) |