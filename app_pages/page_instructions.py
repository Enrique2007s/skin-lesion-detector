import streamlit as st

def page_instructions_body():
    st.write(
    f"**Usage guidelines for the Streamlit Dashboard:**\n\n"
)

    st.info(
        f"**The Summary Page:**\n\n"
        f"The Summary page provides an overview of the Melanoma Detector project, "
        f"including general information about melanoma, the objectives of the project, "
        f"and the business requirements. It also includes links to additional resources "
        f"for users who want to learn more about melanoma and the project itself.\n\n"
    )

    st.info(
        f"**The Melanoma Visualizer Page:**\n\n"
        f"The Melanoma Visualizer page allows users to view images of skin "
        f"lesions. This page contains a gallery of images, along with "
        f"general descriptions of benign and malignant lesions and what to "
        f"look for in each type.\n\n"
        )

    st.info(
        f"**The Melanoma Detector Page:**\n\n"
        f"The Melanoma Detector page allows users to upload images of skin lesions "
        f"and receive real-time predictions of whether the lesion is likely to be "
        f"malignant or benign. The page includes a file uploader for users to upload "
        f"images. The uploaded images are then processed by the machine learning model, which "
        f"performs the actual prediction."
        f"The page also displays the prediction results, including the predicted "
        f"class (malignant or benign) and the associated confidence score.\n\n"
        f"if the model predicts with a low confidence score, the user can compare "
        f"their skin patch with the images in the Melanoma Visualizer page."
    )

    st.success(
        f"**Instructions to Use the Melanoma Detector:**\n\n"
        f"1-) Navigate to the Melanoma Detector page using the sidebar menu.\n\n"
        f"2-) Upload an image of a skin lesion using the file uploader.\n\n"
        f"3-) Click the 'Predict' button to receive the prediction results.\n\n"
        f"4-) If the prediction is uncertain, compare your skin patch with the "
        f"images in the Melanoma Visualizer page."
    )

    st.info(
        f"**Hypothesis Page**\n\n"
        f"The Hypothesis page presents the underlying assumptions and hypotheses "
        f"that guide the development and use of the Melanoma Detector. It includes "
        f"information about the expected performance of the model and the "
        f"conditions under which it is most likely to be accurate."
    )

    st.info(
        f"**Performance Metrics Page**\n\n"
        f"The Performance Metrics page provides detailed information about the "
        f"performance of the Melanoma Detector model. It includes metrics such as "
        f"accuracy, precision, recall, and F1 score, as well as roc curves and confusion matrices "
        f"that illustrate the model's performance across different classes and "
        f"conditions. This page helps users understand the reliability and limitations "
        f"of the model's predictions."
    )

    st.warning(
        f"**Disclaimer:**\n\n"
        f"The Melanoma Detector is a machine learning model that provides predictions "
        f"based on the images of skin lesions. It is not a substitute for professional "
        f"medical advice, diagnosis, or treatment. Users should consult with a qualified "
        f"healthcare provider for any medical concerns or questions regarding their skin health."
    )