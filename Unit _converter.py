while True:
    print("\nWelcome To A Unit Converter App. Choose any option from the below")
    print("1. Kilometer To Miles")
    print("2. Miles to Kilometer")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")
    print("5. Litres to Gallons")
    print("6. Gallons to Litres")
    print("7. Celsius to Fahrenheit")
    print("8. Fahrenheit to Celsius")
    print("9. Exit")

    choice = input("Enter any choice (1-9): ")

    if choice == '9':
        print("Thank you for using the Unit Converter App!")
        break

    value = float(input("Enter any value to convert: "))

    if choice == '1':
        print(f'{value} Kilometer is equal to {value * 0.62137119} Miles')

    elif choice == '2':
        print(f'{value} Miles is equal to {value / 0.62137119} Kilometers')

    elif choice == '3':
        print(f'{value} Kilogram is equal to {value * 2.2046} Pounds')

    elif choice == '4':
        print(f"{value} Pound is equal to {value / 2.2046} Kilograms")

    elif choice == '5':
        print(f'{value} Litres is equal to {value * 0.264172} Gallons')

    elif choice == '6':
        print(f'{value} Gallons is equal to {value / 0.264172} Litres')

    elif choice == '7':
        print(f"{value} Celsius is equal to {(value * 9/5) + 32} Fahrenheit")

    elif choice == '8':
        print(f'{value} Fahrenheit is equal to {(value - 32) * 5/9} Celsius')

    else:
        print("Invalid option. Please select between 1 - 9")