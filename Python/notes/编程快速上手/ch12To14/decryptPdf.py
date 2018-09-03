import os
import PyPDF2
# 第二个功能 PDF 解密部分
pdffiles = []
for folder, sub, file in os.walk('F:\\PycharmProjects\\编程快速上手\\ch12To14'):
    for pdffile in file:
        if pdffile.endswith('.pdf'):
            pdffiles.append(pdffile)

password = input('请输入解密口令：')
for originpdf in pdffiles:
    pdf = open(originpdf, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdf)
    if pdfreader.isEncrypted:   # 判断加密文件是否被加密
        if pdfreader.decrypt(password):
            print('%s解密成功！' % pdfreader)
            pdfwriter = PyPDF2.PdfFileWriter
            for pagenum in range(0, pdfreader.numPages):
                pdfwriter.addPage(pdfreader.getPage(pagenum))

            resultpdf = open(originpdf.split('.')[0] + '_decrypted.pdf', 'wb')  # 写入到结果文件胡总
            pdfwriter.write(resultpdf)
            resultpdf.close()
        else:
            print('解密口令不对！')
