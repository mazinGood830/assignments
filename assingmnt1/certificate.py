def certificate():
    name=input("enter your name: ")
    sub1=int(input(f"enter sub1 grade: "))
    sub2=int(input(f"enter sub2 grade: "))
    sub3=int(input(f"enter sub3 grade: "))
    sub4=int(input(f"enter sub4 grade: "))
    sub5=int(input(f"enter sub5 grade: "))
    print("name: ", (name))
    sum=sub1+sub2+sub3+sub4+sub5
    ave=sum/5
    print("your average is: ", (ave), "%")

certificate()
