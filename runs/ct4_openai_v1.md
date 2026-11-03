| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.56 | [0.39, 0.72] | 0.42 | 0.44 | [0.28, 0.61] | 0.25 | 0.43 | 0.04 | [0.02, 0.05] | 0.73 | 0.00 | 0.00 | 1.00 | 783 | [780, 785] | 0.00011 | 1 |
| fib_min3_fallback_confirm | 0.78 | [0.64, 0.92] | 0.69 | 0.78 | [0.64, 0.92] | 0.44 | 0.72 | 0.02 | [0.00746, 0.04] | 0.88 | 0.00 | 0.00 | 1.06 | 927 | [906, 948] | 0.00013 | 3.22 |
| full | 0.97 | [0.92, 1.00] | 0.78 | 0.94 | [0.86, 1.00] | 0.64 | 0.80 | 0.01 | [0.00343, 0.02] | 0.78 | 0.00 | 0.00 | 1.00 | 1203 | [1133, 1262] | 0.00015 | 10.72 |

recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.33 | 0.42 | 0.92 |
| fib_min3_fallback_confirm | 1.00 | 0.33 | 1.00 |
| full | 1.00 | 0.92 | 1.00 |

fragment recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.17 | 0.17 | 0.92 |
| fib_min3_fallback_confirm | 0.83 | 0.22 | 1.00 |
| full | 0.72 | 0.61 | 1.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.17 | 0.25 | 0.92 |
| fib_min3_fallback_confirm | 1 | 0.33 | 1 |
| full | 0.92 | 0.92 | 1 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct4_twin | ct4_span_twin | ct4_concat_twin |
|---|---|---|---|
| per_message | 0.17 | 0.83 | 0.00 |
| fib_min3_fallback_confirm | 0.17 | 0.42 | 0.00 |
| full | 0.08 | 0.33 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct4 | ct4_span | ct4_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.17 | 0.00 | 0.92 | 0.36 |
| fib_min3_fallback_confirm | 0.83 | 0.17 | 1.00 | 0.67 |
| full | 0.92 | 0.58 | 1.00 | 0.83 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.42 | [0.28, 0.58] | yes |
| full vs per_message | root_recall | 0.50 | [0.36, 0.67] | yes |
| full vs per_message | tokens_per_output | 420 | [352, 479] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.22 | [0.06, 0.42] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.33 | [0.17, 0.53] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 144 | [125, 164] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.19 | [-0.33, -0.08] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.17 | [-0.33, -0.03] | yes |
| fib_min3_fallback_confirm vs full | tokens_per_output | -276 | [-339, -199] | yes |