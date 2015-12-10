def smrecica(n):
    z = 0
    x = n
    deblo = 0

    if n % 2 == 0:
        while deblo < 5:
            print ' ' * (n/4) + '*' * (n/2) + ' ' * (n/4)
            deblo += 1

    else:
        while deblo < 5:
            print ' ' * (n/3) + '*' * (n/2) + ' ' * (n/3)
            deblo += 1


    for i in range(n):
        print(' ' * z + '*' * x + ' ' * z)
        x-=2
        z+=1

def main():
    vnos = int(raw_input("Vnesi velikost kontrasmreke"))
    smrecica(vnos)

if __name__ == '__main__':
    main()

