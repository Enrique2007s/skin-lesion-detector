import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import streamlit as st
from app_pages.multipage import MultiPage

# Load the page body scripts
from app_pages.page_instructions import page_instructions_body
from app_pages.page_summary import page_summary
from app_pages.page_skin_lesion_visualizer import page_skin_lesion_visualizer
from app_pages.page_skin_lesion_detector import page_skin_lesion_detector_body
# from app_pages.page_model_performance import page_model_performance

app = MultiPage(melanoma_detector_app="Melanoma Detector")

app.add_page("Instructions", page_instructions_body)
app.add_page("Summary", page_summary)
app.add_page("Skin Lesion Visualizer", page_skin_lesion_visualizer)
app.add_page("Skin Lesion Detector", page_skin_lesion_detector_body)
app.add_page("Model Performance", page_model_performance)

app.run()