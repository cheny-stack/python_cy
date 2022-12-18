import io
import simpleaudio as sa

# some_bytes = bytearray(b'RIFF$T\x01\x00WAVEfmt')
# data = open('my_file', 'rb').read() # b'RIFF$T\x01\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x
# some_bytes.extend(data)
# wave_obj = sa.WaveObject.from_wave_file(io.BytesIO(some_bytes))

# play_obj = wave_obj.play()
# play_obj.wait_done() 

from pydub import AudioSegment
from pydub.playback import play

data = open('my_file', 'rb').read()

# song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
song = AudioSegment.from_file(io.BytesIO(data), format="raw", 
                                   frame_rate=16000, channels=1, 
                                   sample_width=2,nframes=0).remove_dc_offset()
# song = song.speedup(1.5, 150, 25)                                  
play(song)

