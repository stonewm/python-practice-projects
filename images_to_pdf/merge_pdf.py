import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def mergePDF(filepath, outfile):
    output = PdfFileWriter()
    outputPages = 0
    pdfFiles = os.listdir(filepath)

    for pdfFile in pdfFiles:
        fullpath = os.path.join(filepath, pdfFile)
        inputStream = PdfFileReader(open(fullpath, "rb"))

        pageCount = inputStream.getNumPages()
        outputPages += pageCount

        for pageIdx in range(0, pageCount):
            output.addPage(inputStream.getPage(pageIdx))

    outPath = os.path.join(filepath, outfile)
    outputStream = open(outPath, "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == '__main__':
    file_dir = r'C:\BaiduNetdiskDownload\BC404_EN_COL15\Converted'
    out = u"out.pdf"
    mergePDF(file_dir, out)
    print("Finished")
