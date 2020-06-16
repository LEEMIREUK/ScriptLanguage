# import requests
# import folium
# import webbrowser
#
#
# response = requests.get(URL+Key+page)
# status = response.status_code
# text = response.text
#
# latitude = []
# longitude = []
# coordinate = []
# # 위도 경도 지정
# map_osm = folium.Map (location = [37.568477, 126.981611], zoom_start=17)
# # 마커 지정
# folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
# # html 파일로 저장
# #map_osm.save('osm.html')
# webbrowser.open('osm.html') # web browser에 저장된 지도 띄우기

import xml.etree.ElementTree as ET
import requests
URL = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?serviceKey='
Key ='MtLAG5t2b11STi2IYFynXQZdFRhAIW96u7RqSiFIB77ruJBarCvBhjuk7AmpF8w9pzxN2oLCAOaMx%2FaMyDJqmg%3D%3D'
page ='&pageNo=1&numOfRows=1079&spclAdmTyCd=&'

res = requests.get(URL+Key+page)
status = res.status_code
text = res.text
