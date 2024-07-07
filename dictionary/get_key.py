d = {'apple': 1, 'banana': 2, 'cherry': 3}
keys = d.keys()
print(keys)  # dict_keys(['apple', 'banana', 'cherry'])
d['mango'] = 4
print(keys)  # dict_keys(['apple', 'banana', 'cherry', 'mango'])

print(d["banana"])
# print(d["lemon"]) lemonはないのでエラー
