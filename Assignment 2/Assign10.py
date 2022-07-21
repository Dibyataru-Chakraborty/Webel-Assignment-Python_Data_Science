#Write a python script to accept marks of five subjects from user(Assuming a maximum mark is 100). Display Student's result as pass or fail. if the student pass then also display his percentage and division
sub1=int(input("Enter 1st Subject number: "))
sub2=int(input("Enter 2nd Subject number: "))
sub3=int(input("Enter 3rd Subject number: "))
sub4=int(input("Enter 4th Subject number: "))
sub5=int(input("Enter 5th Subject number: "))
sub=sub1 + sub2 + sub3 + sub4 + sub5
per=sub/5
if (sub1 and sub2 and sub3 and sub4 and sub5)<=100:
    if sub>145:
        print("Result: pass")
        if per>=90:
            print("Percentage: {0}\n Grade: A+".format(per))
        elif per>=80:
            print("Percentage: {0}\n Grade: A".format(per))
        elif per>=60:
            print("Percentage: {0}\n Grade: B+".format(per))
        elif per>=40:
            print("Percentage: {0}\n Grade: B".format(per))
        elif per>=20:
            print("Percentage: {0}\n Grade: c".format(per))
    else:
        print("Percentage: {0}\n Result: fail".format(per))
else:
    print("subject number cannot greater than 100")