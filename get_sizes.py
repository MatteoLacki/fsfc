import pandas as pd
from compare_files import filepath_size

from pathlib import Path

p = Path('/home/matteo/Projects/fsfc/test/A')

x = pd.DataFrame({'files':list(p.glob('*'))})
x.to_clipboard()


df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df.to_clipboard(sep=',')