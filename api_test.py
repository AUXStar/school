import requests

session = requests.session()

def get(url,json={}):
    a = session.get("http://127.0.0.1:8000"+url,json=json)
    print(a.json())
    return a
def post(url,json={}):
    a = session.post("http://127.0.0.1:8000"+url,json=json)
    print(a.json())
    return a

# post('/user/register',{'username':'njzy4688','password':'njzy4688','realname':'王靖元','id_card':'620722200804190013','phone':15393616608,'is_male':True})
post('/user/login',{'username':'njzy4688','password':'njzy4688'})

get('/oa/summary')