# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami','turkey',
#     'roast beef', 'pastrami']
# finished_sandwiches = []
#
# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# while sandwich_orders:
#     cuntur = sandwich_orders.pop()
#     print(f'i made your tuna {cuntur} sandwich')
#     finished_sandwiches.append(cuntur)
#
# for sandwich in finished_sandwiches:
#     print(f" {sandwich} ")

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    responses[name] = place

    repeat  = input(continue_prompt)

    if repeat == 'no':
        break
for name,place in responses.items():
    print(f"{name}would like to visit{place}")