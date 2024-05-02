#coderchef codes(elephant):
x=int(input("enter the value:"))
if(x<5):
  print("1 step")
elif(x%5==0):
  x/5
  print("2 step")
else:
  x//5+1
  print("3 step")