Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
2+2
4
>>> 
2**4
16
>>> 
======== RESTART: C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py ========
Hello World
Name?
Tannis
HelloTannis
Traceback (most recent call last):
  File "C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py", line 5, in <module>
    print('The length of your name is: ' + len(myName))
TypeError: Can't convert 'int' object to str implicitly
>>> 
======== RESTART: C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py ========
Hello World
Name?
Tannis
HelloTannis
Traceback (most recent call last):
  File "C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py", line 5, in <module>
    print('The length of your name is: ' + string(len(myName)))
NameError: name 'string' is not defined
>>> 
======== RESTART: C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py ========
Hello World
Name?
Tannis
HelloTannis
The length of your name is: 6
>>> 
======== RESTART: C:/Users/Tannis/Documents/GitHub/abs/chap0/chap0.py ========
Hello World
Name?
Tannis
Hello Tannis
The length of your name is:
6
>>> 
