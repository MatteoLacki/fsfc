"""Fucking Simple File Sizes""" 
import sys
from compare_files import iter_path, write_2_csv

_, folder_path, result_path = sys.argv


# folder_path = 'test/A'
# result_path = 'file_sizes.csv'
write_2_csv(result_path, iter_path(folder_path), ['path', 'size'])