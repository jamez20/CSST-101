# Machine Problem 2: Evaluating Machine Learning Model Performance

## 📋 Overview

This project implements and evaluates a **Logistic Regression** classification model using the Breast Cancer Wisconsin dataset. It demonstrates a complete data science workflow from data preprocessing to model evaluation and interpretation.

## 📊 Dataset

**Breast Cancer Wisconsin (Diagnostic) Dataset**

- **Source:** scikit-learn built-in dataset
- **Samples:** 569
- **Features:** 30 numeric features computed from digitized images
- **Target:** Binary classification (Malignant = 0, Benign = 1)

## 🎯 Learning Objectives

1. Apply data preprocessing, train-test split, and model training techniques
2. Implement logistic regression for classification tasks
3. Evaluate model performance using confusion matrix and learning curves
4. Apply 5-fold cross-validation to validate model reliability
5. Interpret and communicate model results accurately

## 📁 Project Structure

```
machine-problem-02/
├── logistic_regression.ipynb   # Main Jupyter notebook with all code
├── learning_curve.png          # Learning curve visualization
├── confusion_matrix.png        # Confusion matrix visualization
├── cross_validation.txt        # 5-Fold CV results summary
├── report.md                   # Interpretation and findings report
└── README.md                   # This file
```

## 🛠️ Requirements

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
```

## 🚀 How to Run

1. **Install dependencies:**

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

2. **Open the Jupyter Notebook:**

   ```bash
   jupyter notebook logistic_regression.ipynb
   ```

3. **Run all cells:**
   - Click "Kernel" → "Restart & Run All"
   - Or run cells individually with Shift + Enter

## 📈 Key Results

| Metric                | Score       |
| --------------------- | ----------- |
| Training Accuracy     | ~98.7%      |
| Testing Accuracy      | ~97.4%      |
| Cross-Validation Mean | ~96.5% ± 2% |
| Precision             | ~98%        |
| Recall                | ~97%        |
| F1-Score              | ~97%        |

## 🏆 Bonus Challenge (+10 pts)

The notebook includes a comparison with other classifiers:

- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

## 📝 Author

CSST102 - Basic Machine Learning  
Academic Year: 2025-2026
