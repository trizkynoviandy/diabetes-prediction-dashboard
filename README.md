# Red Wine Quality Prediction

This project aims to predict the quality of red wine using machine learning techniques. Wine quality is a complex attribute influenced by various factors, and by leveraging a dataset of wine properties, we can build a predictive model to classify wine quality.

## Dataset 

The dataset, comprising various features related to red wine, such as acidity levels, alcohol content, and more, includes a quality rating that was utilized as the target variable for classification. 

Dataset source: [here](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

## Methodology

The methodology involved the following steps:

1. Data Preprocessing:

* The problem was made binary by categorizing wine quality as either "high quality" or "low quality" based on a threshold value.
* The issue of class imbalance was addressed by applying random undersampling to balance the dataset.

2. Model Selection and Tuning:

* The XGBoost algorithm, a powerful gradient boosting technique, was employed as the classifier.
* To optimize model hyperparameters, a grid search was performed using cross-validation.

## Results

After the model was trained and evaluated, the following performance metrics were achieved on the testing set:

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 0.87   |
| Precision | 0.85   |
| Recall    | 0.91   |
| F1-Score  | 0.88   |

These metrics demonstrate the effectiveness of our machine learning model in predicting red wine quality.

## Conclusion

In conclusion, a machine learning model was successfully built to predict the quality of red wine. By converting the wine quality into a binary classification problem and addressing class imbalance, impressive results were achieved in terms of accuracy, precision, recall, and F1-score. This model can be valuable for wine producers and enthusiasts to assess and improve the quality of red wines. Further research and refinement can be undertaken to enhance the model's predictive capabilities and applicability in the wine industry.
