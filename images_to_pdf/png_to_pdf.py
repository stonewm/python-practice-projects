import img2pdf
import os


def pngToPDF(fromFile, toFile):
    with open(toFile, "wb") as f:
        f.write(img2pdf.convert(fromFile))


def exportDirectory(fromDir, targetDir):
    print("开始转换...")

    files = os.listdir(fromDir) # get all files in the directory
    num = 0  # keep track of the number of files exported
    for fileName in files:
        path = os.path.join(fromDir, fileName)

        if os.path.isfile(path) and (fileName[-3:] == "png" or fileName[-3:]=="jpg"):
            num += 1

            exportPath = os.path.join(targetDir, fileName[:-3]+"pdf")
            pngToPDF(path, exportPath)
            print("Export ", fileName, " -> ", exportPath)

    print("完成转换 ", num, "个文件")

if __name__ == '__main__':
    # delete files
    outputpath = "C:/FFOutput"
    files = os.listdir(outputpath)
    for f in files:
        fullname = os.path.join(outputpath, f)
        os.remove(fullname)

    exportDirectory(r"C:\BaiduNetdiskDownload\SAPX08_EN_COL10\Converted", r"C:\FFOutput")
