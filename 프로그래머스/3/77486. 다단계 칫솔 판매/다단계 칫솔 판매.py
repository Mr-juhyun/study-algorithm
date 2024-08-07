from math import trunc
def solution(enroll, referral, seller, amount):

    relation = {enroll[i]:referral[i] for i in range(len(enroll))}
    pay = {name:0 for name in enroll}

    def profits(name,offer_to):
        
        if relation[name] != '-' and offer_to > 0:
            
            up_name = relation[name]
            pay[up_name] += offer_to - trunc(offer_to*0.1)
            
            profits(up_name,trunc(offer_to*0.1))               

            
    for name,pcs in zip(seller,amount):
        money = pcs*100
        offer_to = trunc(money*0.1)
        pay[name] += money - offer_to
        
        profits(name,offer_to)

    return list(pay.values())