import mysql.connector as m
import tabulate as t

a = m.connect(host="localhost", user="root", password="", database="student")
b = a.cursor()


def add():
    try:
        adm = int(input("Enter admission number:"))
        b.execute(f'select * from data where s_adm="{adm}"')
        data = b.fetchall()
        # print(data)
        if data == []:
            name = input("Enter student name:")
            grade = input("Enter your class and section:")
            address = input("Enter your address:")
            b.execute(
                "Insert into data values('{}','{}','{}','{}')".format(
                    name, adm, grade, address
                )
            )
            a.commit()
            print("\n\t\t <<<<<---DATA HAS BEEN SAVED TO OUR RECORDS--->>>>>")
        else:
            print(
                "\n\t\t<<<<<---RECORD ALREADY FOUND FOR THIS ADMISSION NUMBER--->>>>>"
            )
            print("\t\t\t----PLEASE TRY AGAIN----")
    except ValueError:
        print("\n\t\t------ADMISSION NO. MUST BE AN INTEGER------\n")


def search():
    print(
        "\n\t\t------SEARCH MENU------\n1. Search by student name\n2. Search by admission number"
    )
    try:
        choice = int(input("Enter choice:"))
    except ValueError:
        print("\n\t\t------CHOICE. MUST BE AN INTEGER------\n")
    try:
        if choice == 1:
            name = input("Enter student name:")
            b.execute(f'Select * from data where s_name="{name}"')
            data = b.fetchall()
            if data == []:
                print("\t\t |******NO RECORDS FOUND******| ")
            else:
                print("\t\t |******RECORD FOUND******|")
                print(
                    t.tabulate(
                        data,
                        headers=["Student name", "Admission no.", "Class", "Address"],
                        tablefmt="pretty",
                    )
                )
        elif choice == 2:
            no = int(input("Enter admission number:"))
            b.execute(f'Select * from data where s_adm="{no}"')
            data = b.fetchone()
            print(data)
            if data == None:
                print("\t\t |******NO RECORDS FOUND******| ")
            else:
                print("\n\t\t |******RECORD FOUND******|\n")
                print(
                    "Student name=",
                    data[0],
                    "\nAdmission no.=",
                    data[1],
                    "\nClass=",
                    data[2],
                )
                print("Address=", data[3])
                print("\t\t |******RECORD FOUND******|")
        else:
            print("\n\t\t---------INVALID OPTION CHOSEN---------\n")
    except ValueError:
        print("\n\t\t------ADMISSION NO. MUST BE AN INTEGER------\n")
    except:
        print("\n\t\t**********UNKNOWN ERROR**********\n")


def delete():
    print(
        "\n\t\t------DELETE MENU------\n1. Delete by student name\n2. Delete by admission number"
    )
    choice = int(input("Enter choice:"))
    if choice == 1:
        name = input("Enter student name:")
        b.execute(f"Select * from data where s_name='{name}'")
        data = b.fetchall()
        print(data)
        if data == []:
            print("\n\t\t |******NO RECORDS FOUND******| ")
        else:
            print("\n\t\t |******RECORD FOUND******|\n")
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
            if len(data) > 1:
                adm = int(input("Enter admission number:"))
                b.execute(f"Select * from data where s_adm='{adm}'")
                dd = b.fetchall()
                print(dd)
                print(
                    t.tabulate(
                        dd,
                        headers=["Student name", "Admission no.", "Class", "Address"],
                        tablefmt="grid",
                    )
                )
                opt = input("\n\tDo you want to delete this record?(yes/no)")
                if opt.lower() == "yes":
                    a1 = dd[0][0]
                    a2 = dd[0][1]
                    a3 = dd[0][2]
                    a4 = dd[0][3]
                    b.execute(
                        "Insert into deleted values('{}','{}','{}','{}')".format(
                            a1, a2, a3, a4
                        )
                    )
                    b.execute(f"Delete from data where s_name='{name}'")
                    print("\n\t\t<<<<<<<<---RECORD HAS BEEN DELETED--->>>>>>>>\n")
                    a.commit()
            else:
                opt = input("\n\tDo you want to delete this record?(yes/no)")
                if opt.lower() == "yes":
                    a1 = data[0][0]
                    a2 = data[0][1]
                    a3 = data[0][2]
                    a4 = data[0][3]
                    b.execute(
                        "Insert into deleted values('{}','{}','{}','{}')".format(
                            a1, a2, a3, a4
                        )
                    )
                    b.execute(f"Delete from data where s_name='{name}'")
                    print("\n\t\t<<<<<<<<---RECORD HAS BEEN DELETED--->>>>>>>>\n")
                    a.commit()
    if choice == 2:
        adm = int(input("Enter admission number:"))
        b.execute(f"Select * from data where s_adm='{adm}'")
        data = b.fetchall()
        if data == []:
            print("\n\t\t |******NO RECORDS FOUND******| ")
        else:
            print("\n\t\t |******RECORD FOUND******|\n")
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
            opt = input("Do you want to delete this record?(yes/no)")
            if opt.lower() == "yes":
                a1 = data[0][0]
                a2 = data[0][1]
                a3 = data[0][2]
                a4 = data[0][3]
                b.execute(
                    "Insert into deleted values('{}','{}','{}','{}')".format(
                        a1, a2, a3, a4
                    )
                )
                b.execute(f"Delete from data where s_adm='{adm}'")
                print("\n\t\t<<<<<<<<---RECORD HAS BEEN DELETED--->>>>>>>>\n")
                a.commit()


def update():
    print("\n\t\t-----------UPDATE MENU-----------")
    print("1. Update by admission number\n2. Update by student name")
    choice = int(input("Enter choice:"))
    if choice == 1:
        no = int(input("Enter admission number:"))
        b.execute(f"Select * from data where s_adm='{no}'")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
            opt = input("Do you want to update this record? (yes/no)")
            if opt.lower() == "yes":
                print("\n\t\t<<<<<<<<<<---UPDATE MENU--->>>>>>>>>>")
                print(
                    "1. Update student name\n2. Update admission number\n3. Update class"
                )
                print("4. Update address\n5. Update all")
                opt1 = int(input("Enter choice:"))
                if opt1 >= 1 and opt1 <= 5:
                    if opt1 == 1:
                        name1 = input("Enter new student name:")
                        b.execute(
                            "Update data set s_name='{}' where s_adm='{}'".format(
                                name1, no
                            )
                        )

                    elif opt1 == 2:
                        adm = int(input("Enter new admission number:"))
                        b.execute(
                            "Update data set s_adm='{}' where s_adm='{}'".format(
                                adm, no
                            )
                        )

                    elif opt1 == 3:
                        c1 = input("Enter new class and section:")
                        b.execute(
                            "Update data set s_class='{}' where s_adm='{}'".format(
                                c1, no
                            )
                        )

                    elif opt1 == 4:
                        add = input("Enter new address:")
                        b.execute(
                            "Update data set s_address='{}' where s_adm='{}'".format(
                                add, no
                            )
                        )
                    elif opt1 == 5:
                        m = input("Enter new student name:")
                        n = int(input("Enter admission number:"))
                        o = input("Enter new class and section:")
                        p = input("Enter new address:")
                        b.execute(
                            "Update data set s_name='{}',s_adm='{}',s_class='{}',s_address='{}' where s_adm='{}'".format(
                                m, n, o, p, no
                            )
                        )
                    a.commit()
                    print("\n\t\t<<<<<<---RECORD UPDATED--->>>>>>\n")
                else:
                    print("\n\t\t*******INVALID OPTION SELECTED********\n")


def view():
    print("\n\t\t-----------VIEWING MENU-----------")
    print(
        "1. View in alphabetical order (BY NAME)\n2. View in ascending order (ADMISSION NO.)"
    )
    print(
        "3. View in descending order (ADMISSION NO.)\n4. View in original order\n5. View in class order"
    )
    choice = int(input("Enter choice:"))
    if choice == 1:
        print(
            "\n\t<<<<<<<<<<<<<---ALL RECORDS OF DATABASE IN ALPHABETICAL ORDER--->>>>>>>>>>>>>"
        )
        b.execute("Select * from data order by s_name")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
    if choice == 2:
        print(
            "\n\t<<<<<<<<<<<<<---ALL RECORDS OF DATABASE IN ASCENDING ORDER--->>>>>>>>>>>>>"
        )
        b.execute("Select * from data order by s_adm")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
    if choice == 3:
        print(
            "\n\t<<<<<<<<<<<<<---ALL RECORDS OF DATABASE IN DESCENDING ORDER--->>>>>>>>>>>>\n"
        )
        b.execute("Select * from data order by s_adm desc")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )

    if choice == 4:
        print(
            "\n\t<<<<<<<<<<<<<---ALL RECORDS OF DATABASE IN ORIGINAL ORDER--->>>>>>>>>>>>\n"
        )
        b.execute("Select * from data")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )
    if choice == 5:
        print(
            "\n\t<<<<<<<<<<<<<---ALL RECORDS OF DATABASE IN CLASS ORDER--->>>>>>>>>>>>>"
        )
        grade = input("Enter class and section:")
        b.execute(f"Select * from data where s_class='{grade}'")
        data = b.fetchall()
        if data == []:
            print("\n\t\t*******NO RECORDS FOUND*******\n")
        else:
            print(
                t.tabulate(
                    data,
                    headers=["Student name", "Admission no.", "Class", "Address"],
                    tablefmt="grid",
                )
            )


def export():
    a = input("Enter the name of the file:")
    a += ".csv"
    file = "C:\\Users\\totar\\OneDrive\\Desktop\\USERS FILES\\" + a
    import csv

    try:
        f = open(file)
        f.close()
        print("\n\t\t----THIS FILE IS ALREADY PRESENT IN OUR RECORDS----")
        print("\n\t\t****PLEASE TRY AGAIN WITH ANOTHER NAME****")
    except:
        columns = ["Student name", "Admission no.", "Class & Section", "Address"]
        f = open(file, "a", newline="")
        b.execute("Select * from data")
        data = b.fetchall()
        data.insert(0, columns)
        xx = csv.writer(f)
        xx.writerows(data)
        f.close()
        print("\n\t\t<<<<<<<<<", a, "FILE IS CREATED>>>>>>>>>")
        print("\n", a, " IS SAVED AT LOCATION:   ", file)


def restore():
    print("\n\t\t<<<<<<<<---RESTORE MENU--->>>>>>>>>\n1. Restore by student name")
    print("2. Restore by admission number")
    choice = int(input("Enter choice:"))
    if choice == 1:
        name = input("Enter student name:")
        b.execute(f"Select * from deleted where s_name='{name}'")
        data = b.fetchall()
        if data == []:
            print("\n\t*********NO RECORDS FOUND*********")
        else:
            for i in data:
                dd = [[i[0], i[1], i[2], i[3]]]
                print(
                    t.tabulate(
                        dd,
                        headers=[
                            "Student name",
                            "Admission no.",
                            "Class & Section",
                            "Address",
                        ],
                        tablefmt="grid",
                    )
                )
                ch = input("Type yes if you want this record to be restored:")
                if ch.lower() == "yes":
                    b.execute(
                        "Insert into data values('{}','{}','{}','{}')".format(
                            i[0], i[1], i[2], i[3]
                        )
                    )
                    b.execute(f"Delete from deleted where s_adm='{i[1]}'")
                    a.commit()
                    print("\n\t--------DATA HAS BEEN RESTORED--------")
                    break
    elif choice == 2:
        try:
            adm = int(input("Enter admission number:"))
            b.execute(f'Select * from deleted where s_adm="{adm}"')
            d = b.fetchall()
            if d == []:
                print("\n\t*********NO RECORDS FOUND*********")
            else:
                a1 = d[0][0]
                a2 = d[0][1]
                a3 = d[0][2]
                a4 = d[0][3]
                print(
                    t.tabulate(
                        d,
                        headers=[
                            "Student name",
                            "Admission no.",
                            "Class and Section",
                            "Address",
                        ],
                        tablefmt="grid",
                    )
                )
                ch = input("Do you want to restore this record? (yes/no)")
                if ch.lower() == "yes":
                    b.execute(
                        "Insert into data values('{}','{}','{}','{}')".format(
                            a1, a2, a3, a4
                        )
                    )
                    b.execute(f"Delete from deleted where s_adm='{adm}'")
                    a.commit()
                    print("\n\t--------DATA HAS BEEN RESTORED--------")
        except ValueError:
            print("\n\t\t------ADMISSION NO. MUST BE AN INTEGER------\n")
