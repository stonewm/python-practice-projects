import cairosvg
import os


def exportToPDF(fromDir, targetDir):
    print("开始转换...")

    files = os.listdir(fromDir) # get all files in the directory
    num = 0  # keep track of the number of files exported
    for fileName in files:
        path = os.path.join(fromDir, fileName)
        if os.path.isfile(path) and fileName[-3:] == "svg":
            num += 1
            fileHandle = open(path, 'rb')
            svg = fileHandle.read()
            fileHandle.close()

            exportPath = os.path.join(targetDir, fileName[:-3]+"pdf")
            exportFileHandle = open(exportPath, 'w')
            cairosvg.svg2pdf(bytestring=svg, write_to=exportPath)

            exportFileHandle.close()
            print("Export ", fileName, " -> ", exportPath)

    print("完成转换 ", num, "个文件")


if __name__ == '__main__':
    # delete files
    outputpath = "C:/FFOutput"
    files = os.listdir(outputpath)
    for f in files:
        fullname = os.path.join(outputpath, f)
        os.remove(fullname)
    
    # export svg to pdfC:\BaiduNetdiskDownload\S4F29_ZH_Col11
    exportToPDF(r"C:\BaiduNetdiskDownload\S4F29_ZH_Col11", "C:/FFOutput")
