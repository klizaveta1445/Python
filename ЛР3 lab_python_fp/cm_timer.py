
import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"time: {elapsed:.6f}")

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"time: {elapsed:.6f}")

if __name__ == '__main__':
    from time import sleep
    
    with cm_timer_1():
        sleep(1.5)
        
    with cm_timer_2():
        sleep(2.2)
