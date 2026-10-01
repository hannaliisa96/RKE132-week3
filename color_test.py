from colorama import Fore, Style
#Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi ja väljastab selle põhjal tema temperamendi.

#lilla --> armas
#roosa --> sõbralik
#sinine --> rahulik
#must --> salapärane
#muud --> unikaalne

color = input("sisesta oma lemmikvärv:").lower() #LILLA --> lilla

""" if color == "lilla":
    print("Oled armas")
elif color == "roosa":
    print("Oled sõbralik")
elif color == "sinine":
    print("Oled rahulik")
elif color == "must":
    print("Oled salapärane")
else:
    print("Oled unikaalne") """

match color:
    case "lilla":
        print(Fore.MAGENTA + "Oled armas" + Style.RESET_ALL)
    case "roosa":
        print(Fore.PINK + "Oled sõbralik" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Oled rahulik" + Style.RESET_ALL)
    case "must":
        print(Fore.BLACK + "Oled salapärane" + Style.RESET_ALL  )
    case _:
        print(Fore.WHITE + "Oled unikaalne" + Style.RESET_ALL)



