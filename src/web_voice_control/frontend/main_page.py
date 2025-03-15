import streamlit as st

from src.web_voice_control.utils.stt import Speech
from src.web_voice_control.utils.schema import STTResponse

def main_page():
    st.title("Голосовой ввод текста")

    speech_worker = Speech()

    if st.button("Начать запись"):
        stt_response: STTResponse = speech_worker.get_text()

        if stt_response.success:
            st.text_area("Вы сказали: ", value=stt_response.transcription, height=200)
        else:
            st.write(f"Ошибка: {stt_response.error}")
