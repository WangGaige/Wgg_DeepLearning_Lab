import segyio
import numpy as np
from shutil import copyfile
INPUTNAME=r"seiscube_path"
f = segyio.open(INPUTNAME)

nparray=segyio.tools.cube(f)
