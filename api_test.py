import requests

session = requests.session()

def get(url,json):
    return session.get("http://127.0.0.1:8000"+url,json=json)
def post(url,json):
    return session.post("http://127.0.0.1:8000"+url,json=json)

post('/user/register',{'username':'njzy4688','password':'njzy4688','realname':'王靖元','id_card':'620722200804190013','phone':15393616608})
# post('/user/login',{'login':'njzy4688','password':'njzy4688'})
