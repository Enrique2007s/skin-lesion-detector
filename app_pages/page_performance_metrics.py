import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as imread
from src.machine_learning.evaluate_clf import evaluate_clf_performance

def page_model_performance():
    st.title("Model Performance Metrics")
    st.write(
        f"**The Model Performance page provides an overview of the performance metrics "
        f"of the melanoma detection model. This page contains various visualizations "
        f"and metrics that help users understand how well the model performs in "
        f"predicting whether a skin lesion is benign or malignant.**\n\n"
    )

    # Load the performance metrics from a CSV file
    performance_metrics = pd.read_csv('outputs/v1/performance_metrics.csv')

    # Display the performance metrics as a table
    st.subheader("Performance Metrics Table")
    st.dataframe(performance_metrics)

    # Plot the performance metrics
    st.subheader("Performance Metrics Visualizations")
    evaluate_clf_performance(performance_metrics)
