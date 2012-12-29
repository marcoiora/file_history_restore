file_history_restore
====================

python script to restore last copy of windows 8 file history backup

usage:
python restore.py

effect:
starting from cwd, recursively, search files with filename partially matching "(YYYY_MM_DD hh_mm_ss UTC)", then choose last version of file * and restore it to original filename (if original file does not exist).

finally delete unused copies

* the last version is the one with the greater datetime before actual datetime
