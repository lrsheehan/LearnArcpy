age = raw_input("Enter your age:")
new_age = int(age) + 50
print(new_age)

c="Hi There"
dir(c)
help("".getitem)

c[0:2] #pulls "Hi"

def divide(a,b):
    try:
        result = a/b
        print(result)
    except:
        print "error"
divide(10,0)
