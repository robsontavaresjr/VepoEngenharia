import requests
import pandas as pd
import numpy as np
import datetime as dt

def getGeoEncoding(cep):

    url = 'https://maps.google.com/maps/api/geocode/json?address=' + str(cep) + '&key=AIzaSyBXF7Rr9FQe - ELRnV7rEhZMrM - soxmwW2k'
    geo = requests.get(url).json()

    return geo['results'][0]['geometry']['location']

def getPV(cep):

    geo = getGeoEncoding(cep)
    lat = str(geo['lat'])
    lng = str(geo['lng'])

    endDate = dt.datetime.today()
    startDate = endDate + dt.timedelta(days=-1080)
    endDate = endDate.strftime('%Y%m%d')
    startDate = startDate.strftime('%Y%m%d')

    url = "https://power.larc.nasa.gov/ cgi - bin / v1 / DataAccess.py? & request = execute & identifier = SinglePoint & parameters = CLRSKY_SFC_SW_DWN & " \
          "startDate =" + startDate + "& endDate =" + endDate + "  & userCommunity = SSE & tempAverage = DAILY & outputList = JSON &" \
          " lat =" + lat + " & lon =" + lng

    url = url.replace(' ', '')
    print(url)

    data = requests.get(url).json()

    data = pd.DataFrame(list(data['features'][0]['properties']['parameter']['CLRSKY_SFC_SW_DWN'].items()))
    data.columns = ['Date', 'wp']
    data = data.loc[data.wp != -999]

    return data
#
# if __name__ == '__main__':
#
#     lng = '10'
#     lat = '5'
#
#     altUrl = "https://api.solcast.com.au/pv_power/estimated_actuals?longitude=" + lng + \
#         "&latitude=" + lat + \
#         "&capacity=1000&api_key=esCMAznqMNL1Cde02ajQqIpq5Ytc3dDz&format=json"
#     cep = '22221-140'
#     data = getPV(cep)
