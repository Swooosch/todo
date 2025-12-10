mina_uppgifter = []

while True:
    print("\n----------------")
    print("Välkommen till Att-göra-listan!")
    print("1. Visa uppgifter")
    print("2. Lägg till uppgift")
    print("3. Avsluta programmet")
    print("------------------")

    val = input("Välj ett alternativ (1, 2 eller 3): ")

    if val == '1':
        print("Visar uppgifter: ")
        if not mina_uppgifter:
            print("Du har inte lagt till några uppgifter")
        
        else:
            for index, uppgift in enumerate(mina_uppgifter):
                print(f"{index + 1}. {uppgift}")

    elif val == '2':
        ny_uppgift = input("Lägg till uppgift: ")
        if ny_uppgift:
            mina_uppgifter.append(ny_uppgift)
            print(f"'{ny_uppgift}' har lagts till!")

        else:
            print("Du angav ingen text!")
    
    elif val == '3':
        print("Avslutar. Hej då!")

    else:
        print("Ogiltigt val. Vänligen välj 1, 2 eller 3.")