import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as imread
from src.machine_learning.evaluate_clf import evaluate_clf_performance

outputs = os.path.join('outputs', 'v1') #cross platform compatibility
outputs = "outputs/v1"

def page_model_performance():
    st.title("Model Performance Metrics")
    st.write(
        f"**The Model Performance page provides an overview of the performance metrics "
        f"of the melanoma detection model. This page contains various visualizations "
        f"and metrics that help users understand how well the model performs in "
        f"predicting whether a skin lesion is benign or malignant.**\n\n"
    )

    # Load evaluation.pkl file
    evaluation_file_path = os.path.join(outputs, 'evaluation.pkl')
    if os.path.exists(evaluation_file_path):
        evaluation_metrics = pd.read_pickle(evaluation_file_path)
        st.write("### Evaluation Metrics")
        st.dataframe(evaluation_metrics)
        st.write(
            f"* Accuracy = 0.8055 means the model classified approximately 80.55% of test images correctly.\n\n "
            f"* Loss = 0.4858 is the average binary cross-entropy error."
            f"Lower is better, but it is not a percentage and is less directly interpretable than accuracy."
        )

    st.write("---")

    # Plot classification report
    st.write("### Classification Report")
    st.write(
        f"The classification report provides precision, recall, and F1-score for each class (benign and malignant). "
        f"Precision is the ratio of true positives to the sum of true positives and false positives. "
        f"Recall is the ratio of true positives to the sum of true positives and false negatives. "
        f"F1-score is the harmonic mean of precision and recall. "
    )
    classification_report_file_path = os.path.join(outputs, 'classification_report.txt')
    if os.path.exists(classification_report_file_path):
        with open(classification_report_file_path, 'r') as f:
            report_lines = f.readlines()

        report_rows = []
        for line in report_lines:
            parts = line.split()
            if len(parts) == 5 and parts[0] not in {'accuracy'}:
                report_rows.append([parts[0], *map(float, parts[1:])])
            elif len(parts) == 3 and parts[0] == 'accuracy':
                report_rows.append([parts[0], float(parts[1]), None, None, int(parts[2])])
            elif len(parts) == 6 and parts[0] in {'macro', 'weighted'}:
                report_rows.append([
                    f'{parts[0]} {parts[1]}',
                    float(parts[2]),
                    float(parts[3]),
                    float(parts[4]),
                    int(parts[5]),
                ])

        report_table = pd.DataFrame(
            report_rows,
            columns=['Class', 'Precision', 'Recall', 'F1-score', 'Support'],
        ).set_index('Class')
        st.dataframe(
            report_table.style.format(
                {'Precision': '{:.2f}', 'Recall': '{:.2f}', 'F1-score': '{:.2f}'}
            ),
            use_container_width=True,
        )

    st.info(
        f" Class: We have two classes of which the model can predict(Benign and Malignant)\n\n"
        f" Precision: Malignant(0.98). When the model suspects a lesion is cancerous, it is correct 98% of the time. \n\n"
        f" Benign(0.63). When the model suspects a lesion is non-cancerous, it is correct 63% of the time.\n\n"
        f" Recall: Benign(0.99). This means the model correctly identifies 99% of all actual benign lesions. Malignant(0.61)."
        f" This means the model only catches 61% of actual skin cancers. This is a massive red flag, as it is better to flag a "
        f" benign lesion than to miss a malignant one.\n\n"
        f" F1-score: 0.75 for Malignant shows the model struggles to balance catching cancers and being accurate when it does.\n\n"
        f" Support: This is the number of images in the test dataset for each class. Benign: 1101 images, Malignant: 1022 images.\n\n"
        f" Accuracy: 0.81 means the model correctly classifies 81% of all test images.\n\n"
        f" Macro Avg: (0.85, 0.80, 0.80) This is the average of the scores, treating both classes equally, regardless of their support.\n\n"
        f" Weighted Avg: (0.85, 0.81, 0.80) This is the average of the scores, weighted by the number of instances in each class, which in this case, is almost identical."
    )

    st.write("---")

    #Confusion Matrix, both .txt and png
    st.write("### Confusion Matrix")

    confusion_matrix_text_path = os.path.join(outputs, 'confusion_matrix.txt')
    if os.path.exists(confusion_matrix_text_path):
        with open(confusion_matrix_text_path, 'r') as f:
            confusion_matrix_text = f.read()
        st.text(confusion_matrix_text)
    st.info(
        f"The confusion matrix confirms the recall score seen earlier. Out of 1022 "
        f"actual malignant lesions, the model correctly identified 622 as malignant, but misclassified 397 as benign(38.8% miss rate). \n\n"
        f"The plot below shows the same information more clearly."
    )

    confusion_matrix_image_path = os.path.join(outputs, 'confusion_matrix.png')
    if os.path.exists(confusion_matrix_image_path):
        st.image(
            confusion_matrix_image_path,
            caption='Confusion Matrix',
            use_container_width=True,
        )

    st.write("---")

    #

    # Plot confusion matrix
    # st.write("### Confusion Matrix")
    # evaluate_clf_performance(evaluation_metrics, outputs)