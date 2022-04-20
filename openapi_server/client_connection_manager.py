import time
from threading import Timer, Lock
from collections import defaultdict


class ClientConnectionManager(Timer):
    TIMEOUT = 5

    def decrement(self):
        remove = []
        for k, v in self._peers.items():
            v[1] -= 1

            if v[1] == 0:
                print(
                    f'have not heard from {k} in {ClientConnectionManager.TIMEOUT*self._interval} seconds, dropping connection'
                )
                remove.append(k)

        for k in remove:
            del self._peers[k]

    def refresh(self, ip):
        self._mutex.acquire()
        self._peers[ip] = self._peers.default_factory()
        self._mutex.release()

    def run(self):
        while not self.finished.wait(self.interval):
            self._mutex.acquire()
            self.function(*self.args, **self.kwargs)
            self._mutex.release()

    def __init__(self, interval=60):
        super().__init__(interval, self.decrement)
        self._interval = interval
        self._mutex = Lock()
        self._peers = defaultdict(lambda: [False, ClientConnectionManager.TIMEOUT])
