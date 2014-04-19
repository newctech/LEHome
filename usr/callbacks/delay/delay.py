#!/usr/bin/env python
# encoding: utf-8
from time import sleep
from lib.sound import Sound
from util.Res import Res
import re
from util.Util import parse_time
from lib.model import Callback


class time_callback(Callback.Callback):
    def callback(self,
            delay=None,
            delay_time=None,
            action=None,
            trigger=None, 
            ):
        DEBUG("* delay callback: %s, action: %s, target: %s" % (delay, action, target))
        return True, pre_value


class delay_callback(Callback.Callback):
    def callback(self,
            delay=None,
            delay_time=None,
            action=None,
            target=None, 
            ):
        DEBUG("* delay callback: %s, action: %s, target: %s" % (delay, action, target))

        if delay_time is None:
            return False, None

        minutes = parse_time(delay_time)
        if minutes is None:
            return False, None

        self._speaker.speak(minutes + u"分钟后执行。")
        INFO(minutes + u"分钟后执行。")
        sleep(int(minutes) * 60)

        self._home.setResume(True)
        Sound.play(
                    Res.get_res_path("sound/com_stop")
                    )
        self._home.setResume(False)

        return True, "delay"
