#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019, GITAI Inc.
# All rights reserved.
# Author: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import rospy
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
from sound_play.libsoundplay import SoundClient


class TextToSpeechRelay(object):
    def __init__(self):
        super(TextToSpeechRelay, self).__init__()
        self.speech = SoundClient(True)
        self.sub_text = rospy.Subscriber(
            'speech_to_text', SpeechRecognitionCandidates, self.callback)

    def callback(self, msg):
        if msg.transcript and msg.transcript[0]:
            self.speech.say(msg.transcript[0], 'ja')


if __name__ == '__main__':
    rospy.init_node('text_to_speech_relay')
    t = TextToSpeechRelay()
    rospy.spin()
