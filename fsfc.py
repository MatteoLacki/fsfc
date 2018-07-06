import sys
from compare_files import compare_paths, write_2_csv

_, A, B = sys.argv
result_path = 'diff.csv'

comparison = compare_paths(A, B)
write_2_csv(A, B, comparison, result_path)