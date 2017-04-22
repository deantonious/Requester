import time

#Color Table
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

try:
    import requests, colorama #Attempt to import non standard modules
except ModuleNotFoundError: #If the modules are not found install them with pip
    print(RED + "\n \nMissing required modules.")
    install = input ("[#] Update/install requirments? (y/n) ")
    if install.lower() == "y":
        import os, sys
        os.system("pip install requests colorama")
        print("If pip installation failed, you need to fix your environment variables.")
        input("Press enter to continue...")
        os.execl(sys.executable, sys.executable, * sys.argv)
        del os, sys

    else:
        print("Your loss...")

colorama.init()
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + BOLD +
      "     ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗███████╗██████╗ \n" +
      "     ██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗\n" +
      "     ██████╔╝█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║   █████╗  ██████╔╝\n" +
      "     ██╔══██╗██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗\n" +
      "     ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   ███████╗██║  ██║\n" +
      "     ╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝\n" + RESET +
      "     v1.1 by deantonious and Jamz\n")
 
def help():
    print (BOLD + " Requester command reference")
    print (" ===========================\n")
    print (CYAN + "    COMMAND         "+RESET+GREEN+"            DESCRIPTION"+RESET+BOLD)
    print ("    -------                     -----------\n")
    print ("    help                        Display command reference")
    print ("    set [url|method] [value]    Set url/method (Methods: POST / GET)")
    print ("    header [type] [value]       Add/Remove header (removes the header it exists)")
    print ("    parameter [type] [value]    Add/Remove parameter (removes the parameter it exists)")
    print ("    output [file|console|none]  Set the output mode (use 'all' to use file and console output)")
    print ("    values                      Display request values")
    print ("    send                        Execute request")
    print ("    exit                        Quit Requester console")
    print ("\n" + RESET)

def setup():
    help()

headers = {  }
parameters = {  }
method = "GET"
url = ""
output = "console"



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
            if args[1].lower() == "file":
                output = "file"
                print ("Output set to file mode!")
            elif args[1].lower() == "console":
                output = "console"
                print ("Output set to console mode!")
            elif args[1].lower() == "none":
                output = "none"
                print ("Output disabled!")
            else:
                print ("Please, set the output to enable / disable")
        else:
            print ("Not enough arguments...")
            
    elif command.lower() == "values":
        print ("\n Request Values")
        print (" ==============")
        print ("    => URL : " + url)
        print ("    => Method : " + method)
        print ("    => Headers : " + str(headers))
        print ("    => Parameters : " + str(parameters))
        print ("    => Output Mode: " + output + "\n")

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
            
            if output == "file" or output == "all":
                t = time.time()
                filename = "requester-" + url.split("/")[2] + "-" + method + "-" + str(t) + ".txt"
                fd = open(filename, "w")
                fd.write(reponse)
                fd.close()
                print ("=> File " + filename + " saved!")
            elif output == "console" or output == "all":
                print ("=> Response Content:\n")
                print (reponse)
                
        else:
            print ("Please, set a valid url to send the request...")
    elif command.lower() == "exit":
        print ("See you next time :)")
        break
    else:
        help()