from dataclasses import dataclass
from typing import List


@dataclass
class Computer:
    id: int
    name: str

@dataclass
class Browser:
    id: int
    name: str
    memory_usage: int  
    computer_id: int   

@dataclass
class ComputerBrowser:
    computer_id: int
    browser_id: int

class BrowserManager:
    def __init__(self):
        self.computers = [
            Computer(1, "Офисный компьютер"),
            Computer(2, "Игровой компьютер"),
            Computer(3, "Серверный отдел"),
            Computer(4, "Главный компьютер")
        ]
        
        self.browsers = [
            Browser(1, "Chrome", 512, 1),
            Browser(2, "Firefox", 256, 1),
            Browser(3, "Edge", 384, 2),
            Browser(4, "Opera", 128, 2),
            Browser(5, "Safari", 192, 3),
            Browser(6, "Chrome", 512, 4)
        ]
        
        self.computer_browsers = [
            ComputerBrowser(1, 1),
            ComputerBrowser(1, 2),
            ComputerBrowser(2, 3),
            ComputerBrowser(2, 4),
            ComputerBrowser(3, 5),
            ComputerBrowser(4, 6),
            ComputerBrowser(1, 3),  
            ComputerBrowser(2, 1)   
        ]
    
    def task_1(self):
        print(" ЗАПРОС 1")        
        
        computer_dict = {comp.id: comp for comp in self.computers}

        browsers_by_computer = {}
        for browser in self.browsers:
            if browser.computer_id not in browsers_by_computer:
                browsers_by_computer[browser.computer_id] = []
            browsers_by_computer[browser.computer_id].append(browser)
        
        for computer_id in sorted(browsers_by_computer.keys()):
            computer = computer_dict[computer_id]
            print(f"\nКомпьютер: {computer.name} (ID: {computer.id})")
            for browser in browsers_by_computer[computer_id]:
                print(f"  - {browser.name} (использует памяти: {browser.memory_usage} МБ)")
    
    def task_2(self):
        print("\n ЗАПРОС 2")        
        
        memory_by_computer = {}
        for browser in self.browsers:
            if browser.computer_id not in memory_by_computer:
                memory_by_computer[browser.computer_id] = 0
            memory_by_computer[browser.computer_id] += browser.memory_usage
                
        sorted_memory = sorted(memory_by_computer.items(), key=lambda x: x[1])
        
        computer_dict = {comp.id: comp for comp in self.computers}
        
        for computer_id, total_memory in sorted_memory:
            computer = computer_dict[computer_id]
            print(f"Компьютер: {computer.name} - Суммарное использование памяти: {total_memory} МБ")
    
    def task_3(self):        
        print("\n ЗАПРОС 3 ")
        
        filtered_computers = [comp for comp in self.computers if "компьютер" in comp.name.lower()]
        
        computer_browser_set = {(cb.computer_id, cb.browser_id) for cb in self.computer_browsers}
        
        browser_dict = {browser.id: browser for browser in self.browsers}
        
        for computer in filtered_computers:
            print(f"\nКомпьютер: {computer.name}")
                        
            related_browsers = []
            for computer_id, browser_id in computer_browser_set:
                if computer_id == computer.id:
                    browser = browser_dict.get(browser_id)
                    if browser:
                        related_browsers.append(browser)
            
            if related_browsers:
                for browser in related_browsers:
                    print(f"  - {browser.name} (использует памяти: {browser.memory_usage} МБ)")
            else:
                print("  - Нет связанных браузеров")

def main():
    manager = BrowserManager()
    
    manager.task_1()
    manager.task_2()
    manager.task_3()

if __name__ == "__main__":
    main()
