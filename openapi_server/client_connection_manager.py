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

    def clients(self):
        with self._mutex:
            return self._peers.items()

    def _has_partner(self, meta):
        return meta[0]

    def next_available(self):
        with self._mutex:
            for peer, meta in self._peers.items():
                if not self._has_partner(meta):
                    meta[0] = True
                    return peer
        return ''

    def separate(self, ip):
        with self._mutex:
            self._peers[ip][0] = False

    def refresh(self, ip):
        with self._mutex:
            self._peers[ip][1] = ClientConnectionManager.TIMEOUT

    def run(self):
        while not self.finished.wait(self.interval):
            with self._mutex:
                self.function(*self.args, **self.kwargs)

    def __init__(self, interval=60):
        super().__init__(interval, self.decrement)
        self._interval = interval
        self._mutex = Lock()
        self._peers = defaultdict(lambda: [False, ClientConnectionManager.TIMEOUT])
