import hashlib
from uuid import uuid4


salt = uuid4().hex
cachStorage = {}

def checkUrl(url):
    if cachStorage.get(url):
        print('Данный адрес присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cachStorage[url] = res
        print(cachStorage)


while True:
    userInput = input('Введите url: ')
    checkUrl(userInput)