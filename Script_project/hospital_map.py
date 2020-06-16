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

def Hospital_List(window):
    data_list = []
    for code in data:
        do = code.find('sidonm')
        city = code.find('sggunm')
        name = code.find('yadmnm')
        tel = code.find('telno')
        kind = code.find('spcladmtycd')
        if kind =='A0':
            kind = "국민안심병원"
        elif kind == '97':
            kind = "코로나검사 실시기관"
        elif kind == '99':
            kind = "선별진료소 운영기관"
        data_list.append((do.text + city.text, name.text, tel.text, kind.text))

    print(data_list)

    fput = tkinter.Frame(window)
    fput.pack()
    lb1 = tkinter.Label(fput, text=" 주소 ")
    lb1.place(x=200, y=100)
    lb1.configure(foreground='greenyellow')
    iptAddr = tkinter.Entry(fput, width=20)
    iptAddr.insert(0, data_list)
    iptAddr.place(x=240, y=280)
    search = tkinter.Button(fput, text="검색", width=10, command=lambda : ())
    search.place(x=390, y=280)

    treeview = tkinter.ttk.Treeview(window, columns=["one", "two", "three", "four", "five"],
                                    displaycolum=["one", "two", "three", "four", "five"])
    treeview.column("#0", width=50, anchor="center")
    treeview.heading("#0", text=table_name[0])
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("#1", text=table_name[1])
    treeview.column("#2", width=100, anchor="center")
    treeview.heading("#2", text=table_name[2]  )
    treeview.column("#3", width=100, anchor="center")
    treeview.heading("#3", text=table_name[3])
    treeview.column("#4", width=100, anchor="center")
    treeview.heading("#4", text=table_name[4])
    for i in range(len(data_list)):
        treeview.insert('' , 'end', text=i, values=data_list[i], iid=str(i)+"번")
    treeview.place(x=10, y=150)


# def Searchinfo():
#     fput
#     # 기존 데이터 있다면 삭제
#     for row in trv.get_children():
#         trv.delete(row)
#
#     global stores
#     jData = requetJson()
#     # 데이터를 제대로 받아오지 못했다면 메세지창으로 알림
#     if type(jData) == int:
#         tkMsg.showerror("실패", "요청을 실패하였습니다.")
#         return -1
#     # print(type(jData)) # dict
#     # print info(stores)
#     cnt = 0
#     for store in jData['stores']:
#         # remain_stat : None, empty, few, some, plenty
#         # empty : 회색(0~1개)/
#         # few: 빨강색(2~29개)/some: 노랑색(30~99개)/ plenty: 녹색(100개 이상)
#         status = store.get('remain_stat')
#         if status in ["few", "some", "plenty"]:
#             # header = ["판매처","주소","재고량","입고일시","생성일시"]
#             info = (store.get('name'),
#                     store.get('addr').replace(iptAddr.get(), "")
#                     , status, store.get('stock_at')
#                     , store.get('created_at'))
#             stores.append(info)
#             cnt += 1
#             # 재고 상태에 따라 색상 변경 해줄려고 재고 상태를 태그로 달아줌
#             trv.insert('', 'end', text=cnt, values=info, tags=[status])
#             # print(stores) #추출한 데이터 확인
#     # 재고 상태별 행 색상 변경(적용이 안된다면 3.3 버그 해결부분 참고)
#     trv.tag_configure('plenty', background="green")
#     trv.tag_configure('some', background="yellow")
#     trv.tag_configure('few', background="red")







#https://map.naver.com/v5/search/도%20시%20기관명/place
#URL = 'https://map.naver.com/v5/search/'+do[0] +'%20'+city[0]+'%20'+tel[0]+'/place'
#print(data_list)
#webbrowser.open(URL)