def capitalize(msg):
    def  wrapper():
        msg.upper()
    return wrapper()


@capitalize
def greet():
    return 'hello'


print(greet())