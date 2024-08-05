# nested loop is nothing just a loop inside another loop

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for row in range(rows):
    for col in range(cols):
        print(symbol, end="")
    print()  # or print("\n", end="")
