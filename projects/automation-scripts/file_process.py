# 批量文件处理脚本
import os
import shutil

# 设置源文件夹和目标文件夹
source_folder = r"xxxxxxxxxxxxxxxxxx"
target_folder = r"xxxxxxxxxxxxxxxxxx"

# 按文件类型分类
file_types = {
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "python": [".py"]
}

# 创建目标文件夹
for folder in file_types.keys():
    os.makedirs(os.path.join(target_folder, folder), exist_ok=True)

# 批量移动文件
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(target_folder, folder, filename))
                moved = True
                break
        if not moved:
            # 其他文件放到 "others"
            os.makedirs(os.path.join(target_folder, "others"), exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, "others", filename))

print("批量文件处理完成！")
