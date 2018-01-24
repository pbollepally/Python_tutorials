import webbrowser
import time

break_count=0
total_breaks=2

while (break_count<total_breaks):
    print("This program started "+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=wIft-t-MQuE")
    break_count= break_count +1