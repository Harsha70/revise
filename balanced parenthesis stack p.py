#Stack

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
        
def par_checker(symbol_string):
    s = Stack() 
    balanced = True 
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index] 
        if symbol == "(" or symbol == "[" or symbol == "{" :
            s.push(symbol) 

        else:
            if s.is_empty(): 
                balanced = False
            else:
                top = s.pop() 
                if not matches(top, symbol): 
                    balanced = False

        index = index + 1
        #print(index)

    if balanced and s.is_empty(): 
         return True 
    else: 
        return False

def matches(open, close): 
    opens = "([{" 
    closes = ")]}" 
    #print(opens.index(open))
    return opens.index(open) == closes.index(close)


print(par_checker('{{([][])}()}]'))
print(par_checker('[{()}]'))


'''
def base_converter(dec_number, base): 
    digits = "0123456789ABCDEFG"
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem) 
        dec_number = dec_number // base
    new_string = "" 
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string
print(base_converter(25, 2)) 
print(base_converter(16,16))
'''
