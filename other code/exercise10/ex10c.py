import time
import random

class Stopwatch:
    def __init__(self):
        self.StartTime = time.time()
        self.EndTime = time.time()

    def start(self):
        self.StartTime = time.time()

    def stop(self):
        self.EndTime = time.time()

    def elapsedTime(self):
        return self.EndTime - self.StartTime

    def getStartTime(self):
        return self.StartTime

    def getEndTime(self):
        return self.EndTime

def main():
    mywatch = Stopwatch()
    mylist = []
    for i in range(10000):
        mylist.append(random.randint(0,1000))
    mywatch.start()
    mylist.sort()
    mywatch.stop()
    return mywatch.elapsedTime()

if __name__ == '__main__':
    main()
