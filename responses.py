import random
d={

    '''Which of the following is a valid variable name in Python?
a) 123variable
b) _variable
c) variable-name
d) variable name
''':"b",

'''
my_list = [1, 2, 3, 4]
print(my_list[5])
a) 5
b) IndexError: list index out of range
c) None
d) [1, 2, 3, 4]
''':"b",
'''
Which keyword is used to define a function in Python?
a) func
b) function
c) def
d) define
''':"c",
'''
5 + 2 * 3
a) 21
b) 11
c) 17
d) 9''':"d",
'''
Which module is used for working with dates and times in Python?
a) datetime
b) time
c) date
d) calendar''':"a",
'''
print("Hello, " + 5)
a) Hello, 5
b) TypeError: can only concatenate str (not "int") to str
c) Hello,
d) SyntaxError: invalid syntax''':"b",
'''
What is the correct way to open a file named "data.txt" in Python?
a) open("data.txt")
b) open_file("data.txt")
c) file_open("data.txt")
d) file.open("data.txt")''':"a",
'''
Which of the following is an immutable data type in Python?
a) List
b) Tuple
c) Dictionary
d) Set''':"b",
'''
What is the purpose of the "pass" statement in Python?
a) It breaks out of the current loop.
b) It skips the rest of the current iteration.
c) It is used as a placeholder for future code.
d) It raises an exception.
''':"c",
'''
Which of the following is used to format a string in Python?
a) % operator
b) & operator
c) * operator
d) $ operator''':"a"
}
prev=-1
questions=list(d.keys())
answers=[list(d.values())]
def get_response(message: str) -> str:
    global prev
    p_message = message.lower()
    if prev==-1:
        prev=random.choice(questions)
    
    if p_message in "abcd" and d[prev]==p_message:
        prev=random.choice(questions)
        return "Thats brillient\n"+prev
    if p_message in "abcd" and d[prev]!=p_message:
        return "Opps!!! try again\n"+prev
    if p_message=="roll" or prev!=-1:
        return prev
    
    

    return 'I didn\'t understand what you wrote. Try typing "!help".'
