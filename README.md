ros_gtts
========

Text-to-Speech service for ROS using python gTTS library for backend.


## Usage

```bash
roslaunch ros_gtts gtts.launch
```

```lisp
$ roseus
$ (load "package://ros_gtts/euslisp/speak.l")
$ (speak "hello" :lang :en)
```

## Author

Yuki Furuta <<furushchev@jsk.imi.i.u-tokyo.ac.jp>>
