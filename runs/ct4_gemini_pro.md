| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.03 | [0.00, 0.08] | 0.03 | 0.03 | [0.00, 0.08] | 0.00 | 0.20 | 0.00407 | [0.00, 0.01] | 1.00 | 0.00 | 0.00 | 1.00 | 726 | [719, 732] | 1 |
| fib_min3_fallback_confirm | 0.00 | [0.00, 0.00] | 0.00 | 0 | [0.00, 0.00] | 0.00 | 0.00 | 0.00203 | [0.00, 0.00683] | n/a | 0.00 | 0.00 | 1.00 | 891 | [878, 903] | 2.80 |
| full | 0.11 | [0.03, 0.22] | 0.08 | 0.08 | [0.00, 0.19] | 0.08 | 0.71 | 0.00203 | [0.00, 0.00683] | 0.75 | 0.00 | 0.00 | 1.00 | 1318 | [1236, 1392] | 10.72 |

recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 |
| fib_min3_fallback_confirm | 0.00 | 0.00 | 0.00 |
| full | 0.08 | 0.17 | 0.08 |

fragment recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 |
| fib_min3_fallback_confirm | 0.00 | 0.00 | 0.00 |
| full | 0.06 | 0.11 | 0.08 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.08 |
| fib_min3_fallback_confirm | 0 | 0 | 0 |
| full | 0.08 | 0.08 | 0.08 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct4_twin | ct4_span_twin | ct4_concat_twin |
|---|---|---|---|
| per_message | 0.00 | 0.17 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.08 | 0.00 |
| full | 0.00 | 0.08 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct4 | ct4_span | ct4_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 | 0.03 |
| fib_min3_fallback_confirm | 0.00 | 0.00 | 0.00 | 0.00 |
| full | 0.08 | 0.17 | 0.08 | 0.11 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.08 | [0.00, 0.19] | no (CI contains 0) |
| full vs per_message | root_recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 592 | [508, 664] | yes |
| fib_min3_fallback_confirm vs per_message | recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 165 | [158, 172] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.11 | [-0.22, -0.03] | yes |
| fib_min3_fallback_confirm vs full | root_recall | -0.08 | [-0.19, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -427 | [-495, -346] | yes |