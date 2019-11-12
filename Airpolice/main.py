import threading
import openApi_call
import weather_api
import kFirebase
import worst_air
import check_worst
# end = False

def _outside(second = 1800.0):
    Weather = weather_api.WeatherAPI()
    Mise = openApi_call.MiseAPI()

    Weather._main()
    Mise._main()

    threading.Timer(second, _outside, [second]).start()

def _inside(second=3.0):
    Check_mise = worst_air.Check_mise()
    Check_worst = check_worst.Check_worst()

    # Check_mise._main()
    Check_worst._main()

    threading.Timer(second, _inside, [second]).start()


if __name__ == '__main__':
    Firebase = kFirebase.Firebase()
    Firebase.firebase_db()

    _outside()
    _inside()
