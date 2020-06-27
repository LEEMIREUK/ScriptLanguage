import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter.ttk

URL = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?serviceKey='
Key ='MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
page ='&pageNo=1&numOfRows=1079&spclAdmTyCd=&'
table_name =["NO.", "시·도", "구·군", "이름", "전화번호", "정보"]

res = requests.get(URL+Key+page)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')

data_list = []

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
        elif kind == '97':
            kind = "코로나검사 실시기관"
        elif kind == '99':
            kind = '선별진료소 운영기관'
        data_list.append((do.text, city.text, name.text, tel.text, kind))
    print(data_list)

    # 검색
    default_search = "경기 시흥시"
    lb1 = tkinter.Label(window, width=10, text=" 주소 ")
    lb1.configure(background='aquamarine')
    lb1.place(x=50, y=103)

    global iptAddr
    iptAddr = tkinter.Entry(window, width=40)
    iptAddr.insert(0, default_search)
    iptAddr.place(x=130, y=103)
    search = tkinter.Button(window, text="검색", width=10, command=lambda: Info_List())
    search.place(x=430, y=100)

    # 목록
    global treeview
    treeview = tkinter.ttk.Treeview(window, height=15, columns=["one", "two", "three", "four", "five"],
                                    displaycolum=["one", "two", "three", "four", "five"],
                                    padding=0)
    scrY = tkinter.Scrollbar(orient='vertical', command=treeview.yview)
    scrY.place(x=675, y=151, height=325)
    treeview.place(x=10, y=150)
    treeview.columnconfigure(0, weight=1)

    treeview.column("#0", width=50, anchor="center")
    treeview.heading("#0", text=table_name[0])
    treeview.column("#1", width=50, anchor="center")
    treeview.heading("#1", text=table_name[1])
    treeview.column("#2", width=50, anchor="center")
    treeview.heading("#2", text=table_name[2])
    treeview.column("#3", width=230, anchor="center")
    treeview.heading("#3", text=table_name[3])
    treeview.column("#4", width=150, anchor="center")
    treeview.heading("#4", text=table_name[4])
    treeview.column("#5", width=150, anchor="center")
    treeview.heading("#5", text=table_name[5])
    for i in range(len(data_list)):
        treeview.insert('', 'end', text=i+1, values=data_list[i])

    treeview.bind("<Double-1>", DoubleClick)

def DoubleClick(event):
    get_do = treeview.item(treeview.selection()[0])['values'][0]
    get_si = treeview.item(treeview.selection()[0])['values'][1]
    get_name = treeview.item(treeview.selection()[0])['values'][2]
    print(get_do)
    print(get_si)
    print(get_name)
    #https://map.naver.com/v5/search/도%20시%20기관명/place
    URL = 'https://map.naver.com/v5/search/'+get_do+'%20'+get_si+'%20'+get_name+'/place'
    webbrowser.open(URL)

def Info_List():
    for row in treeview.get_children():
        treeview.delete(row)

    print(data_list)



