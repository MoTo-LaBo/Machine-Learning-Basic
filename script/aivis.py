from glob import glob
from pathlib import Path
import os
import re
import numpy as np

# ---------- rename function ----------

def rename_func(p, idx: int, str1, str2):
    sub_p = list(p.iterdir())[idx] # subpath　rename したい folder　選択
    tf = list(sub_p.glob('*'))     # target_folder　内の file path取得
    for f in tf[1:]:                   # for文で元の path を使用して振り分けと　rename　を同時に行う
        _, n = os.path.split(f)    # split で folder, fileに分ける
        r = n.replace(str1, str2)  # str1 削除したい文字列　/ str2 代入したい文字列
        os.rename(f, r)
    return


# ---------- rename function number ----------

def rename_func_num(p, idx: int, str1, str2):
    sub_p = list(p.iterdir())[idx] # subpath　rename したい folder　選択
    tf = list(sub_p.glob('*'))     # target_folder　内の file path取得
    for f in tf[1:]:                   # for文で元の path を使用して振り分けと　rename　を同時に行う
        _, n = os.path.split(f)    # split で folder, fileに分ける
        r = re.sub(str1, str2, n)  # str1 削除したい数字　/ str2 代入したい文字列
        os.rename(f, r)
    return