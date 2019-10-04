#My first Python program
# print("Hello World!")
# print('Hello World!')
# print("My lucky numbers are:", 3*4+5, 5*6-1)

# print("balance after  one year:", 10000*1.05)
# print("balance after  two yeara:", 10000*1.05*1.05)

# print("years require to double", 72/5)


# #6 

# def double_balance (balance):
#     count = 0
#     finalBalance = balance * 2
#     while(balance < finalBalance):
#         balance = balance * 1.05
#         count += 1
#     return count

# print(double_balance(10000))

# class DoubleBalance:
#    def __init__(this,balance):
#     this.balance = balance

#    def double(this):
#      count = 0
#      finalBalance = this.balance * 2
#      while(this.balance < finalBalance):
#         this.balance = this.balance * 1.05
#         count += 1
#      return count

# balance1 = DoubleBalance(50000).double()
# print(balance1)



# #6.1
# def sum_all (num) :
#     sum = 0 
#     for x in num :
#         sum += x
#     return sum

# print(sum_all([1,2,3,4,5,6,7,8,9,10]))

# #class version
# class SumAll:
#   def __init__(this, num):
#    this.num = num
  
#   def sum(this):
#       sum = 0 
#       for x in this.num:
#           sum += x
#       return sum

# num1 = SumAll([1,2,3,4,5,6,7,8,9,20]).sum()
# print(num1)


# find out surface area to be painted
# doors and windows will not be painted

def house_dimensions (WindowsDim, DoorsDim, WindowsNum, DoorsNum, W, H, L ):
    WallsArea = 0
    DW  = (WindowsNum * WindowsDim + DoorsNum * DoorsDim)
    if L > 0:
     #Rectangle house
     WallsArea  = (W * H) * 2 + (L * H )* 2 - DW
    else:
        #Cube house
     WallsArea  = (W * H) * 4 - DW

    return WallsArea

print(house_dimensions( W = 15, L = 30, H = 10, WindowsDim = 3, DoorsDim = 4, WindowsNum = 2 , DoorsNum = 1 ))
 
