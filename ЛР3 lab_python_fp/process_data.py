import json
import sys
from datetime import datetime
import random

def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

class cm_timer_1:
    def __enter__(self):
        self.start_time = datetime.now()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        execution_time = (self.end_time - self.start_time).total_seconds()
        print(f"Время работы: {execution_time:.2f} секунд")

path = r"C:\Users\User\Desktop\data_light.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(set(job['job-name'].lower() for job in arg), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in arg]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
