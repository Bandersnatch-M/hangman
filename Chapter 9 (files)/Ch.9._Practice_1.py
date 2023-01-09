# Chapter 9. Practice 1.
# Open and close files
# C:\Home\Развлечения\DUNE2\DUNE.CFG

import os
DUNE_CFG = os.path.join("C:","\Home","Развлечения","DUNE2","DUNE.CFG")
print("Путь к файлу:",DUNE_CFG)

f = open(DUNE_CFG,"r")
print (f.read())
f.close()

with open (DUNE_CFG,"r") as f:
    print (f.read())

