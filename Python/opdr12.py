def weer_app():
    while True:
        print("*" * 50)
        print()
        print("Welkom bij de weer app")
        print("Wat wilt u doen:")
        print("      1. weerstatistieken")
        print("      2. actuele weer")
        print("      3. weerbericht")
        print("Of druk q om te stoppen")
        print()
        print("*" * 50)

        keuze = input("? ").strip().lower()

        if keuze == 'q':
            print("Afgesloten")
            break
        if keuze == '1':
            print("dit zijn de weerstatistieken")
            break
        if keuze == '2':
            print("Het weer is: ugh")
            break
        if keuze == '3':
            print("weerbericht: W.I.P")
            break
weer_app()

