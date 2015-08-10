import threading

class BlinkingThread(threading.Thread):

    def __init__(self):
        super(BlinkingThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()