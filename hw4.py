#part 1
#1
def add_numbers(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(add_numbers(3, 5)) # Output: 8
print(add_lambda(3, 5)) # Output: 8

#2
def join_words(*words):
    return " ".join(words)

join_lambda = lambda *words: " ".join(words)

print(join_words("Hello", "world", "!"))  # Output: "Hello world !"
print(join_lambda("Hello", "world", "!")) # Output: "Hello world !"

#3
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)  # Output: 5, 4, 3, 2, 1, 0

#4
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"

#5
def repeat_phrase(phrase, times=2):
    return phrase * times

print(repeat_phrase("Hi! "))      # Output: "Hi! Hi! "
print(repeat_phrase("Hi! ", 3))  # Output: "Hi! Hi! Hi! "

#6
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x.upper(), "hello"))  # Output: "HELLO"

#part 2
#7
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: "Error: Cannot divide by zero"

#8
def check_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")
    return "Valid age"

try:
    print(check_age(-5))
except ValueError as e:
    print(e)  # Output: "Age must be a positive integer"

#9
def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Invalid integer format"

print(parse_int("25"))  # Output: 25
print(parse_int("abc")) # Output: "Error: Invalid integer format"

#10
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    finally:
        print("Division attempted") #Division attempted

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: "Error: Cannot divide by zero"

#part 3
#11
numbers = [5, 4, 3, 2, 1]
iterator = iter(numbers)
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 1

#12
words = ["hello", "world", "python"]
uppercase_gen = (word.upper() for word in words)
for word in uppercase_gen:
    print(word)  # Output: HELLO, WORLD, PYTHON

#13
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

countdown_iter = Countdown(5)
for num in countdown_iter:
    print(num)  # Output: 5, 4, 3, 2, 1, 0

#14
import itertools
colors = ["red", "blue", "green"]
color_cycle = itertools.cycle(colors)
for _ in range(6):
    print(next(color_cycle))  # Output: red, blue, green, red, blue, green
