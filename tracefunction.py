import sys



def tracefunc(frame, event, arg):
    if event == "return":
        print("function: ", frame.f_code.co_name, ", local vars: ", list(frame.f_locals.keys()))
    return tracefunc

def foo():
    friends = ["Bob", "Tom"]

    for f in friends:
        print("Hi %s!” % f")
    return len(friends)

sys.settrace(tracefunc)
foo()

