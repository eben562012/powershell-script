import sys
from pathlib import Path
from hashlib import sha224
import os


def _copy_file(src, dest):
	src = Path(src)
	f_data = src.read_bytes()
	new_file = Path(dest) / src.name
    new_file.write_bytes(f_data)
 


if len(sys.argv) == 2:
	raise Exception("file_transfer.py requires a src and dest arguments")

src = sys.argv[1]
dest = sys.argv[2]

src = Path(src)
if src.is_dir():
    mfiles = os.listdir(src.resolve())
else:
	mfiles = [src]
for file in mfiles:
	_copy_file(file, dest)

print(_copy_file(src, dest)
)