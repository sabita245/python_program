is_old=True
is_licenced=False
if is_old==True and is_licenced==True:
    print("you can drive")
else:
    print("ckeckcheck")
is_friend=bool(input("enter 0 or 1"))
print(is_friend)
can_message= "you can message" if is_friend else "you are not allowed to message"
print(can_message)