import streamlit as st
import os
from config import GOOGLE_API_KEY, DEFAULT_MODEL, DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES
from utils import extract_audio
from gemini_client import configure_genai, process_media
from analyzer import get_timestamps, get_seo_info, get_social_media_post
import constants

st.set_page_config(
    page_title="Video/Audio Analysis with Google AI",
    layout=constants.PAGE_LAYOUT,
    initial_sidebar_state=constants.INITIAL_SIDEBAR_STATE,
)

def main():

   # Cargar la imagen
    image_url = "media/youtube-gemini.png"
    st.image(image_url, use_column_width=True)
    st.title("Video/Audio Youtube assistant with Google Gemini AI")

    api_key = st.text_input("Ente r your Google API Key:", value=GOOGLE_API_KEY, type="password")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])
    is_audio_only = st.checkbox("Process audio only")

    model_name = st.selectbox(
        "Select the model to use:",
        (constants.GEMINI_FLASH_MODEL,constants.GEMINI_PRO_MODEL),
        index=1 if DEFAULT_MODEL == constants.GEMINI_PRO_MODEL else 0
    )

    language = st.selectbox(
        "Select the language for the response:",
        SUPPORTED_LANGUAGES,
        index=SUPPORTED_LANGUAGES.index(DEFAULT_LANGUAGE)
    )

    if st.button("Start Processing") and uploaded_file is not None and api_key:
        process_media_file(uploaded_file, api_key, model_name, is_audio_only, language)
    else:
        st.write("Please upload a video file and enter your Google API Key to proceed.")

def process_media_file(uploaded_file, api_key, model_name, is_audio_only, language):
    st.write("Processing media...")

    with open(constants.TEMP_MEDIA_PATH, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        configure_genai(api_key)

        if is_audio_only:
            extract_audio(constants.TEMP_MEDIA_PATH, constants.TEMP_AUDIO_PATH)
            media_model, type_model, media_file = process_media(constants.TEMP_AUDIO_PATH, model_name, is_audio_only)
        else:
            media_model, type_model, media_file = process_media(constants.TEMP_MEDIA_PATH, model_name, is_audio_only)

        display_results(media_model, type_model, media_file, is_audio_only, language)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        cleanup_temp_files()

def display_results(media_model, type_model, media_file, is_audio_only, language):
    st.subheader("Timestamps")
    timestamps = get_timestamps(media_model, is_audio_only, media_file, language)
    st.markdown(timestamps)

    st.subheader("SEO Information")
    seo_info = get_seo_info(media_model, is_audio_only, media_file, language)
    st.markdown(seo_info)

    st.subheader("Social media post")
    seo_info = get_social_media_post(media_model, is_audio_only, media_file, language)
    st.markdown(seo_info)    

    if type_model == 'cache_model':
        media_model.delete()

def cleanup_temp_files():
    if os.path.exists(constants.TEMP_MEDIA_PATH):
        os.remove(constants.TEMP_MEDIA_PATH)
    if os.path.exists(constants.TEMP_AUDIO_PATH):
        os.remove(constants.TEMP_AUDIO_PATH)

if __name__ == "__main__":
    main()