# peiliaobiao='adsada,fafsfa,adsasfas,adasfas'
# print(peiliaobiao)
#
# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "
#
# while True:
#     peiliao=input(prompt)
#     if peiliao != "quit":
#         print(f'ning tian jia le {peiliao} dao pizza zhong')
#     else:
#         break

prompt ="\nning ke yi shu ru 'quit' tui chu"
prompt +='\nqing shu ru ni de nian ling: '

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        message = int(message)
        if message  < 3 :
            print('bu shou qu ren he fei yong')
        elif 3 <= message < 12:
            print('ning xu yao jiao na 10 meiyuan')
        elif message >= 12 :
            print('ning xu yao jiao na 15 meiyuan')