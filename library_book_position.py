library_dict={
    'rack1':{
        'science':{
            'biology':['The Science of Sleep','The Science of Plants','Genetics'],
            'chemistry':['Chemistry: The Impure Science','The Handy Chemistry Answer Book'],
            'physics':['The Elegant Universe','Quantum Mechanics','A Brief History of Time']
        }
        ,'math':{
            'trigonmetry':['Trigonometry For Dummies','Geometry and Trigonometry for Calculus'],
            'geometry':['The Elements of COORDINATE GEOMETRY',' A SCHOOL GEOMETRY'],
            'algebra':['HIGHER ALGEBRA','Linear Algebra And Its Applications']
        }
    },
    'rack2':{
        'arts':{
            'political_science':['Arthashastra','The Communist Manifesto'],
            'history':['History Adventures','The Guns of August']
        }
    },
    'rack3':{
        'commerce':{
            'accounts':['Accounting Made Simple','A Brief History of Economic Genius Paperback']
        }
    }
}
print(library_dict.keys())
print(library_dict['rack1'].keys())
print(library_dict['rack2'].keys())
print(library_dict['rack3'].keys())
print(library_dict['rack1']['science'].keys())
print(type(library_dict['rack1']['science']['biology']))
biology_books_list=library_dict['rack1']['science']['biology']
chemistry_books_list=library_dict['rack1']['science']['chemistry']
physics_books_list=library_dict['rack1']['science']['physics']
trigonmetry_books_list=library_dict['rack1']['math']['trigonmetry']
geometry_books_list=library_dict['rack1']['math']['geometry']
algebra_books_list=library_dict['rack1']['math']['algebra']
political_science_books_list=library_dict['rack2']['arts']['political_science']
history_books_list=library_dict['rack2']['arts']['history']
acounts_books_list=library_dict['rack3']['commerce']['accounts']
book_list=biology_books_list+chemistry_books_list+physics_books_list+trigonmetry_books_list+geometry_books_list+algebra_books_list+political_science_books_list+history_books_list
print('list of books')
for i in book_list:
    print(book_list.index(i),i)
user_input=input('choose a book name from the above option: ')
if user_input in biology_books_list:
    print('Go to rack1 science block')
elif user_input in chemistry_books_list:
    print('Go to rack1 science')
elif user_input in physics_books_list:
    print('Go the rack1 science block')
elif user_input in trigonmetry_books_list:
    print('Go to rack1 math block')
elif user_input in geometry_books_list:
    print('Go to rack1 Math block')
elif user_input in algebra_books_list:
    print('Go to rack1 math block')
elif user_input in political_science_books_list:
    print('Go to rack2 arts block')
elif user_input in history_books_list:
    print("Go to rack2 arts block")
elif user_input in acounts_books_list:
    print('Go to rack3 commerce block')
else:
    print('choose a correct option.')

