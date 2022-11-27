from pathlib import Path
from time import ctime
import shutil

'''Working With Files'''

path = Path("ecommerce/__init__.py")
print(path.name)    # returns filename
print(path.suffix)  # returns file extension
print(path.stem)    # returns filename body with extension
print(path.parent)  # returns parent directory
path = path.with_name("file.text")  # returns a new path with file name but same parent
print(path)
path.rename("text.txt")
print(ctime(path.stat().st_ctime))

# copy files from source to target
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)

path_dir = [p.name for p in path.iterdir() if p.is_dir()]  # extract directory name
path_file = [p.name for p in path.iterdir() if p.is_file()]  # extract file name
