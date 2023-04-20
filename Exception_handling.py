print("Exception handling")
try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error1")
else:
    print(c)
finally:
    print("this will always print")

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	print ("Fourth element = %d" %(a[3]))

except:
	print ("error 2 ")
finally:
    print("this will always print")

