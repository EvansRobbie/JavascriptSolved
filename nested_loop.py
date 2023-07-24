# nested loops - these are loops inside other loops

# rectangle
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the Symbol to use: ")

for i in range(rows):
    # print(symbol, end="")
    for j in range(columns):
        print(symbol, end="")
    print()
