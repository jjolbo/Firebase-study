# https://gist.github.com/fronteer-kr/14d7f779d52a21ac2f16
import math

class Trans:

    NX = 149  ## X축 격자점 수
    NY = 253  ## Y축 격자점 수

    Re = 6371.00877  ##  지도반경
    grid = 5.0  ##  격자간격 (km)
    slat1 = 30.0  ##  표준위도 1
    slat2 = 60.0  ##  표준위도 2
    olon = 126.0  ##  기준점 경도
    olat = 38.0  ##  기준점 위도
    xo = 210 / grid  ##  기준점 X좌표
    yo = 675 / grid  ##  기준점 Y좌표
    first = 0

    if first == 0:
        PI = math.asin(1.0) * 2.0
        DEGRAD = PI / 180.0
        RADDEG = 180.0 / PI

        re = Re / grid
        slat1 = slat1 * DEGRAD
        slat2 = slat2 * DEGRAD
        olon = olon * DEGRAD
        olat = olat * DEGRAD

        sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
        sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
        # print(sn)
        sf = math.tan(PI * 0.25 + slat1 * 0.5)
        sf = math.pow(sf, sn) * math.cos(slat1) / sn
        # print(sf)
        ro = math.tan(PI * 0.25 + olat * 0.5)
        ro = re * sf / math.pow(ro, sn)
        # print(ro)
        first = 1


    def mapToGrid(self, lat, lon, code = 0 ):
        ra = math.tan(self.PI * 0.25 + lat * self.DEGRAD * 0.5)
        ra = self.re * self.sf / pow(ra, self.sn)
        theta = lon * self.DEGRAD - self.olon
        if theta > self.PI :
            theta -= 2.0 * self.PI
        if theta < -self.PI :
            theta += 2.0 * self.PI
        theta *= self.sn
        x = (ra * math.sin(theta)) + self.xo
        y = (self.ro - ra * math.cos(theta)) + self.yo
        x = int(x + 1.5)
        y = int(y + 1.5)
        return x, y

    def gridToMap(self, x, y, code = 1):
        x = x - 1
        y = y - 1
        xn = x - self.xo
        yn = self.ro - y + self.yo
        ra = math.sqrt(xn * xn + yn * yn)
        if self.sn < 0.0 :
            ra = -ra
        alat = math.pow((self.re * self.sf / ra), (1.0 / self.sn))
        alat = 2.0 * math.atan(alat) - self.PI * 0.5
        if math.fabs(xn) <= 0.0 :
            theta = 0.0
        else :
            if math.fabs(yn) <= 0.0 :
                theta = self.PI * 0.5
                if xn < 0.0 :
                    theta = -theta
            else :
                theta = math.atan2(xn, yn)
        alon = theta / self.sn + self.olon
        lat = alat * self.RADDEG
        lon = alon * self.RADDEG

        return lat, lon
