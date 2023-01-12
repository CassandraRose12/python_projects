def hello():
    print("hello, user")
def pack(a,b,c):
    return[a,b,c]
def eat_lunch(my_meals):
    if len(my_meals) == 0:
        print("My Child is hungry")
    else:
        for i in range(len(my_meals)):
            if i == 0:
                print("First I eat {my_meals[0]}")
            else: 
                print("Next I eat {my_meals[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["pudding"])
eat_lunch(["carrots","wrap","potatos","cookie"])
