# https://e-learning.training360.com/courses/take/python-alapismeretek/lessons/10508870-feladatok-egyszeru-utasitasok-kifejezesek-comment-print

szobaterület = 90
vödör = 15
vödörár = 5200

teljesszoba = szobaterület / vödör * vödörár

#print("A teljes szoba kifestése " + str(teljesszoba) + " Ft-ba fog kerülni.")

festéssebességpercben = 12
festéssebességórában = festéssebességpercben / 60
átfestésdb = 2
órabér = 1800
végösszeg = szobaterület * festéssebességórában * órabér * átfestésdb
ÁFA = 0.27
végösszegÁFÁval = végösszeg * (1 + ÁFA)

# print("A bér végösszege " + str(végösszeg) + " Ft ÁFA nélkül, és " + str(végösszegÁFÁval) + " Ft ÁFÁ-val.")
# print("A bér végösszege " + str(végösszeg) + " Ft ÁFA nélkül, \n és " + str(végösszegÁFÁval) + " Ft ÁFÁ-val.")

#\n, nem /n az új sor
print(f'fA bér végösszege {végösszeg:.0f} Ft ÁFA nélkül, és  {végösszegÁFÁval:+,.0f} Ft ÁFÁ-val.')
print(f'fA bér végösszege {végösszeg:^} Ft ÁFA nélkül, és \n {végösszegÁFÁval} Ft ÁFÁ-val.')
#új sor
print("")
#mindent, beleértve \n, {...} stb. kiírása
print(r'raw: A bér végösszege {végösszeg} Ft ÁFA nélkül, és {végösszegÁFÁval} Ft ÁFÁ-val.')
print(r'raw: A bér végösszege {végösszeg} Ft ÁFA nélkül, és \n {végösszegÁFÁval} Ft ÁFÁ-val.')

print(str(30 * 0.8 / 0.6) + " üveget tud megtölteni." )

print(str(170*7/100+35*9/100) + " litert fogyaszt csak oda, és " + str(2*170*7/100+35*9/100) + " litert fogyaszt oda-vissza.")
print(str(2*170*7/100+35*9/100*350) + " forintba kerül a teljes út.")

print(bool(9))




