| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.03 | [0.00, 0.08] | 0.00926 | 0.03 | [0.00, 0.08] | 0.03 | 0.17 | 0.00610 | [0.00, 0.01] | 0.33 | 0.00 | 0.00 | 1.00 | 1654 | [1649, 1659] | 0.00536 | 1 |
| fib_min3_fallback_confirm | 0.06 | [0.00, 0.14] | 0.04 | 0.06 | [0.00, 0.14] | 0.06 | 0.33 | 0.00407 | [0.00, 0.01] | 0.67 | 0.00 | 0.00 | 1.06 | 1918 | [1874, 1968] | 0.00625 | 3.11 |
| full | 0.11 | [0.03, 0.22] | 0.07 | 0.11 | [0.03, 0.22] | 0.11 | 0.50 | 0.00407 | [0.00, 0.01] | 0.67 | 0.00 | 0.00 | 1.00 | 2364 | [2252, 2459] | 0.00718 | 10.72 |

recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.00 | 0.08 | 0.00 |
| fib_min3_fallback_confirm | 0.08 | 0.08 | 0.00 |
| full | 0.08 | 0.25 | 0.00 |

fragment recall by attack family
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0.00 | 0.03 | 0.00 |
| fib_min3_fallback_confirm | 0.06 | 0.06 | 0.00 |
| full | 0.06 | 0.17 | 0.00 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct4 | ct4_span | ct4_concat |
|---|---|---|---|
| per_message | 0 | 0.08 | 0 |
| fib_min3_fallback_confirm | 0.08 | 0.08 | 0 |
| full | 0.08 | 0.25 | 0 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct4_twin | ct4_span_twin | ct4_concat_twin |
|---|---|---|---|
| per_message | 0.00 | 0.25 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.17 | 0.00 |
| full | 0.00 | 0.17 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct4 | ct4_span | ct4_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.00 | 0.00 |
| fib_min3_fallback_confirm | 0.08 | 0.08 | 0.00 | 0.06 |
| full | 0.08 | 0.25 | 0.00 | 0.11 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.08 | [0.00, 0.19] | no (CI contains 0) |
| full vs per_message | root_recall | 0.08 | [0.00, 0.19] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 710 | [599, 804] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.03 | [0.00, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.03 | [0.00, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 265 | [222, 312] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.06 | [-0.14, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.06 | [-0.14, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -445 | [-561, -313] | yes |