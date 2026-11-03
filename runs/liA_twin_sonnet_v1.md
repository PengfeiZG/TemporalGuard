| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.86 | [0.72, 0.97] | 0.60 | 0.33 | [0.17, 0.47] | 0.47 | 0.65 | 0.02 | [0.00820, 0.04] | 0.67 | 0.00 | 0.00 | 1.00 | 1654 | [1641, 1668] | 0.00534 | 1 |
| fib_min3_fallback_confirm | 1.00 | [1.00, 1.00] | 0.91 | 0.81 | [0.67, 0.92] | 0.58 | 0.66 | 0.03 | [0.01, 0.05] | 0.86 | 0.00 | 0.00 | 1.23 | 2286 | [2165, 2402] | 0.00739 | 4.79 |
| full | 1.00 | [1.00, 1.00] | 0.94 | 0.81 | [0.67, 0.92] | 0.58 | 0.69 | 0.03 | [0.01, 0.05] | 0.89 | 0.00100 | 0.00 | 1.00 | 2242 | [2163, 2306] | 0.00682 | 10.76 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.83 | 0.75 | 1.00 |
| fib_min3_fallback_confirm | 1.00 | 1.00 | 1.00 |
| full | 1.00 | 1.00 | 1.00 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.42 | 0.39 | 1.00 |
| fib_min3_fallback_confirm | 0.97 | 0.75 | 1.00 |
| full | 0.97 | 0.83 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 1 |
| fib_min3_fallback_confirm | 0.92 | 0.50 | 1 |
| full | 0.92 | 0.50 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.08 | 0.42 | 0.08 |
| fib_min3_fallback_confirm | 0.17 | 0.42 | 0.17 |
| full | 0.17 | 0.42 | 0.17 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.75 | 0.42 | 0.92 | 0.69 |
| fib_min3_fallback_confirm | 0.83 | 0.58 | 0.83 | 0.75 |
| full | 0.83 | 0.58 | 0.83 | 0.75 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| full vs per_message | root_recall | 0.47 | [0.33, 0.64] | yes |
| full vs per_message | tokens_per_output | 588 | [510, 652] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.14 | [0.03, 0.28] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.47 | [0.33, 0.64] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 632 | [518, 746] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 44.02 | [-74.40, 175] | no (CI contains 0) |