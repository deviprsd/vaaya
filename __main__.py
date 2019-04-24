__package__ = 'vaaya'

import sys

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    import vaaya.test
else:
    from vaaya.runner import run

    run()
