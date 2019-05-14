# build the pynng interface.
#
# This script assumes the nng library has already been built; the setup.py
# script should ensure that it is built before running.  It looks in this file
# to see what the expected object file is based on the platform.
from cffi import FFI
import build_config

ffibuilder = FFI()
ffibuilder.set_source(
    "pynng._nng",
    r""" // passed to the real C compiler,
         // contains implementation of things declared in cdef()
         #define NNG_DECL
         #include <nng/nng.h>
         #include <nng/protocol/bus0/bus.h>
         #include <nng/protocol/pair0/pair.h>
         #include <nng/protocol/pair1/pair.h>
         #include <nng/protocol/pipeline0/pull.h>
         #include <nng/protocol/pipeline0/push.h>
         #include <nng/protocol/pubsub0/pub.h>
         #include <nng/protocol/pubsub0/sub.h>
         #include <nng/protocol/reqrep0/req.h>
         #include <nng/protocol/reqrep0/rep.h>
         #include <nng/protocol/survey0/respond.h>
         #include <nng/protocol/survey0/survey.h>
    """,
    libraries=build_config.libraries,
    # library_dirs=['nng/build/Debug',],
    # (more arguments like setup.py's Extension class:
    include_dirs=build_config.includes,
    extra_objects=build_config.objects,
)


with open('nng_api.h') as f:
    api = f.read()

callbacks = """
    // aio callback: https://nanomsg.github.io/nng/man/tip/nng_aio_alloc.3
    extern "Python" void _async_complete(void *);

    // nng_pipe_notify callback:
    // https://nanomsg.github.io/nng/man/tip/nng_pipe_notify.3
    extern "Python" void _nng_pipe_cb(nng_pipe, int, void *);
"""
ffibuilder.cdef(api + callbacks)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
