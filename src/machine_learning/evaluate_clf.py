import streamlit as st
from src.data_management import load_pkl_file

def evaluate_clf_performance(version):
    return load_pkl_file('outputs/{version}/evaluation.pkl')