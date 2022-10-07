from collections import Counter
test_dict = {'Manjeet' : [1, 4, 5, 6],
            'Akash' : [1, 8, 9],
            'Nikhil': [10, 22, 4],
            'Akshat': [5, 11, 22]}
count=Counter()
for idx in test_dict.values():
    count.update(idx)
#print(count)
res={idx:[key for key in j if count[key]==1] for idx,j in test_dict.items()}
print(res)