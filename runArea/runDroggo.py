import sys
sys.path.append('../brainCore/')
sys.path.append('../nervousCentralCore/')

import brainCore
import nervousCentralCore

nervous = nervousCentralCore.NervousSystem()
brain = brainCore.Brain(nervous);