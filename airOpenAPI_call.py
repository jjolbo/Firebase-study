import requests
from pprint import pprint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def change_url(sidoName, pageNo, ServiceKey):
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?"
    url = url + "sidoName=" + sidoName + "&searchCondition=HOUR" + "&pageNo=" + str(pageNo) + "&numOfRows=10" + "&ServiceKey=" + ServiceKey + "&_returnType=json"

    return url

def firebase_db():
    cred = credentials.Certificate('your firebase key.json')
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'your realtime db url'
    })

def print_air_info(tmp_data):
    print('------------------------------------------------')
    print('area: ', tmp_data['cityName'])
    print('일산화탄소 농도: ', tmp_data['coValue'])
    print('미세먼지(pm10) 농도:', tmp_data['pm10Value'])
    print('초미세먼지(pm25) 농도:', tmp_data['pm25Value'])

def air_info(tmp_data):
    dataList = {
        tmp_data['cityName']: {
        'co value': tmp_data['coValue'],
        'pm10 value' : tmp_data['pm10Value'],
        'pm25 value' : tmp_data['pm25Value']
        }
    }

    return dataList


if __name__ == '__main__':
    firebase_db()

    sido = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주", "세종"]
    ServiceKey = "your service key"

    for idx in range(len(sido)):
        sidoName = sido[idx]
        pageNo = 0

        # print('서울시')
        cnt = 0
        for i in range(5):
            # print(1)
            pageNo += 1

            # print(url)
            url = change_url(sidoName, pageNo, ServiceKey)
            print(url)
            response = requests.get(url)

            if (response.status_code == 200):
                # print('ok')
                data = response.json()
                for i in range(len(data['list'])):
                    # print(3)
                    tmp_data = data['list'][i]
                    if tmp_data is None:
                        break
                    else:
                        # print_air_info(tmp_data)
                        ref = db.reference(sidoName)
                        dataList = air_info(tmp_data)
                        ref.update(dataList)
                        cnt += 1

            else:
                print("Error code: "+ response.status_code)

    # ref = db.reference(sidoName)
    # print(ref.get())
