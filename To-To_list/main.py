while True:
    try:
     choice = int(input('''
        ===== TO-DO LIST =====
          1. Add Task
          2. View Tasks
          3. Remove Task
          4. Exit  '''))
     try:
      with open("Text.txt","r") as file:
       Task = [line.strip() for line in file]
     except FileNotFoundError:
       with open("Text.txt","w") as file:
        Task = []
         
     match(choice):
       case 1 :
         task = input("Enter the task you want to add: ")
         Task.append(task)
         print(f"task is added to file")

       case 2:
         for i,task in enumerate(Task,start =1):
          print(f"{i}.{task}")
       case 3 :
         for i,task in enumerate(Task,start =1):
          print(f"{i}.{task}")
         try:
           n =int(input("enter the number of above task to remove:"))
           Task.pop(n-1)
         except ValueError as e:
            print("you have enterd some wrong input",e)
       case 4:
         print("YOU were exiting from program")
         break
       case _:
         print("Enter wrong Input Try again")
     with open("Text.txt","w") as file:
          file.writelines(line + "\n" for line in Task)
    except ValueError as e:
      print("you have enterd some wrong input",e)