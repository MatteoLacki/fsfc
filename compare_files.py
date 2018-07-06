import os

A = 'test/A'
B = 'test/B'


def rm_root(path, root):
    return path[len(root):]

def make_hashable(dir, subdir, files, root):
    dir = rm_root(dir, root)
    subdir = tuple(subdir)
    files = tuple(files)
    return dir, subdir, files

def iter_path(root):
    for dir, subdir, files in os.walk(root):
        yield make_hashable(dir, subdir, files, root)

# TODO: add file size when files are present

paths1 = set(iter_path(A))
paths2 = set(iter_path(B))

paths1
