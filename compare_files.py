import os
# import sys
import csv

# try:
#     _, A, B, result_path = sys.argv
# except ValueError:
#     _, A, B = sys.argv
#     result_path = 'diff.csv'

# A = 'test/A'
# B = 'test/B'

def rm_root(path, root):
    return path[len(root):]


def make_hashable(dir, subdir, files, root):
    dir = rm_root(dir, root)
    subdir = tuple(subdir)
    files = tuple(files)
    return dir, subdir, A


def filepath_size(dir, f, root):
	try:
		file_path = os.path.join(dir, f)
		size = os.path.getsize(file_path)
		file_path = rm_root(file_path, root)
		return file_path, size
	except FileNotFoundError:
		return file_path, "FAIL"


def iter_path(root):
    for dir, subdir, files in os.walk(root):
        if dir == root:
            for f in files:
                yield filepath_size(dir, f, root)
        else:
            if not subdir:
                if files:
                    for f in files:
                        yield filepath_size(dir, f, root)
                else:
                    yield rm_root(dir, root), 0


def diff_comparison(A_B, B_A):
    for path in set(A_B.keys()) | set(B_A.keys()):
        yield path, A_B.get(path, "NA"), B_A.get(path, "NA")


def compare_paths(A, B):
    """Compare the sizes and paths.

    Args:
        A (str): first folder.
        B (str): first folder.
    Returns:
        tuple of sets
    """
    paths1 = set(iter_path(A))
    paths2 = set(iter_path(B))
    A_B = dict(paths1 - paths2)
    B_A = dict(paths2 - paths1)
    return diff_comparison(A_B, B_A)


# if not os.path.exists(result_path):
#     os.makedirs(os.dirname(result_path))

def write_2_csv(A, B, comparison, result_path):
    with open(result_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['path', A, B])
        for row in comparison:
            writer.writerow(row)
