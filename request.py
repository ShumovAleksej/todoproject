import requests
#
# result = requests.get('http://192.168.0.16:8080/change_todo',
#                       params={'id_todo': 3, 'text_todo': 'Vasya poshel v magazin'},
#                       headers={'Accept': 'uguuu'}
#                       )
result = requests.post('https://httpbin.org/post', json={'key':'value'})
result2 = requests.post('https://httpbin.org/post', data={'key':'value'})
result.encoding = 'utf-8'
# print(result.status_code)
# print(result.text)
print(result.request.headers)
print(result2.request.headers)