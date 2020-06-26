from tkinter import *
from PIL import Image, ImageTk

#한글 적용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import webbrowser
import world_data
import hospital_map
import world_corona
import korea_corona
import mask



window = Tk()
window.geometry("800x500+500+200")          #창 크기
window.configure(background='aquamarine')   #배경색
window.title("Corona")                      #창 제목
window.resizable(False, False)              #화면크기조절 불가능

news ='https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty'


#def titlename():



# 국가별 확진자 현황 버튼
def WorldButton(Frame):
    world_button = Button(Frame)
    file_image = Image.open('image/지구.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    world_button.image = ImageTk.PhotoImage(file_image)
    world_button = Button(image = world_button.image, comman=lambda:Open_world_corona(Frame))
    world_button.place(x=710, y=10)

# 국내 확진자 현황 버튼
def KoreaButton(Frame):
    korea_button = Button(Frame)
    file_image = Image.open('image/한국.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    korea_button.image = ImageTk.PhotoImage(file_image)
    korea_button = Button(image = korea_button.image, comman=lambda: Open_korea_corona(Frame))
    korea_button.place(x=710, y=90)

# 국내 공적 마스크 판매 위치 및 제고 버든
def MaskButton(Frame):
    mask_button = Button(Frame)
    file_image = Image.open('image/마스크.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    mask_button.image = ImageTk.PhotoImage(file_image)
    mask_button = Button(image = mask_button.image, comman=lambda: Open_Mask(Frame))
    mask_button.place(x=710, y=170)

#국내 코로나 검진 병원 정보 버튼
def HospitalButton(Frame):
    hospital_button = Button(Frame)
    file_image = Image.open('image/병원.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    hospital_button.image = ImageTk.PhotoImage(file_image)
    hospital_button = Button(image = hospital_button.image, comman=lambda: Open_Map(Frame))
    hospital_button.place(x=710, y=250)


#뉴스 버튼 생성
def NewsButton(Frame):
    news_button =Button(Frame)
    file_image = Image.open('image/뉴스.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    news_button.image = ImageTk.PhotoImage(file_image)
    news_button = Button(image = news_button.image, command=lambda: Open_URL())
    news_button.place(x=710,y=330)

#챗봇 버튼 생성
def TelebotButton(Frame):
    telbot_button = Button(Frame)
    file_image = Image.open('image/텔레그램봇.jpg')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    telbot_button.image = ImageTk.PhotoImage(file_image)
    telbot_button = Button(image = telbot_button.image)
    telbot_button.place(x=710,y=410)

def ShowUI(Frame):
    WorldButton(Frame)
    KoreaButton(Frame)
    MaskButton(Frame)
    HospitalButton(Frame)
    NewsButton(Frame)
    TelebotButton(Frame)

def onclick(event, list):
    world_data.Print_worldMap(Frame)
#    world_data.Show_Graph(window)
    world_data.Pie_Graph(Frame)

def Open_korea_corona(Frame):
    Frame.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    korea_corona.corona(new_Frame)


def Open_world_corona(Frame):
    Frame.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    world_corona.corona(new_Frame)


# 네이버 뉴스창 열어주기
def Open_URL():
    webbrowser.open(news)


# 병원 지도 열기
def Open_Map(Frame):
    Frame.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    hospital_map.Hospital_List(new_Frame)


def Open_Mask(Frame):
    Frame.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    mask.mask(new_Frame)

ShowUI(window)
window.mainloop()