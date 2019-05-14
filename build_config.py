"""
Holds on to build config information.  The globals "objects" and "includes" can
be overwritten by specifying arguments "--nng-lib" and "--nng-include-dir" to
the setup script.  In normal usage, the globals won't be changed

"""
import sys
import shutil

if sys.platform == 'win32':
    if shutil.which('ninja'):
        objects = ['./nng/build/nng.lib']
    else:
        objects = ['./nng/build/Release/nng.lib']
    # libraries determined to be necessary through trial and error
    libraries = ['Ws2_32', 'Advapi32']
else:
    objects = ['./nng/build/libnng.a']
    libraries = ['pthread']

includes = ['nng/include']


