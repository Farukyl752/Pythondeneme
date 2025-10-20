semboller = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
i = 0

def tahta_yazdi():
    print(f"{semboller[0]} | {semboller[1]} | {semboller[2]}")
    print("---------")
    print(f"{semboller[3]} | {semboller[4]} | {semboller[5]}")
    print("---------")
    print(f"{semboller[6]} | {semboller[7]} | {semboller[8]}")

def kazanan_var_mi(sembol):
    kazanma_kombinasyonlari = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # satırlar
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # sütunlar
        [0, 4, 8], [2, 4, 6]              # çaprazlar
    ]
    for combo in kazanma_kombinasyonlari:
        if semboller[combo[0]] == semboller[combo[1]] == semboller[combo[2]] == sembol:
            return True
    return False

def oyun():
    global i
    if i % 2 == 0:
        index = input("1. oyuncu hangi indexe işaret koymak istiyor (0-8): ")
        semboller[int(index)] = "X"
    else:
        index = input("2. oyuncu hangi indexe işaret koymak istiyor (0-8): ")
        semboller[int(index)] = "O"
    i += 1
    tahta_yazdi()

print("X | O | X oyununa hoşgeldiniz!")
tahta_yazdi()

while True:
    oyun()
    if kazanan_var_mi("X"):
        print("1. oyuncu kazandı! 🎉")
        break
    elif kazanan_var_mi("O"):
        print("2. oyuncu kazandı! 🎉")
        break
    elif i == 9:
        print("Oyun bitti! Berabere 🤝")
        break

    

      
   
