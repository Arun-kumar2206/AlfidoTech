# Email Spam Detection - Short Report

## Goal

Build and evaluate supervised classifiers for SMS spam detection, compare at least two algorithms, and report accuracy, precision, recall, F1, and ROC-AUC.

## Data and Preprocessing

- Dataset: SMS spam messages from data.csv.
- Cleaning: Renamed columns, dropped unused columns, created binary target Spam (1 = spam, 0 = ham).
- Features: TF-IDF vectors with English stop words.
- Split: Stratified train/test split (75/25) with fixed random seed.

## Models Compared

- Logistic Regression (TF-IDF + LogisticRegression)
- Random Forest (TF-IDF + RandomForestClassifier)

## Evaluation

- 5-fold stratified cross-validation on full dataset.
- Holdout evaluation on the test split.
- Metrics: accuracy, precision, recall, F1, ROC-AUC.

## Results and Model Selection

- Cross-validation and holdout metrics are reported in the notebook tables.
- The model with the highest holdout ROC-AUC is selected as the final model.
- The final model is trained on the full dataset and saved as spam_classifier.joblib.

## Notes

- See the notebook for ROC curves, confusion matrices, and detailed metric tables.
