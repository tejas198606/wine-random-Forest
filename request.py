import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'fixedacidity':2.000,'volatileacidity':9.000,'citricacid':6.000,'residualsugar':2.000,'chlorides':9.000,'freesulfurdioxide':6000,
                            'totalsulfurdioxide':9.000})

print(r.json())
