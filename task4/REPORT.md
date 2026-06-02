# Fairness, Bias, and Explainability - Short Report

## What was checked

- Feature importance extracted from the trained pipeline.
- Local explanations using LIME on representative spam/ham samples.
- Group fairness checks using selection rate, TPR, and FPR when sensitive columns exist.

## Findings

- The model relies on a small set of high-weight tokens (see top-20 bar plot in the notebook).
- LIME highlights token-level drivers for individual predictions.
- If no sensitive attributes exist in the dataset, only overall error patterns can be inspected.

## Mitigation Recommendations

- Collect or annotate sensitive attributes (when permissible) to enable group-level fairness audits.
- Rebalance the dataset or add class weights to reduce skew.
- Tune decision thresholds to reduce TPR/FPR gaps between groups.
- Add data augmentation and review false positives/negatives for bias patterns.
- Re-evaluate fairness after retraining and monitor for drift.
