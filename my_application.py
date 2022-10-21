import json
import random
import datetime 
import time

class Institute:
    "This is application for training new joiner"
    name_of_institute = "MsysTechnologies India PVT. Ltd." # class Varibale
    def add_trainner(self,name_of_trainer,name_of_technology,active=False):
        self.name_of_trainer = name_of_trainer
        self.name_of_technology = name_of_technology
        id = random.randint(1000,2000)
        data_dict = {}
        try:
            with open("data.json","r",encoding="utf-8") as file:
                data = json.loads(file.read())
                for i in range(len(data["trainers"])):
                    if data["trainers"][i]["trainerId"]==id:
                        id = random.randint(1000,2000)
                    else:
                        pass
            if "trainers" in data:
                data["trainers"].append(
                        {   "trainerId":id,
                        "name":self.name_of_trainer,
                        "technology":self.name_of_technology,
                        "active":eval(active.title())
                    }
                )
            else:
                data["trainers"]=[
                        {   "trainerId":id,
                        "name":self.name_of_trainer,
                        "technology":self.name_of_technology,
                        "active":eval(active.title())
                    }
                ]
            data_dict = data
        except:
            data_dict = {
                "trainers":[
                    {   "trainerId":id,
                        "name":self.name_of_trainer,
                        "technology":self.name_of_technology,
                        "active":eval(active.title())
                    }
                ]
            }
        with open("data.json","w",encoding="utf-8") as file:
            data = json.dumps(data_dict)
            file.write(data)
            return print("Trainer Added Successfully In To DB!")

    def get_trainer_by_technology(self,technology_name):
        self.filter_technology_list = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["technology"]==technology_name:
                    self.filter_technology_list.append(trainer)
        return self.filter_technology_list

    def get_trainer_by_name(self,trainer_name):
        self.filter_name_list = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["name"]==trainer_name:
                    self.filter_name_list.append(trainer)
        return self.filter_name_list
    
    def get_trainer_by_id(self,trainer_id):
        self.filter_id_list = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["trainerId"]==trainer_id:
                    self.filter_id_list.append(trainer)
        return self.filter_id_list
    def trainer_data_update(self,name,technology):
        update_field=input('enter which field you want to update:')
        if update_field=='name':
            for i in self.filter_name_list:
                user_input=input('enter the name  you want:')
            self.filter_name_list['name']=self.filter_name_list['user_input']
        elif update_field=='technology':
            for i in self.filter_technology_list:
                user_input_technology=input('enter the technology name:')
            self.filter_technology_list['technology']=self.filter_technology_list['user_input_technology']
        return self.filter_name_list,self.filter_technology_list
    def del_trainer(self,id):
        user_trainer_id=int(input('enter the id of the trainer you want to remove'))
        trainer_updated_id=self.filter_id_list.remove(user_trainer_id)
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            self.filter_id_list=data['id'].update(trainer_updated_id)

    def add_trainee(self,name,technology,joining_date,duration,email_id,active=False):
        self.trainee_name = name
        self.technology = technology
        self.joining_date = joining_date
        self.duration = duration
        self.email = email_id
        self.id = random.randint(10000,99999)
        data_dict = {}
        try:
            with open("data.json","r",encoding="utf-8") as file:
                data = json.loads(file.read())

            if "trainees" in data:
                data["trainees"].append(
                    {   "traineeId":self.id,
                        "name":self.trainee_name,
                        "technology":self.technology,
                        "email":self.email,
                        "joining_data":self.joining_date,
                        "duration":self.duration,
                        "active":eval(active.title())
                    }
                )
            else:
                data["trainees"]=[
                    {   "traineeId":self.id,
                        "name":self.trainee_name,
                        "technology":self.technology,
                        "email":self.email,
                        "joining_data":self.joining_date,
                        "duration":self.duration,
                        "active":eval(active.title())
                    }
                ]
            data_dict = data
            
        except:
            data_dict = {
                "trainees":[
                    {   "traineeId":self.id,
                        "name":self.trainee_name,
                        "technology":self.technology,
                        "email":self.email,
                        "joining_data":self.joining_date,
                        "duration":self.duration,
                        "active":eval(active.title())
                    }
                ]
            }
        with open("data.json","w",encoding="utf-8") as file:
            data = json.dumps(data_dict)
            file.write(data)
        return print("Trainee Added Successfully In To DB!")

    def get_trainee_by_technology(self,technology_name):
        self.filter_technology_list = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainees"]
            for trainer in trainer_list:
                if trainer["Technology"]==technology_name:
                    self.filter_technology_list.append(trainer)
        return self.filter_technology_list

    def get_trainee_by_name(self,trainee_name):
        self.filter_name_list_trainee = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainees"]
            for trainee in trainer_list:
                if trainee["name"]==trainee_name:
                    self.filter_name_list_trainee.append(trainee)
        return self.filter_name_list_trainee
    
    def get_trainee_by_id(self,trainer_id):
        self.filter_id_list_trainee = []
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainees"]
            for trainer in trainer_list:
                if trainer["traineeId"]==trainer_id:
                    self.filter_id_list_trainee.append(trainer)
        return self.filter_id_list_trainee
    def trainee_data_update(self,name,technology):
        update_field=input('enter which field you want to update:')
        if update_field=='name':
            for i in self.filter_name_list_trainee:
                user_input=input('enter the name  you want:')
            self.filter_name_list_trainee['name']=self.filter_name_list_trainee['user_input']
        elif update_field=='technology':
            for i in self.filter_technology_list:
                user_input_technology=input('enter the technology name:')
            self.filter_technology_list['technology']=self.filter_technology_list['user_input_technology']
        return self.filter_name_list_trainee,self.filter_technology_list
    def del_trainee(self,id):
        user_trainee_id=int(input('enter the id of the trainee you want to remove'))
        trainee_updated_id=self.filter_id_list_trainee.remove(user_trainee_id)
        with open("data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            self.filter_id_list_trainee=data['id'].update(trainee_updated_id)
      


while True:
    q = str(input("press and key to enter in institute management system or 'Q' for quit:"))
    if q.title()=="Q":
        print("thank you for using this program")
        break
    else:
        try:
            obj = Institute()
            choose = int(input("""
            Do You Want To Add Trainer or Trainee
            1 for Trainer
            2 for Traine
            enter the option:"""))
            if choose==1:
                name = str(input("enter the name:")).title()
                tech = str(input("enter the technology name:")).title()
                active = str(input("enter the status:"))
                obj.add_trainner(name,tech,active)
            elif choose==2:
                name = str(input("enter the name:")).title()
                tech = str(input("enter the technology name:")).title()
                date = datetime.datetime.today()
                joining_date = date.strftime("%b/%d/%Y")
                duration = int(input("enter the number of month for duration of course:"))+" Month"
                email = str(input("enter the email id:"))
                active = str(input("enter the status:"))
                obj.add_trainee(name,tech,joining_date,duration,email_id=email,active=active)
            else:
                print("""
                Do you want Get Trainer or Trainee
                1 for Trainer
                2 for Trainee
                """) 
                choose_get = int(input("enter the option:"))
                if choose_get == 1:
                    print("Welcome to Trainer Section")
                    time.sleep(2)
                    print("""
                    Do you wnat to get trainer by 
                    1 for name
                    2 for id
                    3 for technogy
                    """)
                    choose_trainer = int(input("enter option:"))
                    if choose_trainer==1:
                        name = str(input("enter the trainer name:")).title()
                        print(obj.get_trainer_by_name(name))
                    elif choose_trainer==2:
                        trainer_id = int(input("enter the id:"))
                        print(obj.get_trainer_by_id(trainer_id))
                    elif choose_trainer == 3:
                        tech_name =  str(input("enter the technology  name:")).title()
                        print(obj.get_trainee_by_technology(tech_name))
                    else:
                        print("please choose the correct option")
                elif choose_get == 2:
                    choose_trainee = int(input("enter option:"))
                    if choose_trainee==1:
                        name = str(input("enter the trainer name:")).title()
                        print(obj.get_trainee_by_name(name))
                    elif choose_trainee==2:
                        trainer_id = int(input("enter the id:"))
                        print(obj.get_trainee_by_id(trainer_id))
                    elif choose_trainee == 3:
                        tech_name =  str(input("enter the technology  name:")).title()
                        print(obj.get_trainee_by_technology(tech_name))
                    else:
                        print("please choose the correct option")
                else:
                    print("choose the correct option")
        except:
            print("choose correct option somthing went wrong")
    user_update=str(input('press enter to update the trainer or trainee details else press q to exit:'))
    if user_update=='q':
        break
    else:
        try:
            update_obj=Institute()
            input=int(input('''
            choose a option below:
            1.trainer
            2.trainee
            '''))
            if input==1:
                name=str(input('enter the trainer name:')).title()
                tech=str(input('enter the technology name'))
                update_obj.trainer_data_update(name,tech)
            elif input==2:
                name=str(input('enter the trainee name:')).title()
                tech=str(input('enter the technology name'))
                update_obj.trainee_data_update(name,tech)
            else:
                print('choose a correct option')
        except:
            pass
    user_del_update=str(input('press enter to delete and update the trainer or trainee details else press q to exit:'))
    if user_del_update=='q':
        break
    else:
        try:
            del_obj=Institute()
            input=int(input('''
            choose a option below:
            1.trainer
            2.trainee
            '''))
            if input==1:
                trainer_id1=int(input('enter the Id of the trainer:'))
                del_obj.del_trainer(trainer_id1)
            elif input==2:
                trainee_id1=int(input('enter the Id of trainee:'))
                del_obj.del_trainee(trainee_id1)
            else:
                print('choose a correct option')
        except:
            pass
    












    # name = str(input("enter the name:"))
    # tech = str(input("enter the technology name:"))
    # date = datetime.datetime.today()
    # joining_date = date.strftime("%b/%d/%Y")
    # duration = "1 month"
    # email = str(input("enter the email id"))

    # active = str(input("enter the status:"))

    # # obj.add_trainner(name,tech,active) 
    # obj.add_trainner(name,tech,active)
    # obj.add_trainee(name,tech,joining_date,duration,email_id=email,active=active)      

    
                



    
                    







