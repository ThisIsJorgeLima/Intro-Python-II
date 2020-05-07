"""
Import statements:
"""

import random

# rolling dice demo
while True:
    input("Press enter to roll")
    dice = random.randrange(1, 7)

    print(dice)
# +--------------------------------------------+

"""
Practicing Refactoring: "while True" infinite Loops & The "input" Function:
- We are keeping the while answer not in ("yes", "no"):
is nice implementation because we're having the while loop
and we're checking it against a tuple of strengths rather than a list.
Constructing a tuple is going to be a little bit faster.
- We can use a tuple every time when you don't a mutable object
- It's a constant that we use to compare against yes or no
"""

#
# def get_answer(prompt):
#     while True:
#         answer = input(prompt)
#         if answer in ('yes', 'no'):
#             return answer  # this breaks the loop by returning the answer
#
#
# def get_answer_original(prompt):
#     answer = input(prompt)  # we are pulling
#     # 1 while not (answer == "yes" or answer == "no"):
#     # 2 while answer not in ("yes", "no"):
#     # 3 while answer not in ["yes", "no"]:
#
#     while answer not in ("yes", "no"):
#         answer = input(prompt)
#     return answer
#
#
# # print(get_answer("yes or no? "))
