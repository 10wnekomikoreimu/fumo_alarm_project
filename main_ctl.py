import time_ctl
import IO_ctl
import time
import os
import shutil
import csv


class MainCtl():
    def __init__(self):
        self.config_path="config.csv"
        self.default_config_header="year,month,day,hour,minute,second,sound"
        self.check_interval=60
        self.check_example()
        self.time_list, self.sound_list=self.read_config()

    def check_example(self):
        if not os.path.exists("./sound/example.mp3"):
            print("Copy example.mp3 from ./example")
            shutil.copy("./example/example.mp3", "./sound/example.mp3")
    
    #check config 
    def read_config(self):
        time_list=[]
        sound_list=[]
        if not os.path.exists(self.config_path):
            with open(self.config_path,"w") as f:
                f.write(self.default_config_header)
        with open(self.config_path, "r", encoding="utf-8") as file:
            csv_file = csv.reader(file, delimiter=',')
            for row_num,row in enumerate(csv_file):
                if row_num!=0:
                    int_list=[int(i) for i in row[0:-1]]
                    time_list.append(int_list)
                    sound_list.append(row[-1])
            if len(sound_list)==0 or len(time_list)==0:
                temp_ask_time=time_ctl.TimeCtl()
                time_list = temp_ask_time.ask_local_time(temp_ask_time.epoch_now+10)#a few seconds later
                time_list=[time_list[0:6]]
                sound_list.append("example.mp3")#notify BAKA owner to set config file
            return time_list, sound_list

    #main_timer: while(used in outside): compare -> get Min second & index -> wait -> compare / IO
    def main_alarm(self):
        #print(self.time_list)
        #print(self.sound_list)
        io_tool=IO_ctl.IOCtl()
        while(True):
            compare_result=[]
            time_tool=time_ctl.TimeCtl()
            for one_item in self.time_list:
                compare_result.append(time_tool.time_compare(time_tool.time_now,one_item,delay=1))
            wait_seconds=min(compare_result)
            list_index=compare_result.index(wait_seconds)
            #print("wait seconds: ", wait_seconds)
            #print("sound: ", self.sound_list[list_index])
            if wait_seconds > self.check_interval:
                for i in range(self.check_interval):
                    time.sleep(1)
                    #print("left: ", wait_seconds - i - 1)
            else:
                for i in range(wait_seconds):
                    time.sleep(1)
                break
        io_tool.play_sound(self.sound_list[list_index])
