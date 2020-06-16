import requests as rq
import json
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as wbs
import tkinter.messagebox as tkMsg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name, size=8.3)

mask_url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"

addr = "경기도 시흥시" #default address
header = ["판매처","주소","재고량","입고일시","생성일시"]
stores = [] # store list

#해당 주소로 판매처 및 재고현황 정보 요청
def requetJson():
    global addr
    # 응답코드(status_code) 반환
    # 200: 성공, 404:  존재하지 않는 URL
    addr = iptAddr.get()
    res = rq.get(mask_url, params={"address": addr})  # rq.post()
    print(res.status_code)
    if res.status_code == 200:
        print("[요청성공]")
    else:
        print("[알수 없는 에러:%s]\n " % res)
        return -1

    # load json data
    return json.loads(res.content)


def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if
      elm[:2] != ('!disabled', '!selected')]


#해당 주소로 판매처 및 재고현황 정보 가져와서 표시
def infoSearch():
    # 기존 데이터 있다면 삭제
    for row in trv.get_children():
        trv.delete(row)

    global stores
    jData = requetJson()
    # 데이터를 제대로 받아오지 못했다면 메세지창으로 알림
    if type(jData) == int:
        tkMsg.showerror("실패", "요청을 실패하였습니다.")
        return -1
    # print(type(jData)) # dict
    # print info(stores)
    cnt = 0
    for store in jData['stores']:
        # remain_stat : None, empty, few, some, plenty
        # empty : 회색(0~1개)/
        # few: 빨강색(2~29개)/some: 노랑색(30~99개)/ plenty: 녹색(100개 이상)
        status = store.get('remain_stat')
        if status in ["few", "some", "plenty"]:
            # header = ["판매처","주소","재고량","입고일시","생성일시"]
            info = (store.get('name'),
                    store.get('addr').replace(iptAddr.get(), "")
                    , status, store.get('stock_at')
                    , store.get('created_at'))
            stores.append(info)
            cnt += 1
            # 재고 상태에 따라 색상 변경 해줄려고 재고 상태를 태그로 달아줌
            trv.insert('', 'end', text=cnt, values=info, tags=[status])
            #print(stores) #추출한 데이터 확인
    # 재고 상태별 행 색상 변경(적용이 안된다면 3.3 버그 해결부분 참고)
    trv.tag_configure('plenty', background="green")
    trv.tag_configure('some', background="yellow")
    trv.tag_configure('few', background="red")


'''
 더블클릭시 해당 판매처 위치 검색
'''
def OnDoubleClick(e):
#treeview에서 선택된 아이템정보 가져오기
  selectedItem = trv.item(trv.selection()[0])['values']
  # 0: name, 1: addr, 2: remain (주소와 판매처 이름 합치기)
  selectedAddr = iptAddr.get()+selectedItem[1]
  # print(selectedAddr) #합친 주소정보 확인
  googleURL = "https://www.google.com/search?ei=FLDfXv6hI4qRr7wPmbGH8A8&q="
  param = selectedAddr+" "+selectedItem[0]
  print(param) # 보낼 데이터 확인
  wbs.open(googleURL+param, new=1) #해당 주소로 인터넷창 팝업


window = tk.Tk()
window.geometry("900x550")
window.title("공적 마스크 판매 현황") #창 제목


# 입력받는 곳
fInput = tk.Frame(window)
fInput.pack()
lb1 = tk.Label(fInput, text = "주소: ")
lb1.place(x=205, y=283)
lb1 = tk.Label(window, text = "마스크 검색")
lb1.configure(foreground='blue')
lb1.place(x=125, y=283)
iptAddr = tk.Entry(fInput,width=20) #주소 입력받는 인풋 위젯
iptAddr.insert(0, addr)
iptAddr.place(x=240, y=283)
btnSearch = tk.Button(fInput, text="Search", width=10, command=infoSearch)
btnSearch.place(x=390, y=280)


#안내 문구
lb2 = tk.Label(window, text = "few: 빨강색(2~29개)")
lb2.configure(foreground='red')
lb2.place(x=655, y=443)
lb2 = tk.Label(window, text = "some: 노랑색(30~99개)")
lb2.configure(foreground='orange')
lb2.place(x=655, y=463)
lb2 = tk.Label(window, text = "plenty: 녹색(100개 이상)")
lb2.configure(foreground='green')
lb2.place(x=655, y=483)
lb2 = tk.Label(window, text="더블클릭 시 구글에서 위치 검색")
lb2.place(x=655, y=513)


# 판매현황표시 --> treeview(like table)
fInput.pack(fill=tk.BOTH, expand=1)
trv = ttk.Treeview(fInput, columns=header, displaycolumns=header, padding=0)


#트리뷰 스크롤 추가
scrY = ttk.Scrollbar(orient='vertical', command=trv.yview)
scrY.place(x=633, y=313, height=230)
trv.config(yscrollcommand=scrY.set)
trv.place(x=10, y=313)
trv.columnconfigure(0, weight=1)

#데이터 header 설정
trv.column('#0', width=30, anchor="center")
trv.heading("#0", text="No.", anchor="center")
trv.column('#1', width=100) # store name
trv.heading("#1", text=header[0], anchor="center")
trv.column('#2') # addr
trv.heading('#2', text=header[1], anchor="center")
trv.column('#3', width=50) # remain_stat
trv.heading('#3', text=header[2], anchor="center")
trv.column('#4', width=120) # stock_at
trv.heading('#4', text=header[3], anchor="center")
trv.column('#5', width=120) # created_at
trv.heading('#5', text=header[4], anchor="center")

#현황 그래프 생성
now = datetime.now()
key = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
start_date = str(int((now + timedelta(days=-7)).strftime('%Y%m%d')))
end_date = now.strftime('%Y%m%d')
print(start_date, end_date)
url_korea = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey='+key+'&pageNo=1&numOfRows=10&startCreateDt='+start_date+'&endCreateDt='+end_date+'&'
request_korea = requests.get(url_korea)
soup_korea = BeautifulSoup(request_korea.content, 'html.parser')
#확진자 배열
decideCnt_korea = []
data = soup_korea.find_all('decidecnt')
for code in data:
    decideCnt_korea.append(code.text)

lb2 = tk.Label(window, text="국내 코로나 발생 현황")
lb2.place(x=190, y=5)
fig = plt.Figure(figsize=(5, 2.4), dpi=100)
ax = fig.add_subplot(1,1,1)
ax.set_ylim([0, 100])
ax.set_xlabel('day', size=10)
ax.set_ylabel('count', size=10)
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
canvas = FigureCanvasTkAgg(fig, fInput)
canvas._tkcanvas.place(x=10, y=30)


#막대그래프
lb2 = tk.Label(window, text="해외 코로나 발생 현황(단위 : 백만)")
lb2.place(x=600, y=5)
key_world = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
url_world = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?serviceKey='+key_world+'&pageNo=1&numOfRows=10&startCreateDt='+end_date +'&endCreateDt='+end_date+'&'
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
ff = Figure(figsize=(4.5,2.4), dpi=100)
xx = ff.add_subplot(111)
xx.set_ylim([50000, 2500000])
#ind = np.arange(len(datalst))
ind = [decideCnt_world[0][1], decideCnt_world[1][1], decideCnt_world[2][1], decideCnt_world[3][1],
           decideCnt_world[4][1], decideCnt_world[5][1], decideCnt_world[6][1], decideCnt_world[7][1], decideCnt_world[8][1]]
datalst = [decideCnt_world[0][0], decideCnt_world[1][0], decideCnt_world[2][0], decideCnt_world[3][0],
           decideCnt_world[4][0], decideCnt_world[5][0], decideCnt_world[6][0], decideCnt_world[7][0], decideCnt_world[8][0]]
rects1 = xx.bar(ind, datalst, 0.7)
canvas = FigureCanvasTkAgg(ff, master=fInput)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT)
canvas._tkcanvas.place(x=470, y=30)


style = ttk.Style()
style.map('Treeview', foreground=fixed_map('foreground'),
  background=fixed_map('background'))

trv.bind("<Double-1>", OnDoubleClick)
window.mainloop()