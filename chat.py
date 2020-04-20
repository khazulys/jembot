import os, sys, time, random

def tik(s):
	for khaz in s + '\n':
		sys.stdout.write(khaz)
		sys.stdout.flush()
		time.sleep(random.random()*0000.3)

logo = """

   \033[1;92m    __ ___  _   __ ___   _  _____
   \033[1;97m   / // _/ / \,' // o.),' \/_  _/
   \033[1;92mn_/ // _/ / \,' // o \/ o | / /  
   \033[1;97m\_,'/___//_/ /_//___,'|_,' /_/   
                                 
		Jembot kau 
	   code by cryptocyber9\n"""


def bot_khentot():
	os.system('clear')
	print (logo)
	tik("Jembot adalah program bot yang kayak jembot!")
	tik("Disaat kalian gabut, mainkan aku ahh crot!\n")
	bot1 = []
	enter = input("Set kalimat 1 : ")
	bot1.append(enter)
	for khaz in bot1:
		print ("Kalimat 1 sudah di set")

	bot2 = []
	enter2 = input("set kalimat 2 : ")
	bot2.append(enter2)
	for zul in bot2:
		print ("Kalimat 2 sudah di set")

	bot3 = []
	enter3 = input("Set kalimat 3 : ")
	bot3.append(enter3)
	for z in bot3:
		print ("Kalimat 3 sudah di set")


	tik("\nKalimat untuk bot sudah di set, mari kita mulai...")
	time.sleep(1)
	tik("Siapa nama kamu? ")
	nama = input("> ")
	tik("Nama untuk bot? ")
	namabot = input("> ")
	if not nama:
		exit()
	if nama:
		print ("")
		str(input("{}  : ".format(nama)))
		for zul in bot1:
			time.sleep(2)
			print ("{} : ".format(namabot)+zul)

		str(input("{}  : ".format(nama)))
		for kon in bot2:
			time.sleep(2)
			print ("{} : ".format(namabot)+kon)

		str(input("{}  : ".format(nama)))
		for tol in bot3:
			time.sleep(2)
			print ("{} : ".format(namabot)+tol)

	else:
		exit()

	ngentot = True
	while ngentot:
		ul = input("\nMau ngulang lagi? (y/n) ")
		if ul == "y":
			bot_khentot()
		else:
			try:
				while True:
					i = 20
					if i > 10:
						i += 20
						print ("Memang kau khentot, {}".format(nama))

			except KeyboardInterrupt:
				print ("[!]GoodBye khontol!")
if __name__=="__main__":
	bot_khentot()
