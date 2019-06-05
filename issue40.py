import logging
import pynng
import time


# logging.basicConfig(level=logging.DEBUG)


addr = 'inproc:///tmp/derpderpderp'
# addr = 'tcp://127.0.0.1:31131'
sock = pynng.Pair0(listen=addr)
try:
    while True:
        with pynng.Pair0(dial=addr, block_on_dial=False):
            time.sleep(0)
except KeyboardInterrupt:
    pass
