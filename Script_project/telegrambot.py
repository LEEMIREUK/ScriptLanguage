import time
import telepot
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 챗봇
token = '1238627505:AAEQPKXQg1rglXLITWyef7d5NSmbE1OGIzg'
chat_id = '1213595518'
bot = telepot.Bot(token)
now = datetime.now()

# 국외 코로나
def WorldData():
    global now
    World_Key = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
    World_URL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?serviceKey=' + World_Key + '&pageNo=1&numOfRows=10&startCreateDt=' + (now + timedelta(days=-1)).strftime('%Y%m%d') + '&endCreateDt=' + (now + timedelta(days=-1)).strftime('%Y%m%d') + '&'
    request_world = requests.get(World_URL)
    soup_world = BeautifulSoup(request_world.content, 'html.parser')
    decideCnt_world = []
    data_world = soup_world.find_all('item')
    for code in data_world:
        decide = code.find('natdefcnt')
        country = code.find('nationnm')
        decideCnt_world.append((int(decide.text), country.text))
    decideCnt_world.sort(key=lambda element: -element[0])
    return decideCnt_world

# 국내 코로나
def KoeraData():
    global now
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
    return decideCnt_korea

def CityData():
    global now
    key_world = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
    url_world = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey='+key_world+'&pageNo=1&numOfRows=10&startCreateDt='+ (now + timedelta(days=-1)).strftime('%Y%m%d') +'&endCreateDt='+(now + timedelta(days=-1)).strftime('%Y%m%d')+'&'
    request_world = requests.get(url_world)
    soup_world = BeautifulSoup(request_world.content, 'html.parser')
    decideCnt_world = []
    data_world = soup_world.find_all('item')
    for code in data_world:
        decide = code.find('defcnt')
        country = code.find('gubun')
        decideCnt_world.append((int(decide.text), country.text))
    decideCnt_world.sort(key=lambda element: -element[0])
    return decideCnt_world

def FindAddress(address):
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=" + requests.utils.unquote(address)
    response = requests.get(url)
    return json.loads(response.content)

def Divide(msg):
    ad, com = msg.split('-')
    return ad

def handle(msg):
    global now
    content_type, chat_type, chat_id = telepot.glance(msg)
    response = bot.getUpdates()
    pprint(response)
    if content_type != 'text':
        bot.sendMessage(chat_id, "텍스트로 말씀해주세요~")
        return
    # 인사
    if msg['text'].startswith('안녕'):
        bot.sendMessage(chat_id, "안녕하세요 " + msg['from']['first_name'] +"님! 무엇을 도와드릴까요??")
    # 금일 해외 코로나 확진사 수와 나라별 수
    elif ("해외" in msg['text']) and ("확진자" in msg['text']):
        bot.sendMessage(chat_id, "국외 코로나 현황에 대한 정보를 알려드리겠습니다.")
        bot.sendMessage(chat_id, "확진자가 가장 많은 나라 5곳을 알려드리겠습니다.")
        text = f'''
{1}위 {wordlist[0][1]}의 확진자 수는 {wordlist[0][0]}명
{2}위 {wordlist[1][1]}의 확진자 수는 {wordlist[1][0]}명
{3}위 {wordlist[2][1]}의 확진자 수는 {wordlist[2][0]}명
{4}위 {wordlist[3][1]}의 확진자 수는 {wordlist[3][0]}명
{5}위 {wordlist[4][1]}의 확진자 수는 {wordlist[4][0]}명
                '''
        bot.sendMessage(chat_id, text)
    # 금일 국내 코로나 확진자 수와 누적 수
    elif ("국내" in msg['text']) and ("확진자" in msg['text']):
        bot.sendMessage(chat_id, "국내 코로나 현황에 대한 정보를 알려드리겠습니다.")
        bot.sendMessage(chat_id, f"국내 코로나 확진환자는 총 {citylist[0][0]}명 입니다.")
        text2 = f'''
{1}위 {citylist[1][1]}의 확진자 수는 {citylist[0][0]}명
{2}위 {citylist[2][1]}의 확진자 수는 {citylist[1][0]}명
{3}위 {citylist[3][1]}의 확진자 수는 {citylist[2][0]}명
{4}위 {citylist[4][1]}의 확진자 수는 {citylist[3][0]}명
{5}위 {citylist[6][1]}의 확진자 수는 {citylist[6][0]}명
                '''
        bot.sendMessage(chat_id, text2)
    elif ("최근" in msg['text']) and ("확진자" in msg['text']) and ("수" in msg['text']):
        bot.sendMessage(chat_id, "최근 국내 코로나 확진자 수를 알려드리겠습니다.")
        text3 = f'''
{(int((now + timedelta(days=-6)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[0]) - int(korealist[1])}명
{(int((now + timedelta(days=-5)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[1]) - int(korealist[2])}명
{(int((now + timedelta(days=-4)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[2]) - int(korealist[3])}명
{(int((now + timedelta(days=-3)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[3]) - int(korealist[4])}명
{(int((now + timedelta(days=-2)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[4]) - int(korealist[5])}명
{(int((now + timedelta(days=-1)).strftime('%Y%m%d')) - 20200000)/100} - {int(korealist[5]) - int(korealist[6])}명
                        '''
        bot.sendMessage(chat_id, text3)
    # 마스크 현황
    elif "마스크" in msg['text']:
        Divide(msg['text'])
        bot.sendMessage(chat_id, f"{msg['text']} 공적 마스크 판매 현황에 대한 정보를 알려드리겠습니다.")
        addd = FindAddress(Divide(msg['text']))
        adress = addd['address'].split()
        ad = adress[0]+adress[1]
        temp = addd['stores']
        print(ad)
        for i in range(len(temp)):
            text4 = f'''
주소:  {temp[i]['addr']}
이름:  {temp[i]['name']}
지도:  'https://map.naver.com/v5/search/{ad}{temp[i]['name']}/place'
                '''
            bot.sendMessage(chat_id, text4)
    else:
        bot.sendMessage(chat_id, "도와줄수가 없어요... 다른 키워드를 입력해주세요\n,"
                                 "ex) 해외 확진자, 국내 확진자, 최근 확진자 수, 경기도 시흥시-마스크")

if __name__ == '__main__':
    wordlist = WorldData()
    korealist = KoeraData()
    citylist = CityData()
    bot.message_loop(handle)
    while True:
        time.sleep(10)

