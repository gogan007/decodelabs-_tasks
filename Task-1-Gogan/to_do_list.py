task=[];
while(True):
    print("\n\n----TO DO List----");
    print("1.Add Task");
    print("2.Remove Task");
    print("3.Show All Task");
    print("4.Exit");
    choice = input("Enter Your Choice:");
    
    if choice=="1":
        t=input("Enter Your Task:");
        task.append(t);
        
    elif choice=="2":
        try:
            r=int(input("Enter Number Of Task You Want To Remove:"));
            if len(task)<r or r<1:
                raise IndexError("Invalid task number!");
            else:
                removed = task.pop(r - 1);
                print("Removed:", removed);
        
        # Swapped these around so the specific error catches first!
        except IndexError as e:
            print(e);
        except Exception as e:
            print("Invalid!");

    elif choice=="3":
        if len(task) == 0:
            print("No tasks available.");
        else:
            print("\nYour Tasks:");
            for i, t in enumerate(task, start=1):
                print(i, t);
                
    elif choice=="4":
        print("Exit Program...");
        break;
        
    else:
        print("Enter Valid Task.");
        continue;