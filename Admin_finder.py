
import requests
from termcolor import colored
import time
import http
import urllib3


print("\n")
print(r"||\\		    ||     //")
print(r"|| \\               ||    //")
print(r"||  \\		    ||   //")
print(r"||   \\		    ||  //")
print(r"||____\\	    || //")
print(r"||_____\\	    ||//")
print(r"||	\\	    ||\\")
print(r"||	 \\	    || \\")
print(r"||	  \\        ||  \\")
print(r"||	   \\	    ||   \\")
print(r"||	    \\	    ||    \\")
print(r"||	     \\	    ||     \\")
print("\n")


print(colored("██████████████████████████████","green"))
print(colored("██████████████████████████████","green"))
print(colored("██████████████████████████████","white"))
print(colored("██████████████████████████████","white"))
print(colored("██████████████████████████████","red"))
print(colored("██████████████████████████████","red"))
print("\n")

with open('list.txt') as f:
    flat_list=[word for line in f for word in line.split()]




number = 0
for num in open("list.txt"):
    number += 1



print(colored("\n  ►►►►►►►ATTENTION◄◄◄◄◄◄◄  ","red"))
print(colored("    Do not use / at the end of the url    ","red"))
print(colored("    for examp https://www.examp.com \n","green"))
Target = input(colored("Enter website url :\n","blue"))


"""  ***main***  """
def find():
    for i in range(1,number):
        print(i)
        site = requests.get(Target +"/"+ flat_list[i])
        # print(site.url)
        check = site.status_code
        print("this web is ==> ",site.url,colored(check,"yellow"))
        if site.status_code == 200:
            print("this web is ==> ",site.url,colored(check,"red"))
            time.sleep(10)
            break
        try:
            pass
        except (ConnectionError, requests.exceptions.ConnectionError , ConnectionResetError , http.client.RemoteDisconnected ,urllib3.exceptions.ProtocolError):
                print("Something else went wrong")    

find()
