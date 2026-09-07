import streamlit as st

def page_hypothesis_body():
    st.title("Project Hypothesis")
    st.write("### First Hypothesis and its validation")

    st.info(
        f"**Skin lesions are all unique in size, shape, colour, and symmetry. However, "
        f" there are certain patterns and characteristics that can help distinguish "
        f" between benign and malignant skin lesions. We expect benign lesions to have "
        f" more regular patterns, more uniform colour, and more symmetrical shapes, while"
        f" malignant lesions may have more irregular patterns, less uniform colour, and "
        f" less symmetrical shapes.**\n\n"
        f"**We expect the model to be able to learn these patterns and characteristics "
        f" and use them to accurately classify skin lesions as benign or malignant.**"
    )

    st.warning(
        f"The model achieved an accuracy of 0.81 on the test set, which indicates "
        f"that it was able to learn these patterns and characteristics to some extent. "
        f"However, there is still room for improvement. The model was very successful in "
        f"identifying benign lesions, with a precision of 0.73 and a recall of 0.99. But "
        f"it struggled with identifying malignant lesions, with a precision of 0.98 and a recall of 0.61. "
    )

    st.write("---")

    st.write(f"### Second Hypothesis and its validation")

    st.info(
        f" **The implementation of the model can reduce deaths caused by melanoma "
        f"by making skin lesion screening more accessible and efficient, leading to a"
        f" reduction in mortality rates.**\n\n"
    )

    st.success(
        f"**The model achieved an accuracy of 0.81 on the test set, which indicates "
        f"that it was able to learn these patterns and characteristics to some extent. "
        f"However, as previously stated, it falls short when identifying malignant lesions.**\n\n"
        f"**This can be considered as a success, as the model can be used as a screening "
        f"tool to identify potential cases of melanoma, "
        f"which can then be referred to a dermatologist for further evaluation.**")

    st.write("---")

    st.write(f"### Third Hypothesis and its validation")

    st.info(
        f"**The implementation of the model can reduce the number of unnecessary biopsies on benign skin lesions, "
        f"thereby reducing the burden on healthcare systems, economic costs, and improving patient outcomes.**"
    )

    st.success(
        f"**As the model was able to accurately identify almost all benign lesions, "
        f"this hypothesis can also be considered a success."
        f" This means that the model can help reduce the number of unnecessary biopsies, "
        f" which is a significant benefit for both patients and healthcare systems.**"
        )

    st.write("---")

    st.write(
        f" In conclusion, the model was able to accurately label benign skin lesions. "
        f" However, when it comes to malignant skin lesions, it struggled to identify them accurately."
        f" \n\n\n\n"
        f"#### Future Improvements\n\n"
        f"To improve the model's performance, we can consider the following future improvements:\n\n"
        f"- Implementing more data augmentation techniques to increase the diversity of the training data and improve the model's ability to generalize to new data.\n"
        f"- Exploring different model architectures and hyperparameter tuning to improve the model's performance.\n"
        f"- Implementing explainable AI techniques to provide insights into the model's decision-making process and help build trust with users.\n"
        f"- Collaborating with dermatologists and other medical professionals to validate the model's performance and ensure that it meets clinical standards.\n"
    )