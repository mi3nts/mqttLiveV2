
#!/usr/bin/python

import sys
import yaml
import os

from mintsXU4 import mintsDefinitions as mD

nodeIDs              = mD.mintsDefinitions['nodeIDs']
airMarID             = mD.mintsDefinitions['airmarID']
dataFolder           = mD.dataFolder  + "/ref/"

print()
print("MINTS")
print()

sysStr = 'rsync -avzrtu -e  "ssh -p 2222" ' + "--include='*.csv'" + " --include='*/' --exclude='*' mints@mintsdata.utdallas.edu:/home/mints/Downloads/reference/" + airMarID + " " + dataFolder
print(sysStr)
os.system(sysStr)
