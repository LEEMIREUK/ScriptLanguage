import requests as rq
import json
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as wbs
import tkinter.messagebox as tkMsg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"

addr = "경기도 시흥시" #default address
header = ["판매처","주소","재고량","입고일시","생성일시"]
stores = [] # store list

#해당 주소로 판매처 및 재고현황 정보 요청
def requetJson():
    global addr
    # 응답코드(status_code) 반환
    # 200: 성공, 404:  존재하지 않는 URL
    addr = iptAddr.get()
    res = rq.get(url, params={"address": addr})  # rq.post()
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
#lb1.grid(row = 0, column = 0, sticky="e")
lb1.place(x=205, y=283)
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
# ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))
# days = [1,2,3,4,5,6,7]
# graph_lab = tk.Label(window, text =("코로나 발생 현황"))
# graph_lab.pack()
#
# days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
# plt.bar(range(len(days_in_year)), days_in_year)
# plt.show()
lb2 = tk.Label(window, text="국내 코로나 현황")
lb2.place(x=200, y=10)
fig = Figure(figsize=(5, 2.4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, fInput)
canvas._tkcanvas.place(x=10, y=30)

#canvas.get_tk_widget().grid(column=0, row=1, sticky='w')



style = ttk.Style()
style.map('Treeview', foreground=fixed_map('foreground'),
  background=fixed_map('background'))

trv.bind("<Double-1>", OnDoubleClick)
window.mainloop()