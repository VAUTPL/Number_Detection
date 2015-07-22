# python audio.py output.wav
# python audio.py Jaded.wav

import pyaudio
import wave
import time
import sys


#REPRODUCIR
if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()
wf.close()

p.terminate()


#--Grabar
#CHUNK = 1024
#FORMAT = pyaudio.paInt16
#CHANNELS = 2
#RATE = 44100
#RECORD_SECONDS = 5
#WAVE_OUTPUT_FILENAME = "output.wav"
#
#p = pyaudio.PyAudio()
#
#stream = p.open(format=FORMAT,
#                channels=CHANNELS,
#                rate=RATE,
#                input=True,
#                frames_per_buffer=CHUNK)
#
#print("* recording")
#
#frames = []
#
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#    data = stream.read(CHUNK)
#    frames.append(data)
#
#print("* done recording")
#
#stream.stop_stream()
#stream.close()
#p.terminate()
#
#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT))
#wf.setframerate(RATE)
#wf.writeframes(b''.join(frames))
#wf.close()
