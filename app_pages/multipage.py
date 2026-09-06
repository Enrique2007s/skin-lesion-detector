import streamlit as st

#Create the streamlit pages
class MultiPage:
    def __init__(self, melanoma_detector) -> None:
        self.melanoma_detector = melanoma_detector
        self.pages

        st.set_page_config(page_title = 'Melanoma Detector', page_icon=":🥼")

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.title(self.melanoma_detector)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()