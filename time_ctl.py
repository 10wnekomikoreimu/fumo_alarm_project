import time


class TimeCtl():
    def __init__(self):
        self.time_now=self.ask_local_time()
        self.epoch_now=self.ask_epoch()
    
    def ask_local_time(self,stamp=None):
        response_time=time.localtime(stamp)
        time_return=[response_time.tm_year,response_time.tm_mon,response_time.tm_mday,response_time.tm_hour,response_time.tm_min,response_time.tm_sec,response_time.tm_wday,response_time.tm_yday,response_time.tm_isdst]#年，月，日，时，分，秒，星期，一年第几天，是否夏令时
        return time_return

    def ask_epoch(self):
        response_epoch=time.time()
        return response_epoch

    def time_compare(self,now,target,delay=1):
        if (target[3]-now[3]<0) or (target[3]-now[3]==0 and target[4]-now[4]<0) or (target[3]-now[3]==0 and target[4]-now[4]==0 and target[5]-now[5]<0):
            second_wait=(target[3]-now[3]+24)*60*60+(target[4]-now[4])*60+(target[5]-now[5])#change to the next day if passed the target
        else:
            second_wait=(target[3]-now[3])*60*60+(target[4]-now[4])*60+(target[5]-now[5])
        return second_wait+int(delay)