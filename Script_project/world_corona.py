import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name, size=8.3)


#window = tk.Tk()
#window.geometry("900x550")
#window.title("공적 마스크 판매 현황") #창 제목

def corona(window):
    #현황 그래프 생성
    now = datetime.now()
    #막대그래프
    lb2 = tk.Label(window, text="해외 코로나 발생 현황(단위 : 백만)", bg='aquamarine', font=20)
    lb2.place(x=180, y=40)
    key_world = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
    url_world = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?serviceKey='+key_world+'&pageNo=1&numOfRows=10&startCreateDt='+ (now + timedelta(days=-1)).strftime('%Y%m%d') +'&endCreateDt='+(now + timedelta(days=-1)).strftime('%Y%m%d')+'&'
    request_world = requests.get(url_world)
    soup_world = BeautifulSoup(request_world.content, 'html.parser')
    decideCnt_world = []
    #데이터 넣기
    data_world = soup_world.find_all('item')
    for code in data_world:
        decide = code.find('natdefcnt')
        country = code.find('nationnm')
        decideCnt_world.append((int(decide.text), country.text))
    #확진자 많은 순서대로 정렬
    decideCnt_world.sort(key=lambda element : -element[0])
    ff = Figure(figsize=(5,4), dpi=100)
    xx = ff.add_subplot(111)
    ff.patch.set_facecolor('aquamarine')
    xx.set_ylim([50000, 2500000])
    ind = [decideCnt_world[0][1], decideCnt_world[1][1], decideCnt_world[2][1], decideCnt_world[3][1],
               decideCnt_world[4][1], decideCnt_world[5][1], decideCnt_world[6][1], decideCnt_world[7][1], decideCnt_world[8][1]]
    datalst = [decideCnt_world[0][0], decideCnt_world[1][0], decideCnt_world[2][0], decideCnt_world[3][0],
               decideCnt_world[4][0], decideCnt_world[5][0], decideCnt_world[6][0], decideCnt_world[7][0], decideCnt_world[8][0]]
    rects1 = xx.bar(ind, datalst, 0.7)
    canvas = FigureCanvasTkAgg(ff, master=window)
    canvas.get_tk_widget().pack(side=tk.RIGHT)
    canvas._tkcanvas.place(x=50, y=65)

#window.mainloop()