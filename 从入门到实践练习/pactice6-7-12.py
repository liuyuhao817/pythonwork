# name = {
#     "first_name":"liu",
#     "last_name":"yuhao",
#     "age":21,
#     }
# names = {
#     "first_name":"liu",
#     "last_name":"ze",
#     "age":21,
#     }
# namess = {
#     "first_name":"li",
#     "last_name":"siyuan",
#     "age":21,
#     }
# # people=[namess,name,names]
# people=[]
# people.append(name)
# people.append(names)
# people.append(namess)
#
# for peoson in people:
#     mingzi = f'{peoson["first_name"].title()} {peoson["last_name"].title()}'
#     nianl=f'{peoson["age"]}'
#
#     print(mingzi,nianl)


# pets=[]
# cwqd={
#     'cwm':'xiaohua',
#     'zrm':"ming",
#     'zl':'dog'
# }
# pets.append(cwqd)
#
# cwqd={
#     'cwm':'xiaohei',
#     'zrm':"yu",
#     'zl':'cat'
# }
# pets.append(cwqd)
#
# cwqd={
#     'cwm':'xiaohua',
#     'zrm':"yang",
#     'zl':'dog'
# }
# pets.append(cwqd)
#
# for pet in pets:
#     for key,value in pet.items():
#         print(f'{key}:{value}')

# mudidi = {
#     'lsy':['xa','xm','tm'],
#     'lz':['wds','ljs','ts'],
#     'hjt':['bj','sh','tj']
# }
# for ren,mudi in mudidi.items():
#     print(f'\nzhegerenshi{ren}')
#     for mud in mudi:
#         print(f'didianshi {mud}')

cities={
    'wh':{
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes'
    },
    'sh':{
        'country': 'chi',
        'population': 6_000_000,
        'nearby mountains': 'and'
    }
}
for keys,vaules in cities.items():
    # print(f'\n这个城市是 {keys}')
    # for key,vaule in vaules.items():
    #     print(f"{key}:{vaule}")
    country=vaules['country'].title()
    population=vaules['population']
    nearby_mountains=vaules['nearby mountains']

    print(f'\n{keys} shuyu {country}')
    print(f'{population}')
    print(f'{nearby_mountains}')

