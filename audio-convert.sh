#!/bin/bash

mkdir outputs
for f in *.mp3; do ffmpeg -i "$f" -c:a pcm_s16le "outputs/${f%.mp3}.wav"; done

