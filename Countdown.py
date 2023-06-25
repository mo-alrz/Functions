import time


def countdown(t):
    while t:
        min, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, secs)
        print(timer, end="\r", flush=True)
        time.sleep(1)
        t -= 1

    print('Time is up')


countdown(int(5))