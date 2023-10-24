class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def percentage(self):
        return (self.num1 * self.num2) / 100

    def power(self):
        return self.num1 ** self.num2

import string
import random

class Random:
    def __init__(self,length):
        self.length = length
        
    def random_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(self.length))
    
    def random_number(self):
        return [random.randint(1, 90) for u in range(self.length)]
         



        