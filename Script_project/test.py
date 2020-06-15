import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
key = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
start_date = str(int(now.strftime('%Y%m%d'))-7)
end_date = now.strftime('%Y%m%d')
print(start_date, end_date)
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey='+key+'&pageNo=1&numOfRows=10&startCreateDt='+start_date+'&endCreateDt='+end_date+'&'


request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

decideCnt = []
data = soup.find_all('decidecnt')

for code in data:
    decideCnt.append(code.text)

print(decideCnt)