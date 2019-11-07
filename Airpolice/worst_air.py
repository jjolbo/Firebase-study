import kFirebase
import datetime

class Check_mise:
    def date_time(self):
        dt = datetime.datetime.now()
        month = int(dt.month)
        day = int(dt.day)
        # month = 9
        # day = 18
        hour = dt.hour
        min = dt.minute
        # hour = 4
        # min = 37

        min = min - (min % 5)

        return month, day, hour, min


    def calc_day(self):
        month, day, hour, min = self.date_time()

        Firebase = kFirebase.Firebase()
        # Firebase.firebase_db()

        area = ['kitchen', 'livingroom', 'room']

        if day < 10:
            day = '0' + str(day)
            print(day)

        d_hour = 0

        total_temp = []
        total_pm25 = []
        total_pm10 = []
        total_humid = []

        while d_hour < 24:

            pm10path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(d_hour) + '/' + 'pm10Value'
            pm10value = Firebase.load(pm10path)
            # print(pm10value)
            if pm10value is not None:
                # print(pm10value)
                total_pm10.append(pm10value)

            pm25path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(d_hour) + '/' + 'pm25Value'
            pm25value = Firebase.load(pm25path)
            if pm25value is not None:
                # print(pm25value)
                total_pm25.append(pm25value)

            temp_path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(d_hour) + '/' + 'temp'
            temp_value = Firebase.load(temp_path)
            if temp_value is not None:
                total_temp.append(temp_value)
                # print(temp_value)

            humid_path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(d_hour) + '/' + 'humid'
            humid_value = Firebase.load(humid_path)
            if humid_value is not None:
                # print(humid_value)
                total_humid.append(humid_value)

            d_hour += 1

        Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/day', {
            'pm10Value': round(float(sum(total_pm10)) / 24, 2)
        })

        Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/day', {
            'pm25Value': round(float(sum(total_pm25)) / 24, 2)
        })

        Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/day', {
            'temp': round(float(sum(total_temp)) / 24, 2)
        })

        Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/day', {
            'humid': round(float(sum(total_humid)) / 24, 2)
        })


    def calc_hour(self):

        month, day, hour, min = self.date_time()

        Firebase = kFirebase.Firebase()
        # Firebase.firebase_db()

        area = ['kitchen', 'livingroom', 'room']
        # kitchen_pm10values = []
        # kitchen_pm25values = []
        #
        # livingroom_pm10values = []
        # livingroom_pm25values = []
        #
        # room_pm10values = []
        # room_pm25values = []

        tmp_pm10 = []
        tmp_pm25 = []
        tmp_temp = []
        tmp_humid = []

        # pm10values = [kitchen_pm10values, livingroom_pm10values, room_pm10values]
        # pm25values = [kitchen_pm25values, livingroom_pm25values, room_pm25values]

        print(month)
        if day < 10:
            day = '0' + str(day)
            print(day)

        for i in range(1):
            d_hour = 0
            d_min = 0

            while d_hour < hour or d_hour == 24:
                if d_min == 60:
                    d_min = 0
                    d_hour += 1
                    # pm10values[i].append(round(sum(tmp_pm10) / 12, 2))
                    # pm25values[i].append(round(sum(tmp_pm25) / 12, 2))
                    key = d_hour -1
                    print(type(round(float(sum(tmp_temp)) /12,2)))

                    Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(key) + '/', {
                        'pm10Value': round(float(sum(tmp_pm10)) / 12, 2)
                    })

                    Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(key) + '/', {
                        'pm25Value': round(float(sum(tmp_pm25)) / 12, 2)
                    })

                    Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(key) + '/', {
                        'temp': round(float(sum(tmp_temp)) / 12, 2)
                    })

                    Firebase.wa_update('inside/' + area[1] + '/' + str(month) + str(day) + '/ave/' + str(key) + '/', {
                        'humid': round(float(sum(tmp_humid)) / 12, 2)
                    })

                    tmp_pm10.clear()
                    tmp_pm25.clear()
                    tmp_humid.clear()
                    tmp_temp.clear()

                if d_hour == hour:
                    break

                print(d_hour, d_min)


                pm10path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/' + str(d_hour) + ':' +  str(d_min) + '/' + 'pm10Value'
                pm10value = Firebase.load(pm10path)
                #print(pm10value)
                if pm10value is not None:
                    tmp_pm10.append(pm10value)

                pm25path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/' + str(d_hour) + ':' +  str(d_min) + '/' + 'pm25Value'
                pm25value = Firebase.load(pm25path)
                if pm25value is not None:
                    tmp_pm25.append(pm25value)

                temp_path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/' + str(d_hour) + ':' +  str(d_min) + '/' + 'temp'
                temp_value = Firebase.load(temp_path)
                if temp_value is not None:
                    tmp_temp.append(temp_value)
                print(temp_value)

                humid_path = 'inside/' + area[1] + '/' + str(month) + str(day) + '/' + str(d_hour) + ':' +  str(d_min) + '/' + 'humid'
                humid_value = Firebase.load(humid_path)
                if humid_value is not None:
                    tmp_humid.append(humid_value)

                d_min += 5

    def _main(self):
        # Firebase = kFirebase.Firebase()
        # Firebase.firebase_db()
        self.calc_hour()
        self.calc_day()

if __name__ == '__main__':
    ch = Check_mise()
    ch._main()
