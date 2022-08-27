# Update 27/08/2022

import json
from multiprocessing.resource_sharer import stop
from urllib import response
import requests
import os
from tabulate import tabulate

os.system("cls")
os.system("title " + "☠️ M0NEGASQUE TOOLS ☠️")

print("This tool, developed by M0NEGASQUE, is a tool that makes it very\neasy to locate an ip address anywhere in the world. Easy to\nuse and very basic tool")
print('''
 ███▄ ▄███▓ ███▄    █ ▓█████   ▄████  ▄▄▄        ██████   █████   █    ██ ▓█████ 
▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀  ██▒ ▀█▒▒████▄    ▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▓█   ▀ 
▓██    ▓██░▓██  ▀█ ██▒▒███   ▒██░▄▄▄░▒██  ▀█▄  ░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒███   
▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██   ▒   ██▒░██  █▀ ░▓▓█  ░██░▒▓█  ▄ 
▒██▒   ░██▒▒██░   ▓██░░▒████▒░▒▓███▀▒ ▓█   ▓██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓ ░▒████▒
░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░
░  ░      ░░ ░░   ░ ▒░ ░ ░  ░  ░   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░
░      ░      ░   ░ ░    ░   ░ ░   ░   ░   ▒   ░  ░  ░     ░   ░  ░░░ ░ ░    ░   
       ░            ░    ░  ░      ░       ░  ░      ░      ░       ░        ░  ░
                                                                                 
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████                                      
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒                                      
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄                                        
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒                                     
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒                                     
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░                                     
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░                                     
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░                                       
             ░ ░      ░ ░      ░  ░      ░                                       
                                                             ''')

while True:

    try:
      print("\n")
      ip_demande = input("Enter ip adress : ")

      if ip_demande.isalpha():
        print("Please enter an ip and not letters !")
      else:
        response = requests.get(f'http://ip-api.com/json/{ip_demande}')

        the_reponse = response.json()

        kil = ["ip", "region", "city"]

        ip_value = the_reponse['query']
        region_value = the_reponse['regionName']
        city_value = the_reponse['city']
        zip_value = the_reponse['zip']
        as_value = the_reponse['as']
        country_value = the_reponse['country']

        value_tableau = [
            {
            'IP': f'{ip_value}',
            'Country': f'{country_value}',
            'Region': f'{region_value}',
            'City': f'{city_value}',
            'Zip': f'{zip_value}', 
            'Operator': f'{as_value}'
            },
        ]

        for key, value in the_reponse.items():
            value = value
            print(tabulate(value_tableau, headers='keys', tablefmt="grid"))
            break
    except:
      print("An error has occurred !")









