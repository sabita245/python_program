from collections import Counter
test_dict={ 'gfg' : [5, 7, 9, 4, 0], 'si': [6, 7, 4, 3, 3], 'best' : [9, 9, 6, 5, 5]}
count=Counter()
for idx in test_dict.values():
    print(count(idx))

