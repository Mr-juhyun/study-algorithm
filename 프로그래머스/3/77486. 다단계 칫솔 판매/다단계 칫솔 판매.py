from math import trunc
from collections import deque
def solution(enroll, referral, seller, amount):
    seller = deque(seller)
    amount = deque(amount)
    relation = {enroll[i]:referral[i] for i in range(len(enroll))}
    pay = {name:0 for name in enroll}

    def profits(name,seller_amount):

        offer_to = trunc(seller_amount*0.1)
        pay[name] += seller_amount-offer_to

        if relation[name] != '-' and offer_to != 0:
            pay[relation[name]] += offer_to - offer_to
            profits(relation[name],offer_to)

    for i in range(len(seller)):
            name = seller[i]
            seller_amount = amount[i] * 100
            profits(name, seller_amount)

    
    return list(pay.values())