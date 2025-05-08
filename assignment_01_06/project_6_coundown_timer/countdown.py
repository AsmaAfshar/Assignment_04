import time
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  #minutes aur seconds calculate ho rhe hain
        time_formate = '{:02d}:{:02d}'.format(mins, secs) # MM:SS FORMATE
        print(time_formate, end="\r")
        time.sleep(1)   # DELAY
        seconds -= 1
    print("00:00 \n TIMES Up!")
    
    # user input for timer
total_seconds =int(input("Enter time in seconds for Coundown: "))
countdown_timer(total_seconds)
    