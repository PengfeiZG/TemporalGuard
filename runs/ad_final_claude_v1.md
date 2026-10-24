| strategy | recall | recall 95% CI | frag_rec | root_rec | root 95% CI | early | prec | fpr | fpr 95% CI | loc | err | gate_miss | calls/out | tok/out | tok/out 95% CI | ctx/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| per_message | 0.89 | [0.80, 0.96] | 0.56 | 0.39 | [0.26, 0.52] | 0.78 | 0.92 | n/a | [n/a, n/a] | 0.61 | 0.00 | 0.00 | 1.00 | 1748 | [1736, 1762] | 1 |
| fixed5_fallback_confirm | 0.98 | [0.94, 1.00] | 0.92 | 0.93 | [0.85, 0.98] | 0.93 | 0.74 | n/a | [n/a, n/a] | 0.78 | 0.00 | 0.00 | 1.14 | 2327 | [2260, 2400] | 6.55 |
| pow2_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.74 | n/a | [n/a, n/a] | 0.77 | 0.00 | 0.00 | 1.22 | 2449 | [2377, 2534] | 6.32 |
| fib_min3_fallback_confirm | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.76 | n/a | [n/a, n/a] | 0.76 | 0.00 | 0.00 | 1.27 | 2500 | [2424, 2587] | 5.76 |
| full | 0.98 | [0.94, 1.00] | 0.93 | 0.93 | [0.85, 0.98] | 0.93 | 0.76 | n/a | [n/a, n/a] | 0.84 | 0.00 | 0.00 | 1.00 | 2383 | [2305, 2456] | 12.32 |

recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.93 | 0.85 |
| fixed5_fallback_confirm | 1.00 | 0.96 |
| pow2_min3_fallback_confirm | 1.00 | 0.96 |
| fib_min3_fallback_confirm | 1.00 | 0.96 |
| full | 1.00 | 0.96 |

fragment recall by attack family
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.58 | 0.54 |
| fixed5_fallback_confirm | 1.00 | 0.84 |
| pow2_min3_fallback_confirm | 1.00 | 0.85 |
| fib_min3_fallback_confirm | 1.00 | 0.85 |
| full | 1.00 | 0.85 |

root-fragment recall by attack family (was the oldest fragment found?)
| strategy | agentdojo | agentdojo_span |
|---|---|---|
| per_message | 0.41 | 0.37 |
| fixed5_fallback_confirm | 1 | 0.85 |
| pow2_min3_fallback_confirm | 1 | 0.85 |
| fib_min3_fallback_confirm | 1 | 0.85 |
| full | 1 | 0.85 |

paired differences (same episodes)
| A vs B | metric | A - B | 95% CI | separable? |
|---|---|---|---|---|
| full vs per_message | recall | 0.09 | [0.02, 0.19] | yes |
| full vs per_message | root_recall | 0.54 | [0.41, 0.67] | yes |
| full vs per_message | tokens_per_output | 635 | [555, 706] | yes |
| fixed5_fallback_confirm vs per_message | recall | 0.09 | [0.02, 0.19] | yes |
| fixed5_fallback_confirm vs per_message | root_recall | 0.54 | [0.41, 0.67] | yes |
| fixed5_fallback_confirm vs per_message | tokens_per_output | 579 | [514, 645] | yes |
| fib_min3_fallback_confirm vs per_message | recall | 0.09 | [0.02, 0.19] | yes |
| fib_min3_fallback_confirm vs per_message | root_recall | 0.54 | [0.41, 0.67] | yes |
| fib_min3_fallback_confirm vs per_message | tokens_per_output | 752 | [682, 833] | yes |
| pow2_min3_fallback_confirm vs per_message | recall | 0.09 | [0.02, 0.19] | yes |
| pow2_min3_fallback_confirm vs per_message | root_recall | 0.54 | [0.41, 0.67] | yes |
| pow2_min3_fallback_confirm vs per_message | tokens_per_output | 701 | [633, 781] | yes |
| fib_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs full | tokens_per_output | 117 | [10.74, 245] | yes |
| pow2_min3_fallback_confirm vs full | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs full | tokens_per_output | 65.80 | [-25.97, 192] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs pow2_min3_fallback_confirm | tokens_per_output | 51.43 | [-8.95, 110] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| fib_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 173 | [105, 247] | yes |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | root_recall | 0.00 | [0.00, 0.00] | no (CI contains 0) |
| pow2_min3_fallback_confirm vs fixed5_fallback_confirm | tokens_per_output | 122 | [71.34, 179] | yes |