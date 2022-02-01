import hashlib
from uuid import uuid4


salt = uuid4().hex
cach_storage = {}

def check_url(url):
    if cach_storage.get(url):
        print('Данный адрес присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cach_storage[url] = res
        print(cach_storage)


while True:
    user_input = input('Введите url: ')
    check_url(user_input)