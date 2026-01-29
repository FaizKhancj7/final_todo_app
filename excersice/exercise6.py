Name = input("enter the name to be added: ")
file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

members.append(Name)
file = open("../files/members.txt", 'w')
file.writelines(members)
file.close
