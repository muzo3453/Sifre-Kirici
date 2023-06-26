#kaç denemede buldu, kaç saniyede buldu, basamak +1, aynı kombinasyonları tahmin etmesin, denenilen kombinasyonları gösterme, tahmin yanlışsa remove from liste, if list karakter sayısı 0 ise basamak arttır, yasaklı harfler ö ğ
#kullanmak için key
#popüler şifreler için farklı dosya
import mihribankartal246

import random
import time

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'x', 'w', 'q']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z', 'X', 'W', 'Q',  ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolls=['*', "'", '"', '!', '#', '$', '+', '%', '&', '/', '{', '}', '(', ')', '[', ']', '=', '?', '-', '_', '-', '<', '>', '|', '.', ',', ':', ';', '~', '^', '´', '`', ' ']

mrt = lower_letters + upper_letters + numbers + symbolls

try:

    while True:
        tahmin = ''
        deneme_sayisi = 0
        basamak = 1
        combined = mrt
        kirilacak = input('harf. ')

        while tahmin != kirilacak:

            for i in range(basamak):
                # tahmin = random.choice(combined, k=2)
                if basamak == 1:
                    tahmin = random.choice(combined)
                    combined.remove(tahmin) # cannot choose from empty sequence hatası
                    combinations_left = len(combined)
                #if basamak <= 1:
                #    tahmin = random.choice(combined)
                deneme_sayisi += 1

            if tahmin != kirilacak:
                if len(combined) == 0:
                    basamak += 1
                    print('----------')
                    print(f'Yeni basamak sayısı: {basamak}')
                    input('----------')

            if tahmin == kirilacak:
                print('----------')
                print('Şifre kırıldı.')
                print(f'{tahmin} | deneme sayısı: {deneme_sayisi}')
                print('----------')
                input()
                os.system("cls")

except Exception as e:
    print(e)
    input()
