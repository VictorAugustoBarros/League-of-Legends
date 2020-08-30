from time import time
from utils.logger import Logger


class Timer:
    def __init__(self, txt):
        self.txt = txt

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        Logger().info("[TIMER] {}: {:.3f}".format(self.txt, self.end - self.start))