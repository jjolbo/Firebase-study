import kFirebase
import datetime

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

    def worst_air(self):
        month, day, hour, min = self.date_time()

        Firebase = kFirebase.Firebase()
        # Firebase.firebase_db()
        area = ['kitchen', 'livingroom', 'room']

        val_list = []

        for i in range(3):
            pm10path = 'inside/' + area[i] + '/' + str(month) + str(day) + '/' + str(hour) + ':' + str(min) + '/' + 'pm10Value'
            pm10value = Firebase.load(pm10path)
            val_list.append(pm10value)

        if (val_list[0] == val_list[1] or val_list[1] == val_list[2] or val_list[0] == val_list[2] or (val_list[0]==val_list[1]and val_list[1] == val_list[2])):
            val_list.clear()
            for i in range(3):
                pm25path = 'inside/' + area[i] + '/' + str(month) + str(day) + '/' + str(hour) + ':' + str(
                    min) + '/' + 'pm25Value'
                pm25value = Firebase.load(pm25path)
                val_list.append(pm25value)

        print(val_list)
        for idx in range(len(val_list)):
            if val_list[idx] == max(val_list):
                print(idx)
                Firebase.wa_update('mode/', {
                    'auto_area': idx
                })

    def _main(self):
        self.worst_air()

# if __name__ == '__main__':
#     ch = Check_worst()
#     ch.worst_air()
