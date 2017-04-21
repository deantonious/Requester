import requests
import os
import time

print ("\n" +
      "     ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗███████╗██████╗ \n" +
      "     ██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗\n" +
      "     ██████╔╝█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║   █████╗  ██████╔╝\n" +
      "     ██╔══██╗██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗\n" +
      "     ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   ███████╗██║  ██║\n" +
      "     ╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝\n" +
      "     v1.0 by deantonious and Jamz\n")
 
def help():
    print ("Requester command reference")
    print ("===========================\n")
    print ("    COMMAND                     DESCRIPTION")
    print ("    -------                     -----------\n")
    print ("    help                        Display command reference")
    print ("    depends                     Install/Update dependencies")
    print ("    set [url|method] [value]    Set url/method (Methods: POST / GET)")
    print ("    header [type] [value]       Add/Remove header (removes the header it exists)")
    print ("    parameter [type] [value]    Add/Remove parameter (removes the parameter it exists)")
    print ("    output [enable|disable]     Enable/disable file output")
    print ("    values                      Display request values")
    print ("    send                        Execute request")
    print ("    exit                        Quit Requester console")
    print ("\n")

def setup():
    help()

headers = {  }
parameters = {  }
method = "GET"
url = ""
output = False

setup()
while True:

    line = input("requester > ")
    args = line.split(' ')
    
    if len(args) > 3:
        for i in range(3, len(args)):
            args[2] += " " + args[i]
            
    command = args[0].lower()

    if command == "help":
        help()
        
    elif command.lower() == "depends":
        update = input("[#] Do you want to install/update dependencies? (y/n) ")
        if update.lower() == "y" or update.lower() == "":
            os.system("pip install requests")
            
    elif command.lower() == "set":
        if len(args) == 3:
            if args[1].lower() == "url":
                
                if "https://" in args[2] or "http://" in args[2]:
                    url = args[2]
                    print ("URL set to '" + url + "'")
                else:
                    print ("Please, enter the full url...")
            elif args[1].lower() == "method":
                if args[2].lower() == "post":
                    method = "POST"
                    print ("Request method set to POST!")
                elif args[2].lower() == "get":
                    method = "GET"
                    print ("Request method set to GET!")
                else:
                    print ("Set the method to POST / GET")
            else:
                print ("Please, set the url / method parameter...")
        else:
            print ("Not enough arguments...")
            
    elif command.lower() == "header":
        if len(args) > 1:
            if args[1] in headers:
                del headers[args[1]]
                print ("Removed header '" + args[1] + "'")
            elif len(args) == 3 and args[2] != "":
                headers[args[1]] = args[2]
                print ("Added header '" + args[1] + ": " + args[2] + "'")
            else:
                print ("Not enough arguments...")
        else:
            print ("Not enough arguments...")
            
    elif command.lower() == "parameter":
        if len(args) > 1:
            if args[1] in parameters:
                del parameters[args[1]]
                print ("Removed parameter '" + args[1] + "'")
            elif len(args) == 3 and args[2] != "":
                parameters[args[1]] = args[2]
                print ("Added parameter '" + args[1] + "=" + args[2] + "'")
            else:
               print ("Not enough arguments...") 
        else:
            print ("Not enough arguments...")
        
    elif command.lower() == "output":
        if len(args) == 2:
            if args[1].lower() == "enable":
                output = True
                print ("File output enabled!")
            elif args[1].lower() == "disable":
                output = False
                print ("File output disabled!")
            else:
                print ("Please, set the output to enable / disable")
        else:
            print ("Not enough arguments...")
            
    elif command.lower() == "values":
        outt = "enabled" if output == True else "disabled"
        print ("[Request Values]=====================")
        print ("    URL : " + url)
        print ("    Method : " + method)
        print ("    Headers : " + str(headers))
        print ("    Parameters : " + str(parameters))
        print ("    Output File: " + outt)

    elif command.lower() == "send":
        if url != "":
            if len(headers) == 0:
                confirmation = input("[#] Do you want to add the default headers? (y/n) ")
                if confirmation == "y" or confirmation == "":
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
                    
            if method == "GET":
                request = requests.get(url, headers=headers, params=parameters)
            elif method == "POST":
                request = requests.post(url, headers=headers, data=parameters)
            print ("=> Response code: " + str(request.status_code))
            reponse = request.text
            
            if output == True:
                t = time.time()
                filename = "requester-" + url.split("/")[2] + "-" + method + "-" + str(t) + ".txt"
                fd = open(filename, "w")
                fd.write(reponse)
                fd.close()
                print ("=> File " + filename + " saved!")
        else:
            print ("Please, set a valid url to send the request...")
    elif command.lower() == "exit":
        print ("See you next time :)")
        break
    else:
        help()