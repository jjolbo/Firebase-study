import threading
import openApi_call
import weather_api
import kFirebase

# end = False

def _main(secode = 1.0):
    # global end
    # if end:
    #     return

    Firebase = kFirebase.Firebase()
    Firebase.firebase_db()

    Weather = weather_api.WeatherAPI()
    Mise = openApi_call.MiseAPI()

    Weather._main()
    Mise._main()

    # threading.Timer(second, _main, [second]).start()


if __name__ == '__main__':
    _main()
