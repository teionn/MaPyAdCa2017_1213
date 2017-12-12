for %%f in (%*) do (
  pyside-uic -o %~dpn1_pyside.py %%f 
)
for %%f in (%*) do (
  pyside2-uic -o %~dpn1_pyside2.py %%f 
)