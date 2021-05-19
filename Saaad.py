sport=["Sport ID","Sport Name","No.of Person","Location","Status"]
member=["Member ID","Name","Contact Number","Type","Day"]
def sports():
    choice =-1
    while choice !=5:
        print("1-Add Sport Record\n2-View Sport Record\n3-Search Record\n4-Edit Record\n5-Main Menu")
        choice=eval(input("Enter your choice:"))
        if choice==1:
            confirm ="y"
            while confirm=="y":
                id=eval(input("Enter Sport ID: "))
                for p in range(5, len(sport), 5):
                    if id == sport[p]:
                        print("ID is Already Entered")
                        id = eval(input("Enter Sport ID: "))
                        p = 5
                sport.append(id)
                sport_n=input("Enter Sport Name:")
                for j in range(1,len(sport),5):
                    if sport_n == sport[j]:
                        print("Already Entereded")
                        sport_n = input("Enter Sport Name: ")
                        j = 1
                sport.append(sport_n)
                sport.append(eval(input("Enter Team Members:")))
                location=input("Enter Location: ")
                for k in range(3,len(sport),5):
                    if location == sport[k]:
                        print("Already Entered")
                        location=input("Enter Location: ")
                        k=3
                sport.append(location)
                sport.append("Available")
                confirm=input("Press y to Add record Again.")
        elif choice ==2:
            if len(sport) < 10:
                print("Please Add Record First")
            else:
                for i in range(0,len(sport),5):
                    print(sport[i],"\t\t",sport[i+1],"\t\t",sport[i+2],"\t\t",sport[i+3],"\t\t",sport[i+4])
        elif choice == 3:
            if len(sport) < 10:
                print("Please Add Record First")
            else:
                confirm="y"
                while confirm=="y":
                    search = eval(input("Enter Game ID:"))
                    for i in range (0, len(sport), 5):
                        if search == sport[i]:
                            print("Sport ID","\t\t","Sport Name","\t\t","Team Members","\t\t","Day", "\t\t", "Status")
                            print(sport[i],"\t\t",sport[i + 1],"\t\t",sport[i+2],"\t\t",sport[i+3], "\t\t", sport[i+4])
                            break
                        elif i == len(sport) - 5:
                            print("ID Not Found")
                    confirm=input("Press y to search again: ")
        elif choice == 4:
            if len(sport) < 10:
                print("Please Add Record First")
            else:
                confirm="y"
                while confirm=="y":
                    search = eval(input("Enter Game ID:"))
                    for i in range (0, len(sport), 5):
                        if search == sport[i]:
                            id=eval(input("Enter Sport ID: "))
                            for p in range(5, len(sport), 5):
                                if sport[i] != id and id == sport[p]:
                                    print("ID is Already Entered")
                                    id = eval(input("Enter Sport ID: "))
                                    p = 5
                            sport[i] = id
                            sport_n=input("Enter Sport Name:")
                            for j in range(1,len(sport),5):
                                if (sport_n == sport[j]):
                                    print("Already Entereded")
                                    sport_n = input("Enter Sport Name: ")
                                    j=1
                            sport[i+1] = sport_n
                            sport[i+2] = eval(input("Enter Team Members:"))
                            location=input("Enter Location: ")
                            for k in range(3,len(sport),5):
                                if location != sport[i+3] and location == sport[k]:
                                    print("Already Entered")
                                    location=input("Enter Location: ")
                                    k=1
                            sport[i+3] = location
                            sport[i+4] = "Available"
                            break
                        elif i == len(sport) - 5:
                            print("ID Not Found")
                    confirm = input("Press y to edit again")
        else:
            print("Enter Valid Choice")
def mem():
    choice=-1
    while choice!=5:
        print("1-Add Record\n2-View Record\n3-Search Record\n4-Edit Record\n5-Main Menu")
        choice=eval(input("Enter your choice: "))
        if choice ==1:
            confirm="y"
            while confirm=="y":
                id=eval(input("Enter Member ID:"))
                while id in member:
                    print("Id is already taken")
                    id=eval(input("Enter Member ID:"))
                name=input("Enter Member name:")
                cnumber=input("Enter Contact Number:")
                print("Please Select one option")
                for i in range(6,len(sport),5):
                    print(sport[i])
                check = True
                error = False
                while check:
                    if error:
                        print("Please Enter Valid Option")
                    mtype=input("Enter your choice:")
                    for j in range(6,len(sport),5):
                        if mtype == sport[j] and not(mtype in member):
                            sport[j + 3] = "Reserved"
                            check = False
                            break
                        else:
                            error = True
                day=input("Enter Day:")
                member.append(id)
                member.append(name)
                member.append(cnumber)
                member.append(mtype)
                member.append(day)
                confirm=input("press y to add record again:")
        elif choice==2:
            if len(member) < 10:
                print("Please Add Record First")
            else:
                for i in range(0,len(member),5):
                    print(member[i],"\t\t",member[i+1],"\t\t",member[i+2],"\t\t\t",member[i+3],"\t\t",member[i+4])
        elif choice == 3:
            if len(member) < 10:
                print("Please Add Record First")
            else:
                confirm="y"
                while confirm=="y":
                    search = eval(input("Enter Game ID:"))
                    for i in range (0, len(member), 5):
                        if search == member[i]:
                            print("Member ID","\t\t","Member Name","\t\t","Contact Number","\t\t","Type", "\t\t", "Day")
                            print(member[i],"\t\t",member[i + 1],"\t\t",member[i+2],"\t\t",member[i+3], "\t\t", member[i+4])
                            break
                        elif i == len(member) - 5:
                            print("ID Not Found")
                    confirm=input("Press y to search again: ")
        elif choice == 4:
            if len(member) < 10:
                print("Please Add Record First")
            else:
                confirm="y"
                while confirm=="y":
                    search = eval(input("Enter Member ID:"))
                    for i in range (0, len(member), 5):
                        if search == member[i]:
                            id=eval(input("Enter New Member ID: "))
                            for p in range(5, len(member), 5):
                                if member[i] != id and id == member[p]:
                                    print("ID is Already Entered")
                                    id = eval(input("Enter Member ID: "))
                                    p = 5
                            member[i] = id
                            sport_n=input("Enter Member Name:")
                            member[i+1] = sport_n
                            member[i+2] = input("Enter Contact Number:")
                            print("Please Select one option")
                            for l in range(6,len(sport),5):
                                print(sport[l])
                            check = True
                            error = False
                            while check:
                                if error:
                                    print("Please Enter Valid Option")
                                mtype=input("Enter your choice:")
                                for j in range(6,len(sport),5):
                                    if member[i+3] == mtype or (mtype == sport[j] and not(mtype in member)):
                                        sport[j + 3] = "Reserved"
                                        check = False
                                        break
                                    else:
                                        error = True

                            member[i+3] = mtype
                            member[i+4] = input("Enter Number of Days:")
                            break
                        elif i == len(member) - 5:
                            print("ID Not Found")
                    confirm = input("Press y to edit again")
        else:
            print("Enter Valid Choice")
def view():
    conform="y"
    while conform=="y":
        print("1-Check Availabily of Sports\n2-Reserve of Sports")
        vchoice=eval(input("Enter your choice:"))
        if vchoice==1:
            for i in range(4,len(sport),5):
                if sport[i]=="Reserve":
                    continue
                print(sport[i-4],"\t\t", sport[i-3],"\t\t",sport[i-2],"\t\t",sport[i-1],"\t\t",sport[i])
        elif vchoice==2:
            for i in range(0,len(sport),5):
                for j in range(0, len(member), 5):
                    if (member[j + 3] == sport[i + 1]):
                        k = j
                if sport[i + 4] == "Reserved" or sport[i + 4] == "Status":
                    if (sport[i + 4] == "Status"):
                        k = 0
                    print(sport[i],"\t\t", sport[i+1],"\t\t",sport[i+2],"\t\t",sport[i+3],"\t\t",sport[i+4], "\t\t", member[k], "\t\t", member[k + 1], "\t\t", member[k + 2], "\t\t\t", member[k + 3], "\t\t", member[k + 4])
        else:
            print("Enter Valid Choice")
        conform=input("Press y to view again:")

def main():
    check_record=False
    check=True
    choice=-1
    while choice!=4:
        print("1-Add Sport record\n2-Add Member Record\n3-View Record\n4-Exit")
        choice=eval(input("Enter your choice:"))
        if choice==1:
            check_record=True
            sports()
        elif choice==2:
            if check_record==False:
                print("Please Enter Record First")
            else:
                mem()
        elif choice==3:
            if check_record==False:
                print("Please Enter Record First")
            else:
                view()
        elif choice==4:
                print("Program Terminates Here!")
                break
        else:
            print("Enter Valid Choice")

main()
