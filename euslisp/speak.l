;; speak.l
;; Author: Furushchev <furushchev@jsk.imi.i.u-tokyo.ac.jp>

(require :speak "package://pr2eus/speak.l")

(defun speak (str &key (lang :ja) (wait *speak-wait*) (topic-name "robotsound_gtts") (timeout *speak-timeout*))
  (send-speak-msg
   (instance sound_play::SoundRequest :init
             :sound sound_play::SoundRequest::*say*
             :command sound_play::SoundRequest::*play_once*
             :arg (format nil "~A~%~A" (string-downcase lang) str)
             :arg2 "aq_rm.phont")
   :topic-name topic-name
   :wait wait
   :timeout timeout))
