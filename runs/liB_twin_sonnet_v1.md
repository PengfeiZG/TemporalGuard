| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.94 | [0.86, 1.00] | 0.64 | 0.33 | [0.17, 0.47] | 0.53 | 0.64 | 0.03 | [0.01, 0.05] | 0.65 | 0.00 | 0.00 | 1.00 | 1659 | [1646, 1673] | 0.00536 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.99 | 1 | [1.00, 1.00] | 0.64 | 0.60 | 0.05 | [0.03, 0.08] | 0.94 | 0.00100 | 0.00 | 1.27 | 2387 | [2309, 2471] | 0.00772 | 5.16 |
| full | 1.00 | [1.00, 1.00] | 1.00 | 1 | [1.00, 1.00] | 0.64 | 0.60 | 0.06 | [0.04, 0.09] | 0.95 | 0.00200 | 0.00 | 1.00 | 2261 | [2179, 2328] | 0.00692 | 10.76 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.92 | 0.92 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.44 | 0.47 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 0.97 | 1.00 |
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
| per_message | 0.25 | 0.42 | 0.17 |
| fib_min3_fallback_confirm | 0.50 | 0.58 | 0.50 |
| full | 0.50 | 0.75 | 0.50 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.67 | 0.50 | 0.83 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.42 | 0.50 | 0.47 |
| full | 0.50 | 0.25 | 0.50 | 0.42 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| full vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| full vs per_message | tokens_per_output | 602 | [519, 671] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.67 | [0.53, 0.83] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 729 | [650, 811] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 127 | [16.91, 261] | yes |