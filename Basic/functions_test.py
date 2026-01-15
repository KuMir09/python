def my_table():
    num=int(input("Enter the number to get the table: "))
    for i in range(1, 11):
        print(num,"x",i,"=",i*num)

my_table()