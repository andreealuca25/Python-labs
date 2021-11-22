""""Write a function that receives two parameters: a_path and ext. The script will add all files from the a_path
folder that have the extension ext to a zip archive named the.zip. """
import os
import zipfile


def add_to_zip(a_path, ext):
    z = zipfile.ZipFile("new_archive.zip", "w", zipfile.ZIP_DEFLATED)
    for file in os.listdir(a_path):
        extension = os.path.splitext(file)[1]
        if extension == ext:
            z.write(file)
    z.close()



add_to_zip("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab7", ".py")
