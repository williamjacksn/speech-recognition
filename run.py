import logging
import os
import pathlib
import speech_recognition
import sys

logging.basicConfig(format='%(levelname)s [%(name)s] %(message)s', level='INFO', stream=sys.stdout)
log = logging.getLogger(__name__)

AUDIO_FILE = pathlib.Path(os.getenv('AUDIO_FILE')).resolve()
log.info(f'Performing speech recognition on {AUDIO_FILE}')

r = speech_recognition.Recognizer()
with speech_recognition.AudioFile(str(AUDIO_FILE)) as source:
    log.info('Beginning audio recording')
    audio = r.record(source)
    log.info('Audio recording complete')

log.info('Beginning recognition')
log.info(r.recognize_sphinx(audio))
log.info('Recognition complete')
