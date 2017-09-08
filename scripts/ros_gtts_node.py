#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Furushchev <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import os
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
#        assert not os.path.exists(req.wave_path), "wave_path %s already exists" % req.wave_path

        with open(req.text_path, "r") as f:
            text = f.read()
            assert len(text) > 0, "No text content to speech"
        if not req.language:
            req.language = "en"

        tts = gTTS(text=text, lang=req.language, slow=self.slow)
        tts.save(req.wave_path)
        assert os.path.exists(req.wave_path), "wave file was not generateed. Some thing wrong."
        return TextToSpeechResponse(ok=True)


if __name__ == '__main__':
    rospy.init_node("gtts")
    n = ROSGTTSNode()
    rospy.spin()
