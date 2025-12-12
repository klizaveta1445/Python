
class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)  
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            val = next(self.items)  
            key = val.lower() if (self.ignore_case and isinstance(val, str)) else val
            if key not in self.seen:
                self.seen.add(key)
                return val

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

print(list(Unique(data)))  

print(list(Unique(data, ignore_case=True)))

