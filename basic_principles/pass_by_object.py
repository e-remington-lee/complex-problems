class Book(object):
    def __init__(self, name, id):
        super().__init__()
        self.name = name
        self.id = id

    def __eq__(self, other):
        if isinstance(self, type(other)):
            print(type(other))
            return self.name==other.name and self.id==other.id
        return False
    
     
book1 = Book("book1", 1)
book2 = Book("book1", 1)
print(id(book1))
print(id(book2))

book3 = book1
print(id(book3))

print(book2 is book1)
print(book3 is book1)
print(book1==book2)


def do_something(obj):   
    obj.name = "did change the name"

do_something(book1)
print(book1.name)


def rename(obj):
    print(obj.name)
    obj = Book("will not change name", 5)
    print(obj.name)

rename(book1)
print(book1.name)