import time
import alive_progress
with alive_progress.alive_bar(1000) as bar:
    sleep = 0.01
    for _ in range(500):
        
        time.sleep(sleep)
        # print(sleep)
        bar()

