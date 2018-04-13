#-*- coding:utf-8 -*-
import time

class Alarm:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def SetAlarm(self, hour, min):
        self.hour = hour
        self.min = min

    def RunAlarm(self):
        while(True):
            currentTime = time.localtime()
            if currentTime.tm_hour == self.hour and currentTime.tm_min == self.min:
                print('Time up!!!\n')
                break
            else:
                time.sleep(10)

if __name__ == '__main__':
    alarm = Alarm(22, 28)
    alarm.RunAlarm()
