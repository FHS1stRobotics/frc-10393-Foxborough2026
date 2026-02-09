"""Utility file to clear __pycache__ folders"""

import os
import shutil

deleted = 0
for dirpath, dirnames, filenames in os.walk('.'):
    norm_dirpath = os.path.normpath(dirpath)

    # skip any files in the .venv folder
    if ".venv" in norm_dirpath.split(os.sep):
        continue
    if os.path.basename(norm_dirpath) in ("__pycache__", ".pytest_cache"):
        shutil.rmtree(dirpath)
        deleted += 1

if deleted:
    print(f"{deleted} cache folders deleted!")
else:
    print("There were no cache folders found.")