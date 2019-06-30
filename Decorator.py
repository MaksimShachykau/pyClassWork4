class Foo:
    def __init__(self, bar):
        self.bar = bar

    @staticmethod
    def create_file():
        with open("file", 'a') as f:
            f.write("Hehe")


Foo.create_file()

