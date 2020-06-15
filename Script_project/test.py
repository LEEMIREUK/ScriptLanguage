from urllib.request import urlopen
from urllib.parse import urlencode,unquote,quote_plus
import urllib
import json
from datetime import datetime

now = datetime.now()
key = 'MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
start_date = str(int(now.strftime('%Y%m%d'))-7)
end_date = now.strftime('%Y%m%d')
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey='+key+'&pageNo=1&numOfRows=10&startCreateDt='+start_date+'&endCreateDt='+end_date+'&'

# queryParams = '?' + urlencode({ quote_plus('servicekey') : 'YourServiceKey',
#     quote_plus('LAYERS') : 'frejaywalking',
#     quote_plus('FORMAT') : 'image/png',
#     quote_plus('TRANSPARENT') : 'true',
#     quote_plus('SERVICE') : 'WMS',
#     quote_plus('VERSION') : '1.1.1',
#     quote_plus('REQUEST') : 'GetMap',
#     quote_plus('SRS') : 'EPSG:900913',
#     quote_plus('BBOX') : '14142684.718103,4505504.1936344,14147576.687913,4510396.1634438',
#     quote_plus('width') : '2024',
#     quote_plus('height') : '1838',
#     quote_plus('srs') : 'EPSG:900913',
#     quote_plus('searchYearCd') : '2015052',
#     quote_plus('siDo') : '11',
#     quote_plus('guGun') : '320' })

request = urllib.request.Request(url)
jsonData=json.loads(request)

print ('Your Request:\n'+url)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print ("\nResult:")
print (response_body)
print ("\nDataType of Result Data:")
print (type(response_body))

while True:
    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        nTotal = jsonData['response']['body']['totalCount']

        if nTotal == 0:
            break

        # for item in jsonData['response']['body']['items']['item']:
        #     getTourPointData(item, yyyymm, jsonResult)
        #
        # nPage = math.ceil(nTotal / 100)
        # if (nPagenum == nPage):
        #     break
        #
        # nPagenum += 1

    else:
        break