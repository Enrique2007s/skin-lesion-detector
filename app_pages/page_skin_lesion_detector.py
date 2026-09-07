import streamlit as st
import numpy as np
from PIL import Image

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (load_model_and_predict, resize_input_image, plot_predictions_probabilities)


version = 'v1'

def page_skin_lesion_detector_body():
    st.info(
        f"Here you can upload an image of a skin lesion and the model will predict "
        f"the type of lesion it is. The model is trained on a dataset of various "
        f"skin lesions and can help in identifying whether the lesion is benign or malignant. "
        f"Please note that this tool is for educational purposes only and should not "
        f"be used as a substitute for professional medical advice."
    )

    st.write("---")
    image_loader = st.file_uploader("Upload an image of a skin lesion",
                                    type=["jpg", "png"],
                                    help="Upload an image in jpg or png format. The image should be clear and focused on the lesion.")

    if image_loader is not None:
        image = Image.open(image_loader)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        #Resize the image to the required input size for the model
        resized_image = resize_input_image(image, version='v1')

        # Load the model and make predictions
        pred_prob, pred_class = load_model_and_predict(resized_image, version=version)

        #Plots the prediction probabilities
        plot_predictions_probabilities(pred_prob, pred_class)

    else:
        st.warning("Please upload an image to get predictions(must be in jpg or png format).")
