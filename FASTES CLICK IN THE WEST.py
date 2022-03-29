import pyautogui, threading, time, keyboard 

time.sleep(2)
pyautogui.FAILSAFE = False
rangeOf = 16
threads = []
def do_requests():
    count = 1
    while True:
        #pyautogui.write('q')  
        #keyboard.press_and_release('q')
        #keyboard.press_and_release('ctrl+v')
        pyautogui.click()    

        if keyboard.is_pressed('X'):
            print("ended at " , count, "")
            break

for i in range(rangeOf):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)
for i in range(rangeOf):
    threads[i].start()
for i in range(rangeOf):
    threads[i].join()
