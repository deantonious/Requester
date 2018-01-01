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
    print("\n \nMissing required modules.")
    install = input ("[#] Update/install requirments? (y/n) ")
    if install.lower() == "y":
        import os, sys
        os.system("python3 -m pip install requests colorama")
        print("If pip installation failed, you need to fix your environment variables.")
        input("Press enter to continue...")
        os.execl(sys.executable, sys.executable, * sys.argv)
        del os, sys
    else:
        print("Your loss...")
except KeyboardInterrupt:
    print(GREEN + "\n[I] Shutting down..." + END)
    raise SystemExit
except:
    print(RED + "\n[!] Module input failed. Please make sure to install the dependencies." + END)
    raise SystemExit

colorama.init()
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + BOLD +
      "     ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗███████╗██████╗ \n" +
      "     ██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗\n" +
      "     ██████╔╝█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║   █████╗  ██████╔╝\n" +
      "     ██╔══██╗██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗\n" +
      "     ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   ███████╗██║  ██║\n" +
      "     ╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝\n" + RESET +
      "     v1.7 by deantonious and Jamz\n")

def help():
    print (BOLD + " Requester command reference")
    print (" ===========================\n")
    print (CYAN + "    COMMAND         "+RESET+GREEN+"            DESCRIPTION"+RESET+BOLD)
    print ("    -------                     -----------\n")
    print ("    help                        Display command reference\n")

    print ("    header [type] [value]       Add/Remove header (use 'header [type]' to remove a heder)")
    print ("    parameter [name] [value]    Add/Remove parameter (use 'parameter [name]' to remove a parameter)")
    print ("    cookie [name] [value]       Add/Remove cookie (use 'cookie [name]' to remove a cookie)\n")

    print ("    options                     Display request options (use 'options reset' to reset them all)")
    print ("    set [option] [value]        Set option value\n")

    print ("    send                        Execute request")
    print ("    exit                        Quit Requester console")
    print ("\n" + RESET)

def setup():
    help()

s = requests.session()
headers = {  }
parameters = {  }
cookies = {  }
method = "GET"
url = ""
output = "console"

setup()
while True:

    line = input("requester > ")
    args = line.split(' ')

    if len(args) > 3:
        for i in range(3, len(args)):
            args[2] += " " + args[3]
            args.remove(args[3])

    command = args[0].lower()

    if command == "help":
        help()

    elif command == "set":
        if len(args) == 3:
            if args[1].lower() == "url":
                if "https://" in args[2] or "http://" in args[2]:
                    url = args[2]
                    print ("URL set to '" + url + "'")
                else:
                    print (RED + "Please, enter the full url..." + RESET)
            elif args[1].lower() == "method":
                if args[2].lower() == "post":
                    method = "POST"
                    print ("Request method set to POST!")
                elif args[2].lower() == "get":
                    method = "GET"
                    print ("Request method set to GET!")
                else:
                    print ("Set the method to POST / GET")
            elif args[1].lower() == "output":
                if args[2].lower() == "file":
                    output = "file"
                    print ("Output set to file mode!")
                elif args[2].lower() == "console":
                    output = "console"
                    print ("Output set to console mode!")
                elif args[2].lower() == "all":
                    output = "all"
                    print ("Output set to console and file mode!")
                elif args[2].lower() == "none":
                    output = "none"
                    print ("Output disabled!")
                else:
                    print (RED + "Please, set the output to [file|console|all|none]" + RESET)
            else:
                print (RED + "Please, set the url / method parameter..." + RESET)
        else:
            print (RED + "Not enough arguments..." + RESET)

    elif command == "cookie":
        if len(args) == 2:
            if args[1] in cookies:
                # Remove header
                del cookies[args[1]]
                print ("Removed cookie '{}'".format(args[1]))
            else:
                print (RED + "Cookie not found..." + RESET)
        elif len(args) == 3:
            cookies[args[1]] = args[2]
            print("Cookie '{}' set to '{}'".format(args[1], args[2]))
        else:
            print(RED + "Wrong usage..." + RESET)

    elif command == "header":
        if len(args) == 2:
            if args[1] in headers:
                # Remove header
                del headers[args[1]]
                print ("Removed header '{}'".format(args[1]))
            else:
                print (RED + "Header not found..." + RESET)
        elif len(args) == 3:
            if args[1] in headers:
                # Override header
                del headers[args[1]]
                headers[args[1]] = args[2]
                print ("Changed header '{}' to '{}'".format(args[1], args[2]))
            else:
                # Add header
                headers[args[1]] = args[2]
                print ("Added header '{}: {}'".format(args[1], args[2]))
        else:
            print (RED + "Wrong usage..." + RESET)

    elif command == "parameter":
        if len(args) == 2:
            if args[1] in parameters:
                # Remove parameter
                del parameters[args[1]]
                print ("Removed parameter '{}'".format(args[1]))
            else:
                print (RED + "Parameter not found..." + RESET)
        elif len(args) == 3:
            if args[1] in parameters:
                # Override parameter
                del parameters[args[1]]
                parameters[args[1]] = args[2]
                print ("Changed parameter '{}' to '{}'".format(args[1], args[2]))
            else:
                # Add parameter
                parameters[args[1]] = args[2]
                print ("Added parameter '{}={}'".format(args[1], args[2]))
        else:
            print (RED + "Wrong usage..." + RESET)

    elif command == "options":
        if len(args) > 1:
            if args[1] == "reset":
                url = ""
                output = "none"
                headers = { }
                parameters = { }
                method = "GET"
                print ("Options set to default values!")
            else:
                print (RED + "Available parameters: reset" + RESET)
        else:
            print ("\n Request options\n")
            print ("    Name        Description                                         Current Setting")
            print ("    ====        ===========                                         ===============")
            print ("    URL         Url to which the request will be sent               " + url)
            print ("    METHOD      Request method (POST|GET)                           " + method)
            print ("    OUTPUT      Ouput format (file|console|all|none)                " + output)
            print ("    HEADERS     Headers of the request (use headers command)        " + str(headers))
            print ("    PARAMETERS  Parameters of the request (use parameters command)  " + str(parameters))
            print ("    COOKIES     Cookies of the request (use cookies command)        " + str(parameters) + "\n")

    elif command == "send":
        if url != "":
            if len(headers) == 0:
                confirmation = input("[#] Do you want to add the default headers? (y/n) ")
                if confirmation == "y" or confirmation == "":
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
            s.headers.update(headers)
            for cookie in cookies:
                s.cookies.set(cookie, cookies[cookie])
            try:
                if method == "GET":
                    request = s.get(url, params=parameters)
                elif method == "POST":
                    request = s.post(url, data=parameters)

                reponse = request.text

                print ("=> Response code: " + str(request.status_code))
                if output == "file" or output == "all":
                    t = time.time()
                    filename = "requester-" + url.split("/")[2] + "-" + method + "-" + str(t) + ".txt"
                    fd = open(filename, "w")
                    fd.write(reponse)
                    fd.close()
                    print ("=> File " + filename + " saved!")
                if output == "console" or output == "all":
                    print ("=> Response Content:\n")
                    print (reponse)

            except ConnectionRefusedError:
                print (RED + "Failed to connect, invalid url possible." + RESET)
            except requests.packages.urllib3.exceptions.NewConnectionError:
                print(RED + "Failed to connect, invalid url possible." + RESET)
            except requests.packages.urllib3.exceptions.MaxRetryError:
                print(RED + "Reached max retries, invalid url possible." + RESET)
            except requests.exceptions.ConnectionError:
                print(RED + "Failed to connect, invalid url possible." + RESET)

        else:
            print (RED + "Please, set a valid url to send the request..." + RESET)
    elif command == "exit":
        print ("See you next time :)")
        break
    else:
        help()
