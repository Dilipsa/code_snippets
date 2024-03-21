class MyIterator:
    def __init__(self, start, limit):
        self.start = start
        self.limit = limit
        self.current = self.start - 2  # Adjust starting point to include the start value

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2  # Increment by 2 to generate even numbers
        if self.current >= self.limit:
            raise StopIteration
        else:
            return self.current

# Using the MyIterator class
# iter = MyIterator(3, 10)
# for i in iter:
#     print(i)

colors = ['Black', 'Purple', 'Green']
iterator = iter(colors)
print(next(iterator))  # Output: Black
print(next(iterator))  # Output: Purple
print(next(iterator))  # Output: Green
print(next(iterator))
