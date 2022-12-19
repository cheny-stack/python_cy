# coding=UTF-8
import io
import requests
import wave
import json
import time
import os
import simpleaudio as sa
from pydub import AudioSegment
from pydub.playback import play
import pygame

from request_util import request, authorization

def task_process(text):
    req = request()
    req.init()
    auth = authorization()
    auth.init()

    #request_data = collections.OrderedDict()
    request_data = dict()
    request_data['Action'] = 'TextToStreamAudio'
    request_data['AppId'] = auth.AppId
    request_data['Codec'] = req.Codec
    request_data['Expired'] = int(time.time()) + auth.Expired
    request_data['ModelType'] = req.ModelType
    request_data['PrimaryLanguage'] = req.PrimaryLanguage
    request_data['ProjectId'] = req.ProjectId
    request_data['SampleRate'] = req.SampleRate
    request_data['SecretId'] = auth.SecretId
    request_data['SessionId'] = req.SessionId
    request_data['Speed'] = req.Speed
    request_data['Text'] = text
    request_data['Timestamp'] = int(time.time())
    request_data['VoiceType'] = req.VoiceType
    request_data['Volume'] = req.Volume

    signature = auth.generate_sign(request_data = request_data)
    header = {
        "Content-Type": "application/json",
        "Authorization": signature
    }
    url = "https://tts.cloud.tencent.com/stream"
    print("开始请求")
    r = requests.post(url, headers=header, data=json.dumps(request_data), stream = True)
    print("请求成功")
    '''
    if str(r.content).find("Error") != -1 :
        print(r.content)
        return
    '''
    t = time.time()
    # song = AudioSegment.from_file(io.BytesIO(r.content), format="raw", 
    #                                frame_rate=16000, channels=1, 
    #                                sample_width=2,nframes=0).remove_dc_offset() 
    # song = AudioSegment.from_file(io.BytesIO(r.content), format="mp3")
    fp = io.BytesIO(r.content)
    fp.seek(0)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(fp, "mp3")                         
    print(f'coast:{time.time() - t:.8f}s')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # play(song)

    # i = 1
    # timestr = time.strftime("%Y%m%d-%H%M%S")
    # file_name = 'voice/' + timestr + '.wav'
    # t = time.time()

    # wavfile = wave.open(file_name, 'wb')
    # wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
    # for chunk in r.iter_content(1024):
    #     if (i == 1) & (str(chunk).find("Error") != -1) :
    #         print(chunk)
    #         return 
    #     i = i + 1
    #     wavfile.writeframes(chunk)
    # wavfile.close()
    # print(f'coast:{time.time() - t:.8f}s')
    # wav_file_path=os.getcwd() + '/' + file_name
    # # os.system("su cheny &&  vlc " + wav_file_path)
    # wave_obj = sa.WaveObject.from_wave_file(wav_file_path)
    # play_obj = wave_obj.play()
    # play_obj.wait_done()  # Wait until sound has finished playing

