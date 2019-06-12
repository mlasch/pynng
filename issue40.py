from collections import Counter
import time

import pynng
from pynng.nng import dbg


SLEEPY = False


addr = 'inproc:///tmp/derpderpderp'
sock = pynng.Pair0(listen=addr, name='listener')
i = 0
while True:
    try:
        i += 1
        name = 'dialer{}'.format(i)
        if i % 1000 == 0:
            counter = Counter(tuple(v) for k, v in dbg.copy().items() if len(v) <= 3)
            print('iter {} c {}'.format(i, counter))
        with pynng.Pair0(dial=addr, block_on_dial=False, name=name):
            # Add in some sleeping to see how things change
            if SLEEPY:
                time.sleep(0.001)
            pass
    except KeyboardInterrupt:
        counter = Counter(tuple(v) for k, v in dbg.copy().items() if len(v) <= 3)
        print('iter {} c {}'.format(i, counter))
        break
