ros_gtts
========

Text-to-Speech service for ROS using python gTTS library for backend.


## Install

``` bash
sudo pip install -U pydub
```


## Usage

1. Start server

```bash
roslaunch ros_gtts gtts.launch
```

2.1. Use from euslisp

```lisp
$ roseus
$ (ros::roseus "sound_client")
$ (load "package://pr2eus/speak.l")
$ (speak "hello" :lang :en)
```

2.2. Use from python

```python
import rospy
from sound_play.libsoundplay import SoundClient

rospy.init_node("sound_client")
client = SoundClient()
client.say("Hello!", voice="en")
client.say("Guten tag!", voice="de")
```

## Author

Yuki Furuta <<furushchev@jsk.imi.i.u-tokyo.ac.jp>>
