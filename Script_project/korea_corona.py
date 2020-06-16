import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name, size=8.3)


def corona(window):
    #현황 그래프 생성
    now = datetime.now()
    key = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
    start_date = str(int((now + timedelta(days=-7)).strftime('%Y%m%d')))
    end_date = now.strftime('%Y%m%d')
    url_korea = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey='+key+'&pageNo=1&numOfRows=10&startCreateDt='+start_date+'&endCreateDt='+end_date+'&'
    request_korea = requests.get(url_korea)
    soup_korea = BeautifulSoup(request_korea.content, 'html.parser')
    #확진자 배열
    decideCnt_korea = []
    data = soup_korea.find_all('decidecnt')
    for code in data:
        decideCnt_korea.append(code.text)
    lb2 = tk.Label(window, text="국내 코로나 발생 현황", bg='aquamarine', font=20)
    lb2.place(x=220, y=40)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig.patch.set_facecolor('aquamarine')
    ax.set_ylim([0, 100])
    ax.set_xlabel('날짜', size=10)
    ax.set_ylabel('확진자수', size=10)
    x=np.array([round((int((now + timedelta(days=-6)).strftime('%Y%m%d')) - 20200000)/100, 2),
                round((int((now + timedelta(days=-5)).strftime('%Y%m%d')) - 20200000)/100, 2),
                round((int((now + timedelta(days=-4)).strftime('%Y%m%d')) - 20200000)/100, 2),
                round((int((now + timedelta(days=-3)).strftime('%Y%m%d')) - 20200000)/100, 2),
                round((int((now + timedelta(days=-2)).strftime('%Y%m%d')) - 20200000)/100, 2),
                round((int((now + timedelta(days=-1)).strftime('%Y%m%d')) - 20200000)/100, 2)])
    y=np.array([int(decideCnt_korea[0]) - int(decideCnt_korea[1]),
                int(decideCnt_korea[1]) - int(decideCnt_korea[2]),
                int(decideCnt_korea[2]) - int(decideCnt_korea[3]),
                int(decideCnt_korea[3]) - int(decideCnt_korea[4]),
                int(decideCnt_korea[4]) - int(decideCnt_korea[5]),
                int(decideCnt_korea[5]) - int(decideCnt_korea[6])])
    ax.plot(x,y,marker='o')
    canvas = FigureCanvasTkAgg(fig, window)
    canvas._tkcanvas.place(x=50, y=65)
