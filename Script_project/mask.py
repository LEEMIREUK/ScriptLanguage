import requests as rq
import json
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as wbs
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name, size=8.3)


def mask(window):
    mask_url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"

    addr = "경기도 시흥시"
    header = ["판매처","주소","재고량","입고일시","생성일시"]
    global stores
    stores = [] # store list

    #해당 주소로 판매처 및 재고현황 정보 요청
    def requetJson():
        global addr
        addr = iptAddr.get()
        res = rq.get(mask_url, params={"address": addr})  # rq.post()

        # load json data
        return json.loads(res.content)


    def fixed_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option) if
          elm[:2] != ('!disabled', '!selected')]


    #해당 주소로 판매처 및 재고현황 정보 가져와서 표시
    def infoSearch():
        # 기존 데이터 있다면 삭제
        for row in trv.get_children():
            trv.delete(row)

        global stores
        jData = requetJson()
        cnt = 0
        for store in jData['stores']:
            status = store.get('remain_stat')
            if status in ["few", "some", "plenty"]:
                info = (store.get('name'),
                        store.get('addr').replace(iptAddr.get(), "")
                        , status, store.get('stock_at')
                        , store.get('created_at'))
                stores.append(info)
                cnt += 1
                trv.insert('', 'end', text=cnt, values=info, tags=[status])
        trv.tag_configure('plenty', background="green")
        trv.tag_configure('some', background="yellow")
        trv.tag_configure('few', background="red")


    '''
     더블클릭시 해당 판매처 위치 검색
    '''
    def OnDoubleClick(e):
      selectedItem = trv.item(trv.selection()[0])['values']
      selectedAddr = iptAddr.get()+selectedItem[1]
      googleURL = "https://www.google.com/search?ei=FLDfXv6hI4qRr7wPmbGH8A8&q="
      param = selectedAddr+" "+selectedItem[0]
      wbs.open(googleURL+param, new=1) #해당 주소로 인터넷창 팝업


    # 입력받는 곳
    lb1 = tk.Label(window, text = "주소: ",bg='aquamarine')
    lb1.place(x=215, y=120)
    lb1 = tk.Label(window, text = "마스크 검색",bg='aquamarine')
    lb1.configure(foreground='blue')
    lb1.place(x=135, y=120)
    iptAddr = tk.Entry(window,width=20)
    iptAddr.insert(0, addr)
    iptAddr.place(x=250, y=120)
    btnSearch = tk.Button(window, text="Search", width=10, command=infoSearch)
    btnSearch.place(x=400, y=117)


    #안내 문구
    lb2 = tk.Label(window, text = "few: 빨강색(2~29개)",bg='aquamarine')
    lb2.configure(foreground='red')
    lb2.place(x=20, y=390)
    lb2 = tk.Label(window, text = "some: 노랑색(30~99개)",bg='aquamarine')
    lb2.configure(foreground='orange')
    lb2.place(x=20, y=410)
    lb2 = tk.Label(window, text = "plenty: 녹색(100개 이상)",bg='aquamarine')
    lb2.configure(foreground='green')
    lb2.place(x=20, y=430)
    lb2 = tk.Label(window, text="더블클릭 시 구글에서 위치 검색",bg='aquamarine')
    lb2.place(x=20, y=450)


    trv = ttk.Treeview(window, columns=header, displaycolumns=header, padding=0)


    #트리뷰 스크롤 추가
    scrY = ttk.Scrollbar(orient='vertical', command=trv.yview)
    scrY.place(x=633, y=148, height=230)
    trv.config(yscrollcommand=scrY.set)
    trv.place(x=10, y=150)
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



    style = ttk.Style()
    style.map('Treeview', foreground=fixed_map('foreground'),
      background=fixed_map('background'))

    trv.bind("<Double-1>", OnDoubleClick)