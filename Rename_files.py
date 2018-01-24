import os


def rename_files():
    # (1) get file names from a folder

    file_list = os.listdir(r"/Users/hgi/PycharmProjects/Python_course/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is" + saved_path)
    os.chdir(r"/Users/hgi/PycharmProjects/Python_course/prank")

    # (2) for each file, name filename

    for file_name in file_list:
        print("Old Name - " + file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        new_name = file_name.translate(None, "0123456789")
        print(" New Name - " + new_name);
    os.chdir(saved_path)


rename_files()