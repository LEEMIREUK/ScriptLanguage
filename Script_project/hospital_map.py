import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import *
import tkinter.ttk

URL = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?serviceKey='
Key ='MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
page ='&pageNo=1&numOfRows=1079&spclAdmTyCd=&'
table_name =["NO.", "주소", "이름", "전화번호", "정보"]

res = requests.get(URL+Key+page)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')

data_list = []
global treeview

def Hospital_List(window):
    global data_list
    for code in data:
        do = code.find('sidonm')
        city = code.find('sggunm')
        name = code.find('yadmnm')
        tel = code.find('telno')
        kind = str((code.find('spcladmtycd')).string.strip())
        if kind == 'A0':
            kind = '국민안심병원'
        if kind == '97':
            kind = '코로나검사 실시기관'
        elif kind == '99':
            kind = '선별진료소 운영기관'
        data_list.append((do.text + city.text, name.text, tel.text, kind))
    print(data_list)

    # 검색
    default_search = "경기 시흥시"
    lb1 = tkinter.Label(window, width=10, text=" 주소 ")
    lb1.configure(background='aquamarine')
    lb1.place(x=50, y=103)
    iptAddr = tkinter.Entry(window, width=40)
    iptAddr.insert(0, default_search)
    iptAddr.place(x=130, y=103)
    search = tkinter.Button(window, text="검색", width=10, command=lambda :Info_List(treeview))
    search.place(x=430, y=100)

    # 목록
    treeview = tkinter.ttk.Treeview(window, height=15, columns=["one", "two", "three", "four"],
                                    displaycolum=["one", "two", "three", "four"],
                                    padding=0)
    scrY = tkinter.Scrollbar(orient='vertical', command=treeview.yview)
    scrY.place(x=675, y=151, height=250)
    treeview.place(x=10, y=150)
    treeview.columnconfigure(0, weight=1)

    treeview.column("#0", width=50, anchor="center")
    treeview.heading("#0", text=table_name[0])
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("#1", text=table_name[1])
    treeview.column("#2", width=230, anchor="center")
    treeview.heading("#2", text=table_name[2])
    treeview.column("#3", width=150, anchor="center")
    treeview.heading("#3", text=table_name[3])
    treeview.column("#4", width=150, anchor="center")
    treeview.heading("#4", text=table_name[4])
    for i in range(len(data_list)):
        treeview.insert('', 'end', text=i+1, values=data_list[i])

    treeview.tag_bind()

def DoubleClick(event):
    selectlist = treeview.item(treeview.selectiono()[0])

    #https://map.naver.com/v5/search/도%20시%20기관명/place
    #URL = 'https://map.naver.com/v5/search/'+[0] +'%20'+city[0]+'%20'+tel[0]+'/place'
    print(data_list)
    webbrowser.open(URL)

def Info_List(event):
    for row in treeview.get_children():
        treeview.delete(row)

    print(data_list)



