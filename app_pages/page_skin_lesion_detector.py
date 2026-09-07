import streamlit as st
import numpy as np
import pandas as np
from PIL import Image

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analytics import (load_model_and_predict, resize_input_image, plot_predictions_probabilities)

def page_skin_lesion_detector_body():
    st.info(
        
    )