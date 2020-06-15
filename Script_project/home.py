from tkinter import *
from tkinter import font
from tkinter import colorchooser
from PIL import Image, ImageTk
import world_data


window = Tk()
window.geometry("1000x600+500+200")          #창 크기
window.configure(background='snow')          #배경색
window.title("Corona")                       #창 제목

#def titlename():



# 국가별 확진자 현황 버튼
def listbutton1():
    #TempFont = font.Font(window, size=20, weiht = 'bold', family ='Consolas')
#    lb1 = Button(window, text="문구 정하기1", width=25, height=5, command=lambda: world_data.Print_worldMap(window))
    lb1 = Button(window, text="문구 정하기1", width=25, height=5, command=lambda: lb1.pack_forget())
    lb1.place(x=800, y=120)
    lb1['bg'] = '#cffed1'
    lb1['fg'] = '#2924ee'

# 국내 확진자 현황 버튼
def listbutton2():
    lb2 = Button(window, text="문구 정하기2", width=25, height=5)
    lb2.place(x=800, y=240)
    lb2['bg'] = '#cffed1'

# 국내 공적 마스크 판매 위치 및 제고 버든
def listbutton3():
    lb3 = Button(window, text="문구 정하기3", width=25, height=5)
    lb3.place(x=800, y=360)
    lb3['bg'] = '#cffed1'

#국내 코로나 검진 병원 정보 버튼
def listbutton4():
    lb4 = Button(window, text="문구 정하기4", width=25, height=5)
    lb4.place(x=800, y=480)
    lb4['bg'] = '#cffed1'


#뉴스 버튼 생성
def NewsButton():
    news_Button =Button(window)
    file_image = Image.open('image/뉴스.png')
    file_image = file_image.resize((80, 80), Image.ANTIALIAS)
    news_Button.image = ImageTk.PhotoImage(file_image)
    news_Button = Button(image = news_Button.image)
    news_Button.place(x=800,y=10)

#챗봇 버튼 생성
def TelebotButton():
    telbot_Button = Button(window)
    file_image = Image.open('image/텔레그램봇.jpg')
    file_image = file_image.resize((80, 80), Image.ANTIALIAS)
    telbot_Button.image = ImageTk.PhotoImage(file_image)
    telbot_Button = Button(image = telbot_Button.image)
    telbot_Button.place(x=900,y=10)

def ShowUI():
    listbutton1()
    listbutton2()
    listbutton3()
    listbutton4()
    NewsButton()
    TelebotButton()

def onclick(event):
    world_data.Print_worldMap(window)
#    world_data.Show_Graph(window)
    world_data.Show_PieGraph(window)




ShowUI()
window.mainloop()