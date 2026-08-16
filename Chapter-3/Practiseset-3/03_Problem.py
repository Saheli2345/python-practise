"""" A spam comment is defined as a text containing the following keywords:
"Make a lot of money", "buy now", "subscribe this", "click this".
Write a program to detect these spams."""

a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"
message = input()
if( a in message or b in message or c in message or d in message):
    print("This comment is spam")
else:
    print("Not spam")    