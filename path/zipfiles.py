from pathlib import Path
from zipfile import ZipFile

# zipping a file
with ZipFile("filee.zip", "w") as zipp:
    for path in Path(r"C:\Users\denni\Videos\python_practice\oop").rglob("*.*"):
        zipp.write(path)

# Extracting zip file
with ZipFile("filee.zip", "r") as zipp:
    print(zipp.namelist())
    zipp.extractall("extract")
