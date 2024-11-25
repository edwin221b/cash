def minimum_coins():
    coins_available = [25, 10,5,1]
    
    while True:
        user_input=input("change owed: ")
        try:
            owed_money = float(user_input)
            if owed_money >=0 :
                break
            print('only postive number allowed, try again')
        except:
            print('only postive number allowed, try again')

    owed_in_cents = round(owed_money*100)
    coins_available = [25, 10,5,1]


    total_coins = 0
    for i in coins_available:
        total_coins += owed_in_cents//i
        
        owed_in_cents %= i
    
    print(total_coins)

minimum_coins()