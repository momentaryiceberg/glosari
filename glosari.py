import os
import subprocess
from datetime import datetime

# Dagsetningarformat
nuna = datetime.now().strftime('%Y %b %d, %H:%M')

# Desktop slóð, virkar á hvaða Windows tölvu sem er
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# TODO - Gera þennan fæl default og að hægt sé að gera nýjan, með custom nafni
filenafn = "timaglos.txt"

# Desktop slóð og filenafn sameinað
glos_path = os.path.join(desktop, filenafn)


# Opnar fælinn. Býr hann til ef ekki til.
def opna_glos():
    with open(glos_path, 'a', encoding='utf-8') as f:
        pass
    subprocess.run(['python', glos_path])

# Hinn raunverulegi glósari :)
def glosari():
    glosun = input("Til glósunar: ")
    with open(glos_path, 'a', encoding='utf-8') as f:
        f.write(f"{nuna} - {glosun}")
    print("Glósað!")


def main():
    while True:
        print("\ns = Sjá fæl")
        print("g = Glósa")
        print("q = Hætta\n")
        user_input = input("Veldu hvað: ")
        if user_input.lower() == 'q':
            print("Hættir...")
            break
        elif user_input.lower() == 's':
            opna_glos()
        elif user_input.lower() == 'g':
            glosari()
        else:
            print(f"'{user_input}' virkar ekki. Veldu aftur.")


if __name__ == "__main__":
    main()