import os

def unzip_folder(sourcepath):
    if sourcepath[-1:] == "\\":
        files = sourcepath + "*.zip"
    else:
        files = sourcepath + "\\" + "*.zip"

    dest = sourcepath + "\\unzip\\"

    cmd = 'WinRAR.exe x {} {}'.format(files, dest)
    print(cmd)
    os.system(cmd)  


if __name__ == "__main__":
    source_folder = r"D:\test\\"
    unzip_folder(source_folder)