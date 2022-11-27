from pathlib import Path

Path()  # current directory
Path() / Path("ecommerce")
Path() / "__init_.py"

''' Working With Directories'''
path = Path(r"C:\Users\denni\Videos\python_practice\path")
Path.cwd()
path.mkdir()
path.rmdir()
path.rename("ecommerce2")

path_dir = [p for p in path.iterdir() if p.is_file()]
path_file = [p for p in path.iterdir() if p.is_file()]

path_py_files = [p for p in path.glob("*.py")]
path_py_files_r = [p.name for p in path.rglob("*.py")]  # recursive search
print(path_py_files_r)
