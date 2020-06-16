import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
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
    fig = plt.Figure(figsize=(5, 2.4), dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig.patch.set_facecolor('aquamarine')
    ax.set_ylim([0, 100])
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
    canvas._tkcanvas.place(x=100, y=10)
    lb2 = tk.Label(window, text="국내 코로나 발생 현황", bg='aquamarine', font=8)
    lb2.place(x=270, y=15)

    #도시별 현황
    key_world = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
    url_world = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey='+key_world+'&pageNo=1&numOfRows=10&startCreateDt='+ (now + timedelta(days=-1)).strftime('%Y%m%d') +'&endCreateDt='+(now + timedelta(days=-1)).strftime('%Y%m%d')+'&'
    request_world = requests.get(url_world)
    soup_world = BeautifulSoup(request_world.content, 'html.parser')
    decideCnt_world = []
    #데이터 넣기
    data_world = soup_world.find_all('item')
    for code in data_world:
        decide = code.find('defcnt')
        country = code.find('gubun')
        decideCnt_world.append((int(decide.text), country.text))
    #확진자 많은 순서대로 정렬
    decideCnt_world.sort(key=lambda element : -element[0])
    ff = Figure(figsize=(5,2.4), dpi=100)
    xx = ff.add_subplot(111)
    ff.patch.set_facecolor('aquamarine')
    xx.set_ylim([10, 7000])
    ind = [decideCnt_world[1][1], decideCnt_world[2][1], decideCnt_world[3][1], decideCnt_world[4][1], decideCnt_world[5][1], decideCnt_world[6][1],
           decideCnt_world[7][1], decideCnt_world[8][1], decideCnt_world[9][1], decideCnt_world[10][1], decideCnt_world[11][1], decideCnt_world[12][1]]
    datalst = [decideCnt_world[1][0], decideCnt_world[2][0], decideCnt_world[3][0], decideCnt_world[4][0], decideCnt_world[5][0], decideCnt_world[6][0],
               decideCnt_world[7][0], decideCnt_world[8][0], decideCnt_world[9][0], decideCnt_world[10][0], decideCnt_world[11][0], decideCnt_world[12][0]]
    rects1 = xx.bar(ind, datalst, 0.7)
    canvas = FigureCanvasTkAgg(ff, master=window)
    canvas.get_tk_widget().pack(side=tk.RIGHT)
    canvas._tkcanvas.place(x=100, y=255)
    lb2 = tk.Label(window, text="국내 시,도별 코로나 발생 현황", bg='aquamarine', font=8)
    lb2.place(x=230, y=255)
