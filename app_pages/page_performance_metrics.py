import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as imread
import plotly.express as px
from src.machine_learning.evaluate_clf import evaluate_clf_performance
from src.data_management import load_pkl_file

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
            width='stretch',
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
        f"The confusion matrix confirms the recall score seen earlier. Out of 1,022 "
        f"actual malignant lesions, the model correctly identified 622 as malignant, but misclassified 397 as benign(38.8% miss rate). \n\n"
        f"The plot below shows the same information more clearly."
    )

    confusion_matrix_image_path = os.path.join(outputs, 'confusion_matrix.png')
    if os.path.exists(confusion_matrix_image_path):
        st.image(
            confusion_matrix_image_path,
            caption='Confusion Matrix',
            width='stretch',
        )

    st.write("---")

    #Image Dimensions
    st.write("### Image Dimensions")
    image_dimensions_path = os.path.join(outputs, 'image_dimensions_distribution.png')
    if os.path.exists(image_dimensions_path):
        st.image(
            image_dimensions_path,
            caption='Image Dimensions',
            width='stretch',
        )
    st.info(
        f" As we can see, all images are **300x300 pixels (RGB color format)**, which is the size the model was trained on. "
        f" The distribution of image sizes is uniform."
    )

    st.write("---")

    # Image Sizes
    st.write("### Image Sizes")
    image_sizes_path = os.path.join(outputs, 'image_sizes.pkl')
    if os.path.exists(image_sizes_path):
        image_sizes = load_pkl_file(image_sizes_path)
        size_rows = [
            {'Dimension': 'Height', 'Pixels': size[0]}
            for size in sorted(image_sizes)
        ] + [
            {'Dimension': 'Width', 'Pixels': size[1]}
            for size in sorted(image_sizes)
        ]
        size_data = pd.DataFrame(size_rows)
        fig = px.bar(
            size_data,
            x='Dimension',
            y='Pixels',
            color='Dimension',
            text='Pixels',
            title='Image Size (Pixels)',
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, width='stretch')

    st.info(
    f" The image size plot shows the height and width recorded in image_sizes.pkl. "
    f" All images are **300x300 pixels (RGB color format)**, which is the size the model was trained on.\n\n"
    f" It is good practice to ensure that the images used for training and testing are "
    f" of the same size, as this can affect the model's performance."
    )

    st.write("---")

    #Labels Distribution
    st.write("### Labels Distribution")
    labels_distribution_path = os.path.join(outputs, 'labels_distribution.png')
    if os.path.exists(labels_distribution_path):
        st.image(
            labels_distribution_path,
            caption='Labels Distribution',
            width='stretch',
        )
    st.info(
        f" The labels distribution plot shows the number of images for each class (benign and malignant) in the dataset. \n\n"
        f"* The train set contains a total of **7,422** images, with **3,849** benign and **3,573** malignant images. \n\n"
        f"* The validation set contains a total of **1,060** images, with **550** benign and **510** malignant images. \n\n"
        f"* The test set contains a total of **2,123** images, with **1,101** benign and **1,022** malignant images. \n\n"
        f" The total number of images in the dataset is **10,605**, with **5,500** benign and **5,105** malignant images. \n\n"
        f" The dataset is relatively balanced, which is important for training a model that can accurately classify both classes."
    )

    st.write("---")

    #Total images per label
    st.write("### Total Images per Label")
    total_images_per_label_path = os.path.join(outputs, 'total_images_per_label.png')
    if os.path.exists(total_images_per_label_path):
        st.image(
            total_images_per_label_path,
            caption='Total Images per Label',
            width='stretch',
        )

    st.info(
        f" The total images per label plot shows the number of images for each class (benign and malignant) in the dataset. \n\n"
        f" This visualization helps to understand the distribution of images across different labels."
        f" The dataset is relatively balanced, which is important for training a model that can accurately classify both classes."
        f" The total number of images in the dataset is **10,605**, with **5,500** benign and **5,105** malignant images. \n\n"
    )

    st.write("---")

    # Model training accuracy and loss plots
    st.write("### Model Training Accuracy and Loss")
    model_training_accuracy_path = os.path.join(outputs, 'model_training_acc.png')
    model_training_loss_path = os.path.join(outputs, 'model_training_losses.png')
    if os.path.exists(model_training_accuracy_path) and os.path.exists(model_training_loss_path):
        st.image(
            model_training_accuracy_path,
            caption='Model Training Accuracy',
            width='stretch',
        )
        st.image(
            model_training_loss_path,
            caption='Model Training Loss',
            width='stretch',
        )
    st.info(
        f" The model training accuracy and loss plots show the performance of the model during training. \n\n"
        f" The accuracy plot shows the percentage of correctly classified images over the epochs, "
        f" while the loss plot shows the decrease in loss over the epochs."
        f" Training accuracy rises steadily from about 74% to 88%\n\n"
        f" Training loss consistently decreases from about 0.63 to 0.32\n\n"
        f" Validation loss is unstable, with large spikes and no consistent downward trend. "
        f" This is a sign of overfitting, where the model performs well on the training data but poorly on unseen validation data."
    )

    st.write("---")

    #ROC Curve
    st.write("### ROC Curve")
    roc_curve_path = os.path.join(outputs, 'roc_curve.png')
    if os.path.exists(roc_curve_path):
        st.info(
        f" The ROC curve is a graphical representation of the diagnostic ability of a binary classifier system as its discrimination threshold is varied. It plots the true positive rate against the false positive rate."
        )
        st.image(
            roc_curve_path,
            caption='ROC Curve',
            width='stretch',
        )
    st.info(
        f"The ROC curve is very strong, with an AUC of 0.9597."
        f" This indicates that the model has a high ability to distinguish between the two classes."
        f" However, the ROC curve evaluates all possible thresholds. At the current threshold of 0.5, "
        f" the model is only catching 61% of actual skin cancers, which is a major concern."
    )