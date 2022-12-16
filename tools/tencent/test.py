from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_wav('20221216-154313.wav')
print('playing sound using  pydub')
play(song)