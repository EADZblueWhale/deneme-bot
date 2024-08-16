import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifreniz kaç karekterden oluşsun istersiniz?"))


password = ""
for i in range(sayi):
    password += random.chice(karakterler)


print("Şifreniz:" password)


if password=="admin":
    print("bu şifreyi kullanamazsınız")
