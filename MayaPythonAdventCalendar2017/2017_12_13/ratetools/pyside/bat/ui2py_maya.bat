cd /d C:\Program Files\Autodesk\Maya2016\bin

for %%f in (%*) do (
  mayapy pyside-uic -o %~dpn1_pyside.py %%f 
)

cd /d C:\Program Files\Autodesk\Maya2017\bin
for %%f in (%*) do (
  mayapy pyside2-uic -o %~dpn1_pyside2.py %%f 
)