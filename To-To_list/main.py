Input = True
while True:
    try:
     int(input('''
              ===== TO-DO LIST =====
                1. Add Task
                2. View Tasks
                3. Remove Task
                4. Exit  '''))
    except ValueError as e:
     print(e)