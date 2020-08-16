import shutil
import sys

where, to = sys.argv[1],sys.argv[2]
shutil._unpack_zipfile(where,to)

