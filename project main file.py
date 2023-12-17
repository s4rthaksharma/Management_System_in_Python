import functions as m

while True:
    print("\n\t |----------BHARATIYA VIDYA BHAVAN MANAGEMENT SYSTEM----------|")
    print("\n\t\t\t----MENU----")
    print(
        "1. Add student details\n2. Search student details\n3. Delete student details"
    )
    print(
        "4. Update student details\n5. View all students\n6. Export student details to a file"
    )
    print("7. Restore option\n8. Exit")
    choice = int(input("\t\t----ENTER OPTION----"))
    if choice == 1:
        m.add()
    elif choice == 2:
        m.search()
    elif choice == 3:
        m.delete()
    elif choice == 4:
        m.update()
    elif choice == 5:
        m.view()
    elif choice == 6:
        m.export()
    elif choice == 7:
        m.restore()
    elif choice == 8:
        print("\n\t |---------------THANKS FOR USING THE SYSTEM---------------|")
        break
    else:
        print("\n\t\t********INVALID OPTION CHOOSEN********")
