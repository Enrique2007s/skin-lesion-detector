import streamlit as st
import matplotlib.pyplot as plt

def page_summary():
    st.title("Summary of the Melanoma Detector")

    st.info(
        f"**General Information:**\n\n"
        f"Melanoma is a kind of cancer that develops from the pigment-producing "
        f"cells known as melanocytes. "
        f"It is the most dangerous type of skin cancer, and it can spread to "
        f"other parts of the body if not detected early. \n\n"

        f"**Early detection is crucial for successful treatment.** "
        f"In many cases, melanoma is not caught early, either being confused"
        f" with a benign mole or simply overlooked. "
        f"The Melanoma Detector aims to assist in the early detection of "
        f"melanoma by analyzing images of skin lesions and "
        f"providing a prediction of whether the lesion is likely to be "
        f"malignant or benign.\n\n "

        f"The proposed solution is a Machine Leaning(ML) model capable of "
        f"detecting melanoma from skin lesion images. \n\n"

        f"The dataset was collected from \"Melanoma Skin Cancer Dataset of 10000 Images\" dataset in Kaggle, "
        f"created by: Muhammad Hasnain Javid."
    )

    st.write(
        f"**Additional Information:**\n\n"
        f"For additional information about melanoma, please visit the following resources:\n\n"
        f"- [American Academy of Dermatology](https://www.aad.org/public/everyday-care/skin-care-basics/sun-protection)\n\n"
        f"- [Skin Cancer Foundation](https://www.skincancer.org/)\n\n"
        f"- [National Cancer Institute](https://www.cancer.gov/types/skin)"
        f"Or if you want to learn about the project itself, please visit the [README File](https://github.com/Enrique2007s/skin-lesion-detector/blob/main/README.md)"
    )

    st.success(
        f"**Business Requirements:**\n\n"
        f" 1-) The client is interested in conducting a study to visually "
        f"analyze the skin lesions of patients and determine whether they are "
        f"malignant or benign. \n\n"

        f" 2-) The client is interested in developing a machine learning model "
        f"that can accurately classify skin lesions as malignant or benign based "
        f"on images of the lesions. \n\n"

        f" 3-) The client is interested in developing a user-friendly dashboard "
        f" that allows users to upload images of skin lesions and receive "
        f"real-time predictions of whether the lesion is likely to be malignant. "
    )

    st.info(
        f"**Objectives:**\n\n"
        f"The objectives of the project are as follows:\n\n"

        f"1-) Develop a machine learning model that can accurately classify "
        f"skin lesions as malignant or benign based on images of the lesions. \n\n"

        f"2-) Integrate the model into a user-friendly dashboard that allows "
        f"users to upload images and receive real-time predictions.\n\n"

        f"3-) Significantly shorten diagnosis time for skin cancer.\n\n"

        f"4-) Ensure the dashboard is easy to use and provides a good user experience.\n\n"
    )

    st.info(
        f"**Processes:**\n\n"
        f"The processes involved in the project are as follows:\n\n"

        f"1-) Data collection and preprocessing.\n\n"

        f"2-) Model development and training.\n\n"

        f"3-) Model evaluation, validation, and testing.\n\n"

        f"4-) Integration of the model into the dashboard.\n\n"

        f"5-) Deployment of the final product.\n\n"
    )