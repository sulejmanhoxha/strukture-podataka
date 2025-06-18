"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:

(), ()(), (({[]}))  <- Balanced.

((), {{{)}], [][]]] <- Not Balanced.
Balanced Exanple: {[]}
Non-Balanced Exanple: (()
Non-Balanced Example: ))

"""

# sdi a punen , vet e kam ba
from data_structures.stack_queue.stack import Stack


def is_match(p1, p2):
    return (p1 == "(" and p2 == ")") or (p1 == "[" and p2 == "]") or (p1 == "{" and p2 == "}")


def is_parenthesis_balanced(str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(str) and is_balanced:
        parenthesis = str[index]
        if parenthesis in "{[(":
            s.push(parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parenthesis):
                    is_balanced = False
        index = index + 1
    return s.is_empty() and is_balanced


print(is_parenthesis_balanced("[(())]"))
