| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.53 | [0.36, 0.69] | 0.34 | 0.22 | [0.08, 0.36] | 0.25 | 0.54 | 0.02 | [0.00205, 0.04] | 0.63 | 0.00 | 0.00 | 1.00 | 567 | [557, 577] | 1 |
| fib_min3_fallback_confirm | 0.72 | [0.58, 0.86] | 0.65 | 0.67 | [0.53, 0.81] | 0.33 | 0.55 | 0.02 | [0.00466, 0.04] | 0.79 | 0.00 | 0.00 | 1.06 | 715 | [691, 741] | 3.44 |
| full | 0.94 | [0.86, 1.00] | 0.90 | 0.92 | [0.81, 1.00] | 0.47 | 0.64 | 0.02 | [0.00375, 0.04] | 0.87 | 0.00 | 0.00 | 1.00 | 994 | [938, 1041] | 10.78 |

recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.42 | 0.50 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.83 | 0.83 |
| full | 0.92 | 1.00 | 0.92 |

fragment recall by attack family
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0.17 | 0.19 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.61 | 0.83 |
| full | 0.86 | 0.92 | 0.92 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | li | li_span | li_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.67 |
| fib_min3_fallback_confirm | 0.50 | 0.67 | 0.83 |
| full | 0.92 | 0.92 | 0.92 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | li_twin | li_span_twin | li_concat_twin |
|---|---|---|---|
| per_message | 0.08 | 0.25 | 0.00 |
| fib_min3_fallback_confirm | 0.08 | 0.42 | 0.00 |
| full | 0.17 | 0.25 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | li | li_span | li_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.33 | 0.33 | 0.67 | 0.44 |
| fib_min3_fallback_confirm | 0.42 | 0.50 | 0.83 | 0.58 |
| full | 0.75 | 0.75 | 0.92 | 0.81 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.42 | [0.25, 0.58] | yes |
| full vs per_message | root_recall | 0.69 | [0.56, 0.86] | yes |
| full vs per_message | tokens_per_output | 427 | [371, 474] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.19 | [0.03, 0.39] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.44 | [0.28, 0.61] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 148 | [127, 172] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.22 | [-0.36, -0.11] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.25 | [-0.39, -0.11] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -279 | [-328, -219] | yes |