#https://e-learning.training360.com/courses/take/python-alapismeretek/lessons/10509132-feladatok-string-operatorok-es-vezerles

input_age = int(input("Hány éves vagy?"))
input_order = str(input("Mit iszol?"))

if input_order not in ("sör", "kóla"):
    print("Csak sört vagy kólát tudunk adni!")

elif (input_age < 14 and input_order == "sör") :
    print("Csak kólát tudunk adni!")

elif (input_age > 60 and input_order == "kóla"):
    print("Csak sört tudunk adni vérnyomásra!")
elif input_order == "sör":
    print("A söre.")
elif input_order == "kóla":
    print("A kólád.")

