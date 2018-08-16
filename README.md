Run speech recognition on an audio file.

Create `docker-compose.override.yml` like so:

```yaml
version: '3'

services:
  speech-recognition:
    environment:
      AUDIO_FILE: /data/audio_file.wav
    volumes:
      - /path/to/audio_file.wav:/data/audio_file.wav
```

Then run `docker-compose up`. This will build the Docker image, run speech recognition on the audio file, and
print the recognized text to the terminal.

Don't forget to clean up with `docker-compose down` and perhaps `docker image rm speech-recognition:latest`.
