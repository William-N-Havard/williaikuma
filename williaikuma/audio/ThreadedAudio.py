#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: ThreadedAudio$.py (as part of project Williaikuma)
#   Created: 15/10/2022 00:52
#   Last Modified: 15/10/2022 00:52
# -----------------------------------------------------------------------------
#   Author: William N. Havard
#           Postdoctoral Researcher
#
#   Mail  : william.havard@ens.fr / william.havard@gmail.com
#  
#   Institution: ENS / Laboratoire de Sciences Cognitives et Psycholinguistique
#
# ------------------------------------------------------------------------------
#   Description: 
#       • 
# -----------------------------------------------------------------------------

import wave
import pyaudio
import threading
import simpleaudio

from williaikuma.models.Messages import MSG
from williaikuma.models.utils import assert_recording_exists, assert_recording_readable

class ThreadedPlayer(threading.Thread):
    def __init__(self, audio_path):
        super(ThreadedPlayer, self).__init__()
        self.audio_path = audio_path

    def run(self):
        try:
            wave_object = simpleaudio.WaveObject.from_wave_file(self.audio_path)
            wave_play = wave_object.play()
            wave_play.wait_done()
        except Exception as e:
            raise IOError(MSG.EXCEPT_READING_WAVE_FILE.format(str(e)))

    def stop(self):
        pass


class ThreadedRecorder(threading.Thread):
    def __init__(self, audio_path, sampling_rate, num_channels,
                 chunk_size = 1024, format=pyaudio.paInt16):
        super(ThreadedRecorder, self).__init__()
        self.continue_recording = True

        self.audio_path = audio_path
        self.format = format
        self.chunk = chunk_size
        self.channels = num_channels
        self.sampling_rate = sampling_rate

    def run(self):
        audio_input_stream = pyaudio.PyAudio()

        with wave.open(self.audio_path, 'wb') as wave_file:
            wave_file.setnchannels(self.channels)
            wave_file.setsampwidth(audio_input_stream.get_sample_size(self.format))
            wave_file.setframerate(self.sampling_rate)

            wave_stream = audio_input_stream.open(format=self.format, channels=self.channels, rate=self.sampling_rate,
                                                  input=True, frames_per_buffer=self.chunk)
            while self.continue_recording:
                wave_file.writeframes(wave_stream.read(self.chunk))

            wave_stream.stop_stream()
            wave_stream.close()
            audio_input_stream.terminate()
        del audio_input_stream

    def stop(self):
        self.continue_recording = False

    @property
    def success(self):
        return assert_recording_exists(self.audio_path) and assert_recording_readable(self.audio_path)