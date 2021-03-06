from tkinter import *
from PIL import Image, ImageTk
#한글 적용
from matplotlib import font_manager, rc
import os
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import webbrowser
import hospital_map
import world_corona
import korea_corona
import mask
import telegrambot

# 국가별 확진자 현황 버튼
def WorldButton(window):
    world_button = Button(window)
    file_image = Image.open('image/지구.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    world_button.image = ImageTk.PhotoImage(file_image)
    world_button = Button(image = world_button.image, comman=lambda:Open_world_corona(window))
    world_button.place(x=710, y=10)

# 국내 확진자 현황 버튼
def KoreaButton(window):
    korea_button = Button(window)
    file_image = Image.open('image/한국.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    korea_button.image = ImageTk.PhotoImage(file_image)
    korea_button = Button(image = korea_button.image, comman=lambda: Open_korea_corona(window))
    korea_button.place(x=710, y=90)

# 국내 공적 마스크 판매 위치 및 제고 버든
def MaskButton(window):
    mask_button = Button(window)
    file_image = Image.open('image/마스크.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    mask_button.image = ImageTk.PhotoImage(file_image)
    mask_button = Button(image = mask_button.image, comman=lambda: Open_Mask(window))
    mask_button.place(x=710, y=170)

#국내 코로나 검진 병원 정보 버튼
def HospitalButton(window):
    hospital_button = Button(window)
    file_image = Image.open('image/병원.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    hospital_button.image = ImageTk.PhotoImage(file_image)
    hospital_button = Button(image = hospital_button.image, comman=lambda: Open_Map(window))
    hospital_button.place(x=710, y=250)


#뉴스 버튼 생성
def NewsButton(window):
    news_button =Button(window)
    file_image = Image.open('image/뉴스.png')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    news_button.image = ImageTk.PhotoImage(file_image)
    news_button = Button(image = news_button.image, command=lambda: Open_URL())
    news_button.place(x=710,y=330)

#챗봇 버튼 생성
def TelebotButton(window):
    telbot_button = Button(window)
    file_image = Image.open('image/텔레그램봇.jpg')
    file_image = file_image.resize((60, 60), Image.ANTIALIAS)
    telbot_button.image = ImageTk.PhotoImage(file_image)
    telbot_button = Button(image = telbot_button.image, command=lambda: telbot())
    telbot_button.place(x=710,y=410)

def ShowUI(window):
    WorldButton(window)
    KoreaButton(window)
    MaskButton(window)
    HospitalButton(window)
    NewsButton(window)
    TelebotButton(window)

def Open_world_corona(window):
    window.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    world_corona.corona(new_Frame)

def Open_korea_corona(window):
    window.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    korea_corona.corona(new_Frame)

# 네이버 뉴스창 열어주기
def Open_URL():
    news = 'https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty'
    webbrowser.open(news)

# 병원 지도 열기
def Open_Map(window):
    window.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    hospital_map.Hospital_List(new_Frame)

def Open_Mask(window):
    window.destroy()
    new_Frame = Tk()
    new_Frame.geometry("800x500+500+200")  # 창 크기
    new_Frame.configure(background='aquamarine')  # 배경색
    new_Frame.title("Corona")  # 창 제목
    new_Frame.resizable(False, False)  # 화면크기조절 불가능
    ShowUI(new_Frame)
    mask.mask(new_Frame)

def telbot():
    os.startfile("telegrambot.py")

if __name__ == '__main__':
    window = Tk()
    window.geometry("800x500+500+200")  # 창 크기
    window.configure(background='aquamarine')  # 배경색
    window.title("Corona")  # 창 제목
    window.resizable(False, False)  # 화면크기조절 불가능
    korea_corona.corona(window)
    ShowUI(window)
    window.mainloop()
