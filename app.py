import streamlit as st

def main():
    st.title("Indian Medicinal Plants Identifier")
    st.write("Upload an image of a plant to identify its medicinal plant name.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Add your image classification code here
        # You can use any image classification model
        # For simplicity, let's assume it's already classified and the name is 'neem'

        result = "neem"
        st.write("Predicted Medicinal Plant Name: ", result)

if __name__ == "__main__":
    main()
