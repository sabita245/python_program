#list can not be used as a key in dict because list is mutable
#once we create a list its hash value will create and if we change the list value then hash value will also change nad if we use list as a key of dict then it can not able to find the value as the the hash value has been changed
#we can use list as a dict key in following way
d={}
li=[1,2,3]
a=str(li)
d[a]=10
for key,value in d.items():
    print(key,":",value)
