""""Write a script that receives a directory as argument and creates a JSON file with data about all the files in
that directory. For each file, the following information will be displayed: file_name, md5_file, sha256_file,
size_file (in bytes), time when the file was created (human-readable) and the absolute path to the file. """
import hashlib
import json
import os
import datetime


def display_info(dir_path):
    files_dict = dict()
    for file in os.listdir(dir_path):
        filename = os.path.basename(file)
        file_size = os.path.getsize(file)
        creation_time = str(datetime.datetime.fromtimestamp(os.path.getctime(file)))
        absolute_path = os.path.abspath(file)
        m1 = hashlib.md5()
        m1.update(bytes(file, encoding='utf-8'))
        md5_file = m1.hexdigest()

        m2 = hashlib.sha256()
        m2.update(bytes(file, encoding='utf-8'))
        sha256_file = m2.hexdigest()
        file_dict = {
            "filename": filename,
            "md5_file": md5_file,
            "sha256_file": sha256_file,
            "file_size": file_size,
            "creation_time": creation_time,
            "absolute_path": absolute_path
        }

        files_dict[file] = file_dict
    json_content = json.dumps(files_dict)
    f = open("json_file.txt", "w")
    f.write(json_content)
    f.close()


if __name__ == '__main__':
    display_info("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab7")
