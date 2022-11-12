import os
import re

path = 'I:\\SCHOOL\\opencv\\Cycle-IR-master\\RetargetMeAll\\0.75'
all_files_path = []
for root, dirs, files in os.walk(path, topdown=False):
    if len(files) > 0:
        each_folder_files = [os.path.join(root,files[0])]
        all_files_path.extend(each_folder_files)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "0.75", "..", "")
print(data_dir)
for i in all_files_path:
    print(i)
    file = re.sub('\\\\', '/', i)
    print(file)
