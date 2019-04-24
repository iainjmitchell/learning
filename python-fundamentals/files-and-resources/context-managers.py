from contextlib import closing

class Example:
    def open(self):
        print("open")
    
    def doSomething(self, message):
        print("Hello {message}".format(message=message))

    def close(self):
        print("Closing")

with closing(Example()) as example:
    example.open()
    example.doSomething("this message")
