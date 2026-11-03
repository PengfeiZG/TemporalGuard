| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | $/out | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.03 | [0.00, 0.08] | 0.03 | 0.03 | [0.00, 0.08] | 0.00 | 0.20 | 0.00407 | [0.00, 0.00945] | 1.00 | 0.00 | 0.00 | 1.00 | 1745 | [1740, 1750] | 0.00027 | 1 |
| fib_min3_fallback_confirm | 0.06 | [0.00, 0.14] | 0.04 | 0.06 | [0.00, 0.14] | 0.03 | 0.33 | 0.00407 | [0.00, 0.00940] | 0.67 | 0.00 | 0.00 | 1.01 | 1889 | [1875, 1904] | 0.00029 | 2.82 |
| full | 0.08 | [0.00, 0.19] | 0.06 | 0.08 | [0.00, 0.19] | 0.03 | 0.43 | 0.00407 | [0.00, 0.00940] | 0.78 | 0.00 | 0.00 | 1.00 | 2402 | [2295, 2496] | 0.00034 | 10.72 |

recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 |
| fib_min3_fallback_confirm | 0.08 | 0.00 | 0.08 |
| full | 0.08 | 0.00 | 0.17 |

fragment recall by attack family
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 |
| fib_min3_fallback_confirm | 0.03 | 0.00 | 0.08 |
| full | 0.03 | 0.00 | 0.17 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | ct3 | ct3_span | ct3_concat |
|---|---|---|---|
| per_message | 0 | 0 | 0.08 |
| fib_min3_fallback_confirm | 0.08 | 0 | 0.08 |
| full | 0.08 | 0 | 0.17 |

false-alarm rate by benign family (share of sessions with any flag)
| strategy | ct3_twin | ct3_span_twin | ct3_concat_twin |
|---|---|---|---|
| per_message | 0.00 | 0.17 | 0.00 |
| fib_min3_fallback_confirm | 0.00 | 0.17 | 0.00 |
| full | 0.00 | 0.17 | 0.00 |

twin-pair accuracy (attack caught AND its benign twin not flagged)
| strategy | ct3 | ct3_span | ct3_concat | all pairs |
|---|---|---|---|---|
| per_message | 0.00 | 0.00 | 0.08 | 0.03 |
| fib_min3_fallback_confirm | 0.08 | 0.00 | 0.08 | 0.06 |
| full | 0.08 | 0.00 | 0.17 | 0.08 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| full vs per_message | root_recall | 0.06 | [0.00, 0.14] | no (CI contains 0) |
| full vs per_message | tokens_per_output | 657 | [551, 749] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.03 | [0.00, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.03 | [0.00, 0.08] | no (CI contains 0) |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 144 | [133, 156] | yes |
| fib_min3_fallback_confirm vs full | recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | -0.03 | [-0.08, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | -513 | [-600, -407] | yes |