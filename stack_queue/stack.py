class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        '''adds item to stack'''
        return self.items.append(item)

    def pop(self):
        '''return the last item in stack but also removes it from the stack'''
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        '''returns true if stack is empty, otherwise false'''
        return len(self.items) == 0

    def peek(self):
        '''returns the last item in stack but it doesnt remove it from the stack'''
        if not self.is_empty():
            return self.items[-1]

    def get_stack_items(self):
        '''return the items of the stack'''
        return self.items

    def print_stack(self):
        '''prints the stack'''
        print(self.get_stack_items())

    def divide_odd_even(self, oddStack, evenStack):
        '''places the elements that have odd numbers(value) to the oddStack, and the other even numbered elements to the evenStack.

        *** Removes all elements of the called stack ***
        '''
        while self.is_empty() is not True:
            if self.peek() % 2 == 0:
                oddStack.push(self.pop())
            else:
                evenStack.push(self.pop())

    def create_copy_of_stack(self):
        '''returns a copy of the called stack'''
        copy = Stack()
        temp = self.get_stack_items()

        for i in temp:
            copy.push(i)

        # copy.print_stack()
        return copy

    def reverse(self):
        '''reverses a stack

        *** Does not create a new stack.
        '''
        s = []
        while self.is_empty() is not True:
            s.append(self.pop())

        for i in s:
            self.push(i)

        # self.print_stack()

    # e kam nru code te detyres bombe
    def remove_value_from_stack(self, value):
        '''removes a value from the stack'''
        cisti_stek = Stack()
        counter = 0
        while not self.is_empty():
            element = self.pop()
            if element == value:
                counter = counter + 1
            if element != value:
                cisti_stek.push(element)
        cisti_stek.reverse()
        return cisti_stek
        # print("Ocisceni stek: " + str(cisti_stek.get_stack_items()) +
        #       " ---> Broj bombi u steku:" + str(counter))

    @staticmethod
    def convert_to_binary(broj):
        '''converts a number to its binary representation'''
        stack = Stack()
        while broj > 0:
            reminder = broj % 2
            stack.push(reminder)
            broj = broj//2
        binarni_broj = ""
        while not stack.is_empty():
            binarni_broj = binarni_broj+str(stack.pop())

        print(binarni_broj)
        return binarni_broj

    def parnepar(self, s2):
        '''creates and returns two stacks, one with even and one with odd numbers.

        *** The called stack will be empty ***
        '''
        s1 = Stack()
        while not self.is_empty():
            element = self.pop()
            if element % 2 == 0:
                s1.push(element)
            else:
                s2.push(element)
        return s1, s2

# def remove_duplicates_in_pair(s):
#     res = Stack()
#     while not s.is_empty():
#         elem = s.pop()
#         if s.peek() != elem:
#             res.push(elem);
#     return res

# def reverse_stack(stack):
#     stack.get_stack().reverse()
#     return stack

# def remove_duplicates(s):
#     l = s.get_stack().copy() # ovo obavezno da se ne desi da odradimo reverse i nad s i nad l
#     l.reverse()

#     new_stack = Stack()
#     counter = 1
#     while not s.is_empty():
#         elem = s.pop()
#         if elem not in l[counter:]:
#             new_stack.push(elem)
#         counter = counter + 1

#     return reverse_stack(new_stack)

# kta ne koment jan per kta 3 metodat e profit
# r = remove_duplicates_in_pair(s)
# reverse_stack(r)
# print(r.get_stack())
# print(remove_duplicates(r).get_stack())


s1 = Stack()
s1.push(5)
s1.push(2)
s1.push(4)
s1.push(4)
s1.push(5)
s1.push(7)
s1.push(4)
s1.push(9)
s1.push(7)

s1.print_stack()

s1 = s1.remove_value_from_stack(5)

s1.print_stack()


s2 = Stack()
s2.push(4)
s2.push(5)
s2.push(7)
s2.push(4)
s2.push(2)
s2.push(9)
s2.push(4)
s2.push(7)
s2.push(5)

# s2.print_stack()

# Stack.convert_to_binary(276)
