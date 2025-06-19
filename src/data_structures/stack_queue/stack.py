class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """adds item to stack"""
        self.items.append(item)

    def pop(self):
        """return the last item in stack but also removes it from the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        """returns true if stack is empty, otherwise false"""
        return len(self.items) == 0

    def peek(self):
        """returns the last item in stack but it doesnt remove it from the stack"""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def get_stack_items(self):
        """return the items of the stack"""
        return self.items.copy()  # Return a copy to prevent external modification

    def print_stack(self):
        """prints the stack"""
        print(self.get_stack_items())

    def divide_odd_even(self, odd_stack, even_stack):
        """places the elements that have odd numbers(value) to the odd_stack, and the other even numbered elements to the even_stack.
        *** Removes all elements of the called stack ***
        """
        if not isinstance(odd_stack, Stack) or not isinstance(even_stack, Stack):
            raise TypeError("Arguments must be Stack instances")

        while not self.is_empty():
            element = self.pop()
            try:
                if element % 2 == 0:
                    even_stack.push(element)  # Fixed: even numbers go to even_stack
                else:
                    odd_stack.push(element)  # Fixed: odd numbers go to odd_stack
            except TypeError:
                # Handle non-numeric values by putting them in odd_stack
                odd_stack.push(element)

    def create_copy_of_stack(self):
        """returns a copy of the called stack"""
        copy = Stack()
        temp = self.get_stack_items()
        for item in temp:
            copy.push(item)
        return copy

    def reverse(self):
        """reverses a stack
        *** Does not create a new stack.
        """
        temp_list = []
        while not self.is_empty():
            temp_list.append(self.pop())
        for item in temp_list:
            self.push(item)

    def remove_value_from_stack(self, value):
        """removes a value from the stack and returns a new stack without that value"""
        clean_stack = Stack()
        removed_count = 0

        while not self.is_empty():
            element = self.pop()
            if element == value:
                removed_count += 1
            else:
                clean_stack.push(element)

        clean_stack.reverse()  # Restore original order

        # Restore original stack
        temp_items = clean_stack.get_stack_items()
        for item in temp_items:
            if item != value:  # Don't add back the removed values
                self.push(item)

        return clean_stack, removed_count

    @staticmethod
    def convert_to_binary(number):
        """converts a number to its binary representation"""
        if not isinstance(number, int) or number < 0:
            raise ValueError("Input must be a non-negative integer")

        if number == 0:
            return "0"

        stack = Stack()
        original_number = number

        while number > 0:
            remainder = number % 2
            stack.push(remainder)
            number = number // 2

        binary_string = ""
        while not stack.is_empty():
            binary_string += str(stack.pop())

        return binary_string

    def separate_even_odd(self, odd_stack):
        """creates and returns two stacks, one with even and one with odd numbers.
        *** The called stack will be empty ***
        """
        if not isinstance(odd_stack, Stack):
            raise TypeError("Argument must be a Stack instance")

        even_stack = Stack()

        while not self.is_empty():
            element = self.pop()
            try:
                if element % 2 == 0:
                    even_stack.push(element)
                else:
                    odd_stack.push(element)
            except TypeError:
                # Handle non-numeric values by putting them in odd_stack
                odd_stack.push(element)

        return even_stack, odd_stack

    def size(self):
        """returns the number of items in the stack"""
        return len(self.items)

    def __str__(self):
        """string representation of the stack"""
        return f"Stack({self.items})"

    def __repr__(self):
        """detailed string representation of the stack"""
        return f"Stack(items={self.items})"

    def __eq__(self, other):
        """equality comparison for stacks"""
        if not isinstance(other, Stack):
            return False
        return self.items == other.items
