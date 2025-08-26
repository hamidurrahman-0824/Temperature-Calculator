#simple temperature conversion
x = int(input("Press '1' for fahrenheit  to celcius, press'2' for clecius to fahrenheit:"))
if x==1:
    x1= int(input("Enter temperature in Fahrenheit:"))
    x2 = 0.56*(x1-32)
    print(f"{x2} is your temperature.")
  
elif x==2:
    x3= int(input("Enter temperature in Celcius:"))
    x4 = (1.8*x3)+32
    print(f"{x4} is your temperature")
else:
    print("Follow instruction.")

