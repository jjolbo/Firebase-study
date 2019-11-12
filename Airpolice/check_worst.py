import kFirebase
import datetime
import numpy as np

class Check_worst:
    def date_time(self):
        dt = datetime.datetime.now()
        # month = int(dt.month)
        # day = int(dt.day)
        month = 9
        day = 18
        hour = dt.hour
        min = dt.minute
        # hour = 4
        # min = 37

        min = min - (min % 5)

        return month, day, hour, min

    def find_max(self, list):
        Firebase = kFirebase.Firebase()
        # print(list)
        for idx in range(len(list)):
            if list[idx] == max(list):
                # print('findmax',idx)
                Firebase.wa_update('mode/', {
                    'auto_area': idx
                })

    def worst_air(self):
        month, day, hour, min = self.date_time()

        Firebase = kFirebase.Firebase()
        # Firebase.firebase_db()
        area = ['kitchen', 'livingroom', 'room']

        pm10_list = []
        pm25_list = []

        for i in range(3):
            pm10path = 'inside/' + area[i] + '/' + str(month) + str(day) + '/' + str(hour) + ':' + str(min) + '/' + 'pm10Value'
            pm10value = Firebase.load(pm10path)
            pm10_list.append(pm10value)

            pm25path = 'inside/' + area[i] + '/' + str(month) + str(day) + '/' + str(hour) + ':' + str(
                min) + '/' + 'pm25Value'
            pm25value = Firebase.load(pm25path)
            pm25_list.append(pm25value)

        # worst: 3, bad: 2, normal: 1, good: 0
        auto_area = [0,0,0]

        print(pm10_list)
        print(pm25_list)

        for i in range(3):
            if pm10_list[i] >= 101 or pm25_list[i] >= 51:
                auto_area[i] = 3
            elif pm10_list[i] >= 151 or pm25_list[i] >= 26:
                auto_area[i] = 2
            elif pm10_list[i] >= 31 or pm25_list[i] >= 16:
                auto_area[i] = 1
            else:
                auto_area[i] = 0

        print(auto_area)

        pm10_array = np.array(pm10_list)
        pm25_array = np.array(pm25_list)

        if auto_area.count(1) > 1 or auto_area.count(2) > 1 or auto_area.count(3) > 1:
            self.find_max(pm25_array + pm10_array)
            return

        if sum(auto_area) == 0:
            print(1)
            Firebase.wa_update('mode/', {
                'auto_area': 1
            })
        else:
            self.find_max(auto_area)


    def _main(self):
        self.worst_air()

# if __name__ == '__main__':
#     ch = Check_worst()
#     ch.worst_air()
