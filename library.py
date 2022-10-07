from operator import index

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
user_input=input('''choose a rack to see the list of books:
rack1
rack2
rack3
 ''')
if user_input=='rack1':
    user_input_rack1=input('''which of the below list of books you want
    science
    math
    ''')
    if user_input_rack1=='science':
        user_input_science=input('''
        choose a option below
        biology
        chemistry
        physics
        ''')
        if user_input_science=='biology':
            print(biology_books_list)
        elif user_input_science=='chemistry':
            print(chemistry_books_list)
        elif user_input_science=='physics':
            print(physics_books_list)
        else:
            print('choose a correct option')
    elif user_input_rack1=='math':
        user_input_math=input('''
        choose a option below
        trigonmetry
        geometry
        algebra
        ''')
        if user_input_math=='trigonmetry':
            print(trigonmetry_books_list)
        elif user_input_math=='geometry':
            print(geometry_books_list)
        elif user_input_math=='algebra':
            print(algebra_books_list)
        else:
            print('enter a correct option')
elif user_input=='rack2':
    user_input_arts=input('''
    choose a option below
    political_science
    history
    ''')
    if user_input_arts=='political_science':
        print(political_science_books_list)
    elif user_input_arts=='history':
        print(history_books_list)
    else:
        print('enter a correct option')
    
elif user_input=='rack3':
    print(f'Welcome to commerce section and here is the list of accounts books {acounts_books_list}')
else:
    print('enter a correct option')
# for i in biology_books_list:
#     print('List of Biology books',biology_books_list.index(i),'-',i)