import streamlit as st
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

my_data_dir = 'inputs/skin_cancer_dataset/melanoma_cancer_dataset'
labels = os.listdir(my_data_dir + '/validation')
version = 'v1'

def page_skin_lesion_visualizer():
    st.title("Skin Lesion Visualizer")
    st.write(
        f"**The Melanoma Visualizer page allows users to view images of skin "
        f"lesions. This page contains a gallery of images, along with "
        f"general descriptions of benign and malignant lesions and what to "
        f"look for in each type.**\n\n"
    )

    #Average and Variability images of benign and malignant lesions
    if st.checkbox("Difference between average and variability images of benign and malignant lesions"):
        st.write(
            f"**The average image of benign lesions is generally lighter in color "
            f"and has a more uniform appearance.**\n\n"
        )
        avg_benign = imread(my_data_dir + '/avg_var_benign.png')
        st.image(avg_benign, caption="Average Image of Benign Lesions")

        st.write(
            f"**The average image of malignant lesions shows more variation in darker "
            f" colors and has a more irregular appearance.\n\n"
        )
        avg_malignant = imread(my_data_dir + '/avg_var_malignant.png')
        st.image(avg_malignant, caption="Average Image of Malignant Lesions")

    #Difference between benign and malignant lesions
    if st.checkbox("Difference between benign and malignant skin lesions"):
        
        st.write(
            f"**Benign lesions are non-cancerous growths on the skin. They are usually "
            f" harmless and do not spread to other parts of the body. "
            f"Common types of benign lesions include moles, freckles, and skin tags.\n\n"

            f"Malignant lesions are cancerous growths on the skin. They can spread "
            f"to other parts of the body if not detected early. "
            f"**\n\n"
        )
        benign_vs_malignant = imread(my_data_dir + '/benign_vs_malignant.png')
        st.image(benign_vs_malignant, caption="Benign VS Malignant Lesions")


    if st.checkbox("Characteristics of benign and malignant lesions"):
        st.write(
            f"**When examining benign lesions, look for the following characteristics:**\n\n"
            f"- Symmetry: Benign lesions are usually symmetrical in shape.\n"
            f"- Borders: The edges of benign lesions are usually smooth and well-defined.\n"
            f"- Color: Benign lesions are usually uniform in color, often brown or tan.\n"
            f"- Size: Benign lesions are usually small, typically less than 6mm in diameter.\n\n"

            f"**When examining malignant lesions, look for the following characteristics:**\n\n"
            f"- Asymmetry: Malignant lesions are often asymmetrical in shape.\n"
            f"- Borders: The edges of malignant lesions are often irregular or poorly defined.\n"
            f"- Color: Malignant lesions may have multiple colors, including shades of brown, black, red, white, or blue.\n"
            f"- Size: Malignant lesions are often larger than 6mm in diameter and may continue to grow over time.\n\n"
        )

    if st.checkbox("Malignant image montage"):
        st.write(
            f"**The user can use the montage to compare and analyze the characteristics "
            f"of malignant lesions.**\n\n"
        )
        malignant_montage = imread(my_data_dir + '/malignant_montage.png')
        st.image(malignant_montage, caption="Montage of Malignant Lesions")

    if st.checkbox("Benign image montage"):
        st.write(
            f"**The user can use the montage to compare and analyze the characteristics "
            f"of benign lesions.**\n\n"
        )
        benign_montage = imread(my_data_dir + '/benign_montage.png')
        st.image(benign_montage, caption="Montage of Benign Lesions")












    st.info(
        f"**Benign Lesions:**\n\n"
        f"Benign lesions are non-cancerous growths on the skin. They are usually "
        f" harmless and do not spread to other parts of the body. "
        f"Common types of benign lesions include moles, freckles, and skin tags. "
        f"When examining benign lesions, look for the following characteristics:\n\n"
        f"- Symmetry: Benign lesions are usually symmetrical in shape.\n"
        f"- Borders: The edges of benign lesions are usually smooth and well-defined.\n"
        f"- Color: Benign lesions are usually uniform in color, often brown or tan.\n"
        f"- Size: Benign lesions are usually small, typically less than 6mm in diameter.\n\n"
    )

    st.info(
        f"**Malignant Lesions:**\n\n"
        f"Malignant lesions are cancerous growths on the skin. They can spread to other parts of the body if not detected early. "
        f"The most common type of malignant lesion is melanoma. "
        f"When examining malignant lesions, look for the following characteristics:\n\n"
        f"- Asymmetry: Malignant lesions are often asymmetrical in shape.\n"
        f"- Borders: The edges of malignant lesions are often irregular or poorly defined.\n"
        f"- Color: Malignant lesions may have multiple colors, including shades of brown, black, red, white, or blue.\n"
        f"- Size: Malignant lesions are often larger than 6mm in diameter and may continue to grow over time.\n\n"
    )