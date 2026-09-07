import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
from tensorflow.keras.models import load_model
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """
    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Benign': 0, 'Malignant': 1},
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x != pred_class:
            prob_per_class.loc[x] = 1 - pred_proba

    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height = 300, template='seaborn',
        title='Prediction Probabilities'
    )

    def resize_input_image(img, version):
        """
        Resize the input image according to defined image shape for a specified version
        """
        image_shape = load_pkl_file(file_path=f"outputs/{version}/image_sizes.pkl")
        img_resized= img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
        my_image = np.expand_dims(img_resized, axis=0)/255
    
        return my_image


def load_model_and_predict(my_image, version):
    """Loads the model and predicts the class of the input image"""
    model = load_model(f"outputs/{version}/melanoma_detector_model.keras")
    
    target_map = {v:k for k, v in {'benign': 0, 'malignant':1}.items()}
    pred_class= target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"the model predicts that the input image is **{pred_class}** with a probability of **{pred_proba:.2f}**."
    )

    return pred_proba, pred_class
