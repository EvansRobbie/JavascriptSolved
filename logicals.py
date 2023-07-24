# logical operators (or, and , not )
temp = int(input("what is the temperature outside? "))

if temp >= 0 and temp <= 20:
    print("Too cold today")
elif temp >=21 or temp <=25:
    print("the weather is atleast")
else:
    print('you can go out and play')