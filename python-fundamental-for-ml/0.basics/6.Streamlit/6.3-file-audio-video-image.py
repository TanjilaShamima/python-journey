import streamlit as st

def main():
    st.title("Hello, Streamlit!")
    st.write("This is a simple Streamlit app.")
    st.header("Upload your files")

    # uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "gif", "mp4", "mp3"], accept_multiple_files=False)

    uploaded_files = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "gif", "mp4", "mp3"], accept_multiple_files=True)

    # if uploaded_file is not None:
    #     file_type = uploaded_file.type
    #     if file_type.startswith("image/"):
    #         st.image(uploaded_file, caption="Uploaded Image")
    #     elif file_type.startswith("video/"):
    #         st.video(uploaded_file, caption="Uploaded Video")
    #     elif file_type.startswith("audio/"):
    #         st.audio(uploaded_file, caption="Uploaded Audio")
    #     else:
    #         st.write("Unsupported file type. Please upload an image, video, or audio file.")
    if len(uploaded_files) > 0:
        col = st.columns(len(uploaded_files))
        for i, file in enumerate(uploaded_files):
            file_type = file.type
            if file_type.startswith("image/"):
                with col[i]:
                    st.image(file, caption="Uploaded Image")
            elif file_type.startswith("video/"):
                with col[i]:
                    st.video(file, caption="Uploaded Video")
            elif file_type.startswith("audio/"):
                with col[i]:
                    st.audio(file, caption="Uploaded Audio")
            else:
                st.write("Unsupported file type. Please upload an image, video, or audio file.")

    

if __name__ == "__main__":
    main()