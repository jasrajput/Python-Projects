sandwiches_orders = ['tuna', 'macaroni', 'tomato', 'noodle', 'chicken', 'pastrami', 'pastrami', 'pastrami']
finish_sandwiches = []
print("Deli has run out of all pastrami")


def sandwiches(sandwich_orders, finished_sandwiches):
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    for order in sandwich_orders:
        print("I made your " + order + " sandwich")
        finished_sandwiches.append(order)
    for complete_order in finished_sandwiches:
        print(complete_order)


sandwiches(sandwiches_orders, finish_sandwiches)