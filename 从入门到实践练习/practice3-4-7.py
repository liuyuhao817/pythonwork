Invitees=['father','mother','sister']
# print(f'{Invitees[0]},Welcome to beijing')
# print(f'{Invitees[1]},Welcome to beijing')
# print(f'{Invitees[2]},Welcome to beijing')
print(f'{Invitees[0]},wufacanjia')
Invitees[0]='brother'
# print(f'{Invitees[0]},Welcome to beijing')
# print(f'{Invitees[1]},Welcome to beijing')
# print(f'{Invitees[2]},Welcome to beijing')
print(f'wo zhao dao le yi ge da can zuo')
Invitees.insert(0,'aobama')
Invitees.insert(2,'xjp')
Invitees.append('hjt')
# i=0
# while i<len(Invitees):
#     print(f'{Invitees[i]},Welcome to beijing')
#     i+=1
print(Invitees)
print(f'sorry,因为不可抗力，只能邀请两位了')
i=0
while i <= len(Invitees):
    pop1=Invitees.pop(0)
    print(f'不好意思，{pop1}')
    i += 1
print(f'{Invitees[0]},Welcome to beijing')
print(f'{Invitees[1]},Welcome to beijing')
del Invitees[0]
del Invitees[0]
print(Invitees)
