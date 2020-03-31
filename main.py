"""
=======================================================================
|                                  Planner                             |
|                                  -------                             |
|    A school  management system that helps you organizing             |
|    your schedules, agendas for the homeworks, quizzes, and subjects. |
|    The system lets you enter the subjects you have, the schedule, the|
|    the homeworks or quizzes and it will show you daily your agenda   |
|    based on what you entered.You will be able to store teacher's     |
|    information like emails, his/her office and the office hours.     |
|                                                                      |
=======================================================================
"""
_author_ = "Guy Cherubin Ntajugumba"
_version_ = '1.0'

# Everything to import
##########################
from Subject import *
##########################


# To welcome the user with the app title
def app_title():
    print(30 * " ", end='')
    print(17 * "-", end='')
    print(30 * " ")
    print(30 * " ", end='|')
    print(4 * " ", end='')
    print("Planner", end='')
    print(4 * " ", end='|')
    print(30 * " ")
    print(30 * " ", end='')
    print(17 * "-", end='')
    print(30 * " ")


# To show the menu selection and prompt the user to choose
def user_menu():
    print(18 * " ", end='')
    print("\t1. Show Schedule", end='')
    # print(8 * " ", end='')
    print("\t\t2. Show Agenda")
    print(18 * " ", end='')
    print("\t3. Add Homework/Quiz", end='')
    # print(8 * " ", end='')
    print("\t4. Add Schedule")
    print(18 * " ", end='')
    print("\t5. Add teacher\t", end='')
    # print(8 * " ", end='')
    print("\t\t6. Add Subject")
    print(35 * " ", end='')
    print("7. Exit")


class Main:
    __doc__ = "Manages the user inputs and everything related to what is " \
              "shown to the user."

    def __init__(self):
        app_title()
        self.run = True
        self.subject = Subject()

    # To prompt the user to choose from menu selection
    def get_user_choice(self):
        while self.run:
            user_menu()
            choice = int(input("Choice: "))
            if choice not in range(1, 8):
                print('Wrong choice!')
            elif choice == 1:
                print("Show Schedule")
            elif choice == 2:
                print("Show Agenda")
            elif choice == 3:
                print("Add Homework/Quiz")
            elif choice == 4:
                print("Add Schedule")
            elif choice == 5:
                subject_id = input("Enter the Subject Id: ")
                self.subject.get_subject(subject_id)
            elif choice == 6:
                self.subject.add_subject()
            elif choice == 7:
                print("Thank you for using our Program!See you soon")
                break


if __name__ == '__main__':
    main = Main()
    main.get_user_choice()
