'''
Spróbuj zmodyfikować powyższy skrypt, aby zamiast obrazka wysłać załącznik w formacie PDF. 
Pamiętaj, że musisz zmienić sposób wczytywania i dodawania załącznika. Oto kilka wskazówek, 
które pomogą Ci w realizacji zadania:

Zmień nazwę pliku i rozszerzenie z 'obrazek.jpg' na nazwę Twojego pliku PDF, na przykład 'dokument.pdf'.
Zamiast klasy MIMEImage, będziesz musiał użyć klasy MIMEApplication 
z modułu email.mime.application. Zaimportuj tę klasę na początku swojego skryptu:
from email.mime.application import MIMEApplication
Zastąp wczytywanie obrazka i dodanie go jako załącznik wczytaniem pliku PDF i dodaniem go jako załącznik:
with open('dokument.pdf', 'rb') as file:
    pdf = MIMEApplication(file.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='dokument.pdf')
    msg.attach(pdf)
'''

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email import encoders

# Tworzenie wiadomości e-mail
msg = MIMEMultipart()
msg['From'] = 'przykładowy_nadawca@mail.com'
msg['To'] = 'przykładowy_odbiorca@mail.com'
msg['Subject'] = 'Temat wiadomości'

# Dodanie treści do wiadomości
tekst = 'Cześć! Oto przykładowa wiadomość e-mail z załącznikiem.'
msg.attach(MIMEText(tekst,'plain'))

# Wczytanie obrazka i dodanie jako załącznik
with open('dokument.pdf', 'rb') as file:
    pdf = MIMEApplication(file.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='dokument.pdf')
    msg.attach(pdf)

# Konfiguracja serwera SMTP i wysłanie wiadomości
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('przykładowy_nadawca@mail.com', 'przykladowehaslo')
server.send_message(msg)
server.quit()