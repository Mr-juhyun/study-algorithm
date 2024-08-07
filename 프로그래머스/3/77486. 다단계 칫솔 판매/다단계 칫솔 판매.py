from math import trunc
def solution(enroll, referral, seller, amount):
    
    relation = {enroll[i]:referral[i] for i in range(len(enroll))}
    pay = {name:0 for name in enroll}

    
    def profits(name,offer_to):
        
        if relation[name] != '-' and offer_to != 0:
            for_up = trunc(offer_to*0.1)
            pay[relation[name]] += offer_to - for_up
            profits(relation[name],for_up)

            
    for i in range(len(seller)):
            seller_name = seller[i]
            seller_amount = amount[i] * 100
            
            offer_to = trunc(seller_amount*0.1)
            pay[seller_name] += seller_amount-offer_to
            
            profits(seller_name, offer_to)

    
    return list(pay.values())