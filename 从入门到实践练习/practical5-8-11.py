# names=['admin','lyh','lsy','lz','hjt']
#
# if names:
#
#     for name in names:
#         if name == 'admin':
#             print('hello admin,Enjoy your meal')
#         else:
#             print(f'hello {name},welcome')
# else:
#     print('we need to find some users')
#
# current_users=['admin','lyh','lsy','lz','hjt']
# nem_users=['admin','lbj','hz','lj','hjt']
#
# current_users_low=[user.lower() for user in current_users]
#
# for nem_user in nem_users:
#     if  nem_user in current_users_low:
#         print(f'cimingziyiweishiyong {nem_user}')
#     else:
#         print(f'gaimingziweibeishiyong {nem_user}')


shuzis = list(range(1,10))
print(shuzis)
for shuzi in shuzis:
    if shuzi == 1:
        print(f"{shuzi}st")
    elif shuzi == 2:
        print(f"{shuzi}nd")
    elif shuzi == 3:
        print(f"{shuzi}rd")
    else:
        print(f"{shuzi}th")
