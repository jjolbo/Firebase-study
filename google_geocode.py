import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import trans
import time

def get_address(country, lat, lng, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json?language=%s&latlng=%f,%f&key=%s" % (country, lat, lng, api_key)
    r = requests.get(url).json()

    new_full_adr = r['results'][1]['formatted_address']
    old_full_adr = r['results'][0]['formatted_address']

    return new_full_adr

def firebase_db():
    cred = credentials.Certificate('key.json)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://********.firebaseio.com/'
    })

def load_coordinate():
    firebase_db()

    ref = db.reference('area/latitude')
    latitude = ref.get()
    ref = db.reference('area/longitude')
    longitude = ref.get()

    return latitude, longitude

def trans_coordinate(latitude, longitude):
    # print(latitude, longitude)
    Trans = trans.Trans()
    x, y = Trans.mapToGrid(latitude, longitude)

    return x, y

def update_temp(temp, humid):

    ref = db.reference('area')
    ref.update({
        'temp': temp,
        'humid': humid
                })

def update_address(address):

    ref = db.reference('area')
    ref.update({'now_location': address})


if __name__ == '__main__':

    latitude, longitude = load_coordinate()
    x, y = trans_coordinate(latitude,longitude)

    address = get_address('ko', latitude, longitude, "google_api")
    update_address(address)
    # print(address)

    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?"
    ServiceKey = "ServiceKey= service key"
    today = time.localtime()

    year = str(today.tm_year)
    day = str(today.tm_mday)
    mon = ''
    time = str(today.tm_hour)
    if today.tm_mon < 10:
        mon = "0" + str(today.tm_mon)
    else:
        mon = str(today.tm_mon)

    base_date = "&base_date=" + str(year) + str(mon) + str(day)
    base_time = "&base_time=" + str(int(time) - 1) + "30"
    nx = "&nx=" + str(x)
    ny = "&ny=" + str(y)
    url = url + ServiceKey + base_date + base_time + nx + ny + "&pageNo=1" + "&numOfRows=10&_type=json"

    # print(url)

    response = requests.get(url)

    if response.status_code == 200:
        # print("ok")
        data = response.json()
        tmp_data = data['response']['body']['items']['item']
        # print(tmp_data)
        # print()
        temp = 0
        humid = 0

        if tmp_data[3]["category"] == "T1H":
            print('온도: ', tmp_data[3]['obsrValue'], '℃')
            temp = int(tmp_data[3]['obsrValue'])

        if tmp_data[1]["category"] == "REH":
            print('습도: ', tmp_data[1]['obsrValue'], '%')
            humid = int(tmp_data[1]['obsrValue'])

        update_temp(temp, humid)
        pass

    else:
        print("Error code: " + response.status_code)
