# This program will read in a file of fifteen US academic libraries and their technology services
# We will print the libraries' name, the number of technology services offered, Technology service maturity (TSM) percentage, and TSM level

# Explain the purpose of this program
def main():
    print("This program looks at how many technology services are offered by fifteen US academic libraries and calculates their technology service maturity (TSM)")

if __name__ == "__main__":
    main()

# Open the library technology services records file
libdata = open('libraries.csv', 'r')

# Skip the header row and read from line 2
def skiprow():
    next(libdata)
    
skiprow()

# Split lines
for line in libdata:
    librarydata = line.split(',')
    librarydata[-1] = librarydata[-1].rstrip('\n')

# Distinguish the name of the libraries and their services
    name = librarydata[0]
    services = librarydata[-23:]

# Calculate the number of technology services offered by the libraries
    num = 0
    total = 23
    for offer in services:
        if offer == 'O':
            num += 1

# Calculate TSM percentage
    maturity = num/total*100

# Print the libraries' name, the number of technology services offered, TSM percentage
# Here TSM means the breadth of technology services
# The higher the TSM percentage is, the more services the libraries offer
    print(f"\n***** {name} *****")
    print(f"The number of technology services is {num}")
    print(f"The technology service maturity (TSM) is {maturity:,.2f}")

# Group by TSM level
    levels = ('Extensive', 'Developing', 'Basic', 'None')

# Print TSM level
    if maturity >= 50:
        print(f"TSM level: {levels[0]}")
    elif maturity >= 20 and maturity < 50:
        print(f"TSM level: {levels[1]}")
    elif maturity > 0 and maturity < 20:
        print(f"TSM level: {levels[2]}")
    else:
        print(f"TSM level: {levels[3]}")

# Close the file
libdata.close()
