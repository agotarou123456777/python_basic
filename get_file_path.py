import os


full_path = os.path.realpath(__file__)
DIR_PATH, FILE_NAME = os.path.split(full_path)
EXT_FILE_PATH=DIR_PATH+'/'+FILE_NAME

print("path to dir :", DIR_PATH)
print("path to file :", EXT_FILE_PATH)
print("file name :", FILE_NAME)


#特定の拡張子を持つファイルを検索
def get_files_in_dir(directory,format):
    fl = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(format):
                fl.append(os.path.join(root, file))
    return fl


jpg_files = get_files_in_dir("/home/hajime/mylib/data/CategoryFlower102/102flowers/jpg",'.jpg')
print(jpg_files)


