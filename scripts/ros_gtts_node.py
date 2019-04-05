#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Furushchev <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import codecs
import os
import warnings
from pydub import AudioSegment

import rospy
from gtts import gTTS

from ros_gtts.srv import TextToSpeech, TextToSpeechResponse

from dynamic_reconfigure.server import Server
from ros_gtts.cfg import GTTSConfig as Config


class ROSGTTSNode(object):
    def __init__(self):
        self.cfg_srv = Server(Config, self.config_callback)
        self.tts_srv = rospy.Service("text_to_speech", TextToSpeech,
                                     self.tts_srv_cb)

    def config_callback(self, config, level):
        self.slow = config.slow
        return config

    def tts_srv_cb(self, req):
        assert len(req.wave_path) > 0, "No output wave_path specified"

        with codecs.open(req.text_path, encoding="utf-8", mode="r") as f:
            text = f.read()
            assert len(text) > 0, "No text content to speech"
        if not req.language:
            req.language = "en"

        filename, ext = os.path.splitext(req.wave_path)
        mp3_path = filename + '.mp3'
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tts = gTTS(text=text, lang=req.language, slow=self.slow)
            tts.save(mp3_path)
            AudioSegment.from_mp3(mp3_path).export(req.wave_path, format='wav')
        assert os.path.exists(req.wave_path), "wave file was not generateed. Something went wrong."
        return TextToSpeechResponse(ok=True)


if __name__ == '__main__':
    rospy.init_node("gtts")
    n = ROSGTTSNode()
    rospy.spin()
