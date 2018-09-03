import os
import PyPDF2
# 第一个功能PDF 加密部分
pdffiles = []
# os.walk 遍历 pycharm 文件夹
for folder, sub, file in os.walk('F:\\PycharmProjects\\编程快速上手\\ch12To14'):
    for pdffile in file:    #文件中的每一个文件
        if pdffile.endswith('.pdf'):
            pdffiles.append(pdffile)

password = input('请输入加密口令：')
for originpdf in pdffiles:
    pdf = open(originpdf, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdf)
    if pdfreader.isEncrypted != True:   # 同之前操作加密的 PDF 区分开
        pdfwriter = PyPDF2.PdfFileWriter()
        for pagenum in range(0, pdfreader.numPages):    # PDF复制
            pdfwriter.addPage(pdfreader.getPage(pagenum))
        pdfwriter.encrypt(password)
        resultpdf = open(originpdf.split('.')[0]+'_encrypted.pdf', 'wb')
        pdfwriter.write(resultpdf)
        resultpdf.close()
    if pdfreader.isEncrypted:   # 判断加密文件是否被加密
        if pdfreader.decrypt(password):
            print('%s被成功加密!' % pdfreader)