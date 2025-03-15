import speech_recognition as sr

from web_voice_control.utils.schema import STTResponse
from speech_recognition.audio import AudioData


class Speech:

    def __init__(self):
        self._microphone = sr.Microphone()
        self._recognizer = sr.Recognizer()

    def get_text(self) -> STTResponse:
        audio = self._record()
        response = self._recognize(audio)
        return response

    def _record(self) -> AudioData:
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)
            return self._recognizer.listen(source)

    def _recognize(self, audio: AudioData) -> STTResponse:
        try:
            response = STTResponse(
                success=True,
                transcription= self._recognizer.recognize_google(audio, language="ru-RU"),
                error=None
            )
        except sr.RequestError:
            response = STTResponse(
                success=False,
                error="API недоступен",
                transcription=None
            )
        except sr.UnknownValueError:
            response = STTResponse(
                success=False,
                error="Не удалось распознать речь",
                transcription=None
            )

        return response
