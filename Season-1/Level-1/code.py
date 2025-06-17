'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal(0.0)
    total_cost = Decimal(0.0)

    for item in order.items:
        if item.type == 'payment':
            payment_amount = Decimal(str(item.amount))
            net += payment_amount
        elif item.type == 'product':
            if item.quantity < 0 or item.quantity != int(item.quantity):
                return "Invalid order detected"
            product_amount = Decimal(str(item.amount))
            cost = product_amount * item.quantity
            
            net -= cost
            total_cost += cost
        else:
            return "Invalid item type: %s" % item.type
    # Check if the total amount payable exceeds the limit
    if total_cost > 999999:
        return "Total amount payable for an order exceeded"
    elif net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id