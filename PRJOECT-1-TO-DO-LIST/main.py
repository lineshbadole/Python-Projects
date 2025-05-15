
# To Do List Application

# This is a simple command-line to-do list application that allows users to add, view, and delete tasks.

#Set variables 

user_prompt = 'Enter Your To Do Task:'

to_do_list = []
file = open('files/todo.txt','r')
to_do_list = file.readlines()
file.close()

while True:
    print('\n\n\n ************* TO DO LIST *************** \n\n')
    user_action = input("What would you like to do: \n  1] ADD \n  2] SHOW the list \n  3] EDIT an existing TASK \n  4] Complete the Task \n  5] Exit \n\n Enter your choice:  ")

    user_action = user_action.strip()

    match user_action:
        case 'add' | '1' | 'Add' | 'ADD':
            task = input('\n Enter a task: ') + '\n'

 
            to_do_list.append(task)

            file = open('files/todo.txt', 'w')
            file.writelines(to_do_list)
            file.close()
    
        case 'show' | '2' | 'Show' | 'SHOW':
            print('\n\n\n ************ Tasks in the LIST *********** ')
            if len(to_do_list) == 0:
                print('NO TASK in the list. Please Add or Exit\n\n\n')
            
            for i, task in enumerate(to_do_list, start=1):
                print(f'{i}] {task.strip('\n')}')
  
        case 'edit' | '3' | 'EDIT' | 'Edit':
            task_no = input('\n\n Which Task would you like to EDIT (please input task number) : ')
            index = int(task_no) - 1
            
            new_task = input('\n\n Enter the new task: ')
            old_task = to_do_list[index]
            to_do_list[index] = new_task

            print(f'\n\n SUCCESS: The Task has been updated \n')
            
            for i, task in enumerate(to_do_list, start=1):
                print(f'{i}] {task}')

        case 'complete' | '4' | 'Complete' | 'COMPLETE':
            task_no = input('\n\n Which Task would you like to mark COMPLETE (please input task number) : ')
            index = int(task_no) - 1

            to_do_list.pop(index)
            
            print(f'\n\n SUCCESS: The Task is complete. Here is the updated list \n')
            
            for i, task in enumerate(to_do_list, start=1):
                print(f'{i}] {task}')

        case 'exit' | '5' | 'Exit' | 'EXIT' | 'stop':
            break

        case _:
            print('Enter a valid option')


print("\n\n ********** Thanks for using the To Do List ********** \n\n")
    

     


