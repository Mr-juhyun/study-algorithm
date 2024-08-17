def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        head = phone_book[i]
        if head == phone_book[i+1][:len(head)]:
            return False
            
    return True
            
