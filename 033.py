#Zaprojektuj program do rejestracji użytkownika w systemie. 
#Hasło do konta użytkownika powinno mieć co najmniej 8 znaków i zawierać minimum jedną cyfrę. 
#Gdy hasło nie spełnia warunków, pojawia się komunikat o błędnym haśle i ponownym wpisaniu hasła. 


def passwordLength(length):
    minimalPasswordLength = 8
    if length < minimalPasswordLength:
        print("Hasło musi składać się z co najmniej 8 znaków. Wprowadź hasło jeszcze raz.")
        return 0
    else:
        return 1
    
def passwordNumber(currentPassword):
    for character in currentPassword:
        numberList = ["0","1","2","3","4","5","6","7","8","9"]
        for number in numberList:
            if character == number:
                return 1
    print("Hasło musi zawierać cyfrę. Wprowadź hasło jeszcze raz.")
    return 0
            
username = input("Wprowadź nazwę nowego użytkownika: ")

while True:
    password = input("Wprawadź hasło: ")
    checkLength = passwordLength(len(password))
    checkNumber = passwordNumber(password)
    if checkLength == 1 and checkNumber == 1:
        print("Użytkownik został poprawnie zarejestrowany.")
        break
