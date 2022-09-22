pet_list=['cyan','ryiku','shanti']
def capitalize(item):
    return item.capitalize()
print(list(map(capitalize,pet_list)))
score_list=[50,60,40,30,70,90]
def max_score(item):
    return item>50
print(list(filter(max_score,score_list)))
