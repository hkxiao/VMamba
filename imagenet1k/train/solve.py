import os
import tarfile
from pathlib import Path
 
source_folder = "."  # 替换为你的源文件夹路径
target_root = "."  # 替换为你的目标文件夹路径

# 获取源文件夹下所有以.tar结尾的文件
tar_files = [file for file in os.listdir(source_folder) if file.endswith(".tar")]

# 创建目标文件夹（如果不存在）
os.makedirs(target_root, exist_ok=True)

# 循环解压每个tar文件到目标文件夹
for tar_file in tar_files:
    tar_file_path = os.path.join(source_folder, tar_file)
    with tarfile.open(tar_file_path, 'r') as tar:
        target_folder = os.path.join(target_root,tar_file[:-4])
        Path(target_folder).mkdir(parents=True)
        tar.extractall(path=target_folder)

print("解压完成")
