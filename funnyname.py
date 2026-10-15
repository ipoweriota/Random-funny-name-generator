from random import choice
a=('integral', 'cyan', 'ipoweriota', 'mao', 'vaanaaved')
b=('pathak', 'mishra', 'upadhyay', 'pandey', 'kumar')
x = choice(a)
y = choice(b)
while True:
    print("\033[43m" + f'{x} {y}' + "\033[0m")
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == 'n':
        break
    x = choice(a)
    y = choice(b)

