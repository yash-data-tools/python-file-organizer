import os

def sort(folder_name , file_ext):
    if  not os.path.exists(folder_name):
        os.makedirs(folder_name)

    cur_dir = os.getcwd()
    dest_path = os.path.join(cur_dir, folder_name)

    files = os.listdir()
    for items in files:
        if(items == os.path.basename(__file__)):
            continue
        if not os.path.isdir(items):
            filename, extension = os.path.splitext(items)
            if(extension == file_ext):
                os.rename(f"{cur_dir}/{items}", f"{dest_path}/{items}")


def check():
    while True:
        ask_folder = input("Enter the  folder name you want: ")
        ask_ext = input("Enter the extension name you want to sort(example(.txt)): ")
        if not ask_ext.startswith("."):
            print("Please, start the extension name with fullstop. Example = .txt")
            continue
            
        sort(ask_folder, ask_ext)
        rerun = input("Are you done sorting: (y/n) ").lower()
        if rerun == "y":
            print("Sorting done")
            break



check()


