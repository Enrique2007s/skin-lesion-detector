import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
from tensorflow.keras.models import load_model
from src.data_management import load_pkl_file



def plot_predictions_probabilities(pred_proba, pred_class): #I have no idea why without pred_class, the function does not work. It is not used in the function, but it is required for some reason. I have no idea why.
    """                                                     #It is not used in the function, but it is required for some reason. I have no idea what is going on here. Please DO NOT TOUCH.
    Plot prediction probability results.
    pred_proba is the raw probability of being malignant (from model output).
    """
    # The model outputs the probability of being Malignant.
    # Therefore, the probability of being Benign is 1 - pred_proba.
    malignant_prob = pred_proba
    benign_prob = 1 - pred_proba

    # Create a clean DataFrame with exactly 2 rows
    df_prob = pd.DataFrame({
        'Diagnostic': ['benign', 'malignant'],
        'Probability': [benign_prob, malignant_prob]
    })
    df_prob['Probability'] = df_prob['Probability'].round(3)

    # Plot the bar chart
    fig = px.bar(
        df_prob,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600,
        height=300,
        template='seaborn',
        title='Prediction Probabilities'
    )
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)
    st.info(
        f"The addition of the probabilities of benign and malignant should equal 1."
        f"In the bar chart, probabilities are represented as a fraction of 1, where 1 represents 100% probability."
        f"Multiplying the probabilities by 100 will convert them to percentages, where 100% represents a certainty of the prediction."
    )



def resize_input_image(img, version):
    """
    Resize the input image according to defined image shape for a specified version.
    Handles any nested structure (sets, tuples, lists) and extracts the first two numbers.
    """
    raw_shape = load_pkl_file(file_path=f"outputs/{version}/image_sizes.pkl")

    # --- Flatten the nested structure to a list of numbers ---
    def flatten(x):
        if isinstance(x, (list, tuple, set)):
            for item in x:
                yield from flatten(item)
        else:
            yield x

    numbers = list(flatten(raw_shape))
    # Keep only numeric values (int/float)
    ints = [int(n) for n in numbers if isinstance(n, (int, float))]

    # Extract height and width (first two numbers)
    if len(ints) >= 2:
        height, width = ints[0], ints[1]
    elif len(ints) == 1:
        height = width = ints[0]
    else:
        height = width = 224  # fallback

    # Resize (PIL expects (width, height))
    img_resized = img.resize((width, height), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0) / 255.0
    return my_image



def load_model_and_predict(my_image, version):
    """
    Loads the model, makes a prediction, and displays the result.
    Assumes binary classification (Benign vs Malignant) with a sigmoid output.
    """
    # 1. Load the trained model
    model = load_model(f"outputs/{version}/melanoma_detector_model.keras")
    
    # 2. Make the prediction (returns probability of being class 1 - Malignant)
    pred_proba = model.predict(my_image)[0][0]  # Shape: (1,1) -> extract the float
    
    # 3. Determine the class based on threshold 0.5
    if pred_proba > 0.5:
        pred_class = "malignant"
    else:
        pred_class = "benign"
        # If benign, the probability of benign is 1 - pred_proba
        # But we keep pred_proba as the raw malignant probability for the chart.
        # The chart function `plot_predictions_probabilities` expects the malignant probability.
    
    # 4. Display the result in Streamlit
    st.write(
        f"The model predicts that the input image is **{pred_class}** "
        f"with a probability of **{pred_proba:.2f}** (as malignant)."
    )
    
    # 5. Return the raw probability (for malignant) and the class string
    return pred_proba, pred_class
