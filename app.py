
VERSION = "0.0.1" # 参考https://www.geeksforgeeks.org/creating-pdf-documents-with-python/

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors



def main():
    content = "好好学习，天天向上！"
    
    filename="我的字帖.pdf"
    documentTitle = "sample"
    title = "这是一份字帖"
    subTitle = "创建一个PDF文件"
    textLines = ["好好学习，","天天向上"]
    
    pdf = canvas.Canvas(filename)
    pdf.setTitle(documentTitle)
        
    pdfmetrics.registerFont(TTFont('abc','STKAITI.TTF'))    
    
    pdf.setFont('abc',36)
    pdf.drawCentredString(300,770,title)
    
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("abc", 24)
    pdf.drawCentredString(290, 720, subTitle)
    
    pdf.line(30, 710, 550, 710)      
    text = pdf.beginText(40, 680)
    text.setFont("abc", 20)
    text.setFillColor(colors.red)
    
    for line in textLines:
        text.textLine(line)        
    pdf.drawText(text)    

    pdf.save()
        
    
    
    

if __name__=="__main__":
    main()