import sys

def tracefunc(frame, event, arg):
    if event == "return":
        print("function: ", frame.f_code.co_name,", local vars: ", list(frame.f_locals.keys()))
    return tracefunc

