import pystray
from PIL import Image
import threading
import sys
import main_ctl
import IO_ctl

icon_path="./icon/897.jpg"

def main_process_func():
    main_process=main_ctl.MainCtl()
    while not stop.is_set():
        main_process.main_alarm()
        
def play_random_clicked(icon):
    random_IO.play_random()

def on_quit_clicked(icon):
    stop.set()
    icon.stop()

if __name__ == "__main__":
    random_IO=IO_ctl.IOCtl()
    stop=threading.Event()
    
    main_process_thread = threading.Thread(target=main_process_func, daemon=True)
    main_process_thread.start()

    image=Image.open(icon_path)
    menu = (\
        pystray.MenuItem(text='抚摸fumo', action=play_random_clicked),\
        pystray.MenuItem(text='退出', action=on_quit_clicked)\
    )
    icon = pystray.Icon("fumo", image, "fumo alarm", menu)
    icon.run()

    try:
        sys.exit(0)
    except:
        pass
