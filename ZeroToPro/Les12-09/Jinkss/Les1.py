walletBTC = 0.0
bankAcc = 100.0

lvl1card = 1
lvl2card = 0
lvl3card = 0

sellingRate = 21980.65


print("У вас есть 1 видеокарта мощностью 0.1BTC/Day")

while True:
	print("Что вы хотите сделать?")
	userChoise = input("Намайнить(1)/Продать(2)/Купить видеокарты(3)/Купить BTC(4))/Выход(0): ")

	if userChoise=="1":
		print("Майнинг запущен на 1 день... На всех ваших "+str(lvl1card+lvl2card+lvl3card)+ " видеокартах" )
		walletBTC+=(0.1*lvl1card)
		walletBTC+=(0.15*lvl2card)
		walletBTC+=(0.25*lvl3card)
		walletBTC = round(walletBTC, 6)
		print("Резутат на вашем кошельке = "+str(walletBTC))
	elif userChoise=="2":
		print("Процесс продажи запущен...")
		BTCforSale = input("Сколько вы хотите продать? Bal:"+str(walletBTC)+"BTC -> ")
		#print("Вы продаёте все свои биткоины в количестве "+ str(walletBTC) +" по цене " + str(sellingRate))

		if float(BTCforSale)>walletBTC:
			print("На вашем кошельке недостаточно BTC, на данный момент у вас Bal:"+str(walletBTC))
		elif float(BTCforSale)<=walletBTC:
			bankAcc += float(BTCforSale)*sellingRate
			bankAcc = round(bankAcc, 2)
			walletBTC = walletBTC-float(BTCforSale)
			walletBTC = round(walletBTC, 6)
		print("На вашем банковском аккаунте находится "+str(bankAcc)+"USD, на вашем биткоин кошельке осталось "+ str(walletBTC)+"BTC")
	elif userChoise=="3":
		print("У нас есть 3 типа видеокарт")
		print("Первого уровня - майнит 0.1 BTC в день артикул (1)")
		print("Второго уровня - майнит 0.15 BTC в день артикул (2)")
		print("Третьего уровня - майнит 0.25 BTC в день артикул (3)")

		userMarketChoise = input("Купить(1)/Выйти(0)")
		if userMarketChoise=="1":
			userCardChoise = input("Купить(артикул)")
			if userCardChoise=="1":
				if bankAcc<20000.00:
					print("У вас недостаточно средств для покупки")
				else:
					bankAcc = bankAcc - 20000 
					lvl1card += 1
					print("Теперь у вас "+str(lvl1card)+" видеокарт(ы) 1 lvl")

			elif userCardChoise=="2":
				# 
				if bankAcc<30000.00:
					print("У вас недостаточно средств для покупки")
				else:
					bankAcc = bankAcc - 30000 
					lvl2card += 1
					print("Теперь у вас "+str(lvl2card)+" видеокарт(ы) 2 lvl")

			elif userCardChoise=="3":
				if bankAcc<40000.00:
					print("У вас недостаточно средств для покупки")
				else:
					bankAcc = bankAcc - 40000 
					lvl3card += 1
					print("Теперь у вас "+str(lvl3card)+" видеокарт(ы) 3 lvl")



	elif userChoise=="4":
		BTC = input("Введите количество BTC на покупку: ")

		allPrice = float(BTC)*sellingRate

		if bankAcc<allPrice:
				print("У вас недостаточно средств для покупки")
		else:
			bankAcc = bankAcc - allPrice
			walletBTC += float(BTC)
			print("Теперь у вас "+str(walletBTC)+"BTC")




	elif userChoise=="0":
		break



















