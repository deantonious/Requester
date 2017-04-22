[![Requester Logo](https://deantonious.es/wp-content/uploads/2017/04/requester_logo_1.jpg)](https://github.com/deantonious/Requester)

## Description

> Create custom HTTP/HTTPS requests and saves the output to a text file. This is really useful for some CTF challenges and Web Pentesting. (Made to work with Python 3.6.1)

## Commands

Use this commands on the Requester console to configure and send your request:

COMMAND                   | DESCRIPTION
--------------------------| -------------
help                      |  Display command reference
set \[url\|method\] \[value\]  |  Set url/method (Methods: POST / GET)
header \[type\] \[value\]     |  Add/Remove header (removes the header it exists)
parameter \[type\] \[value\]  |  Add/Remove parameter (removes the parameter it exists)
output \[file\|console\|none]   |  Set the output mode (use 'output all' to use file and console outputs)
values                    |  Display request values. (use 'values reset' to reset them)
send                      |  Execute request
exit                      |  Quit Requester console

## Installation and usage example

1. Download the script to your computer and run it from terminal. 
2. Run the depends command to install the dependencies
3. Set the target url with "set url http://example.com"
4. Set the request method with "set method [POST|GET]" (by default it's set to GET)
5. (Optional) Set the request headers (if it is already set, you'll remove it)
6. (Optional) Add parameters to the request with "parameter user username" (if it is already set, you'll remove it)
7. (Optional) Set the file output mode with "output console"
8. Send the request with "send"

## Screenshots

![Requester Console](https://deantonious.es/wp-content/uploads/2017/04/requester_console-1.png)

Requester console 

## License

This project is licensed under the MIT License - see the [license file](LICENSE) for more details. _Please note that if you redistribute this project, you have to include this license on it!_

## Sources, Libraries and Credits

Python HTTP Requests for Humans™ by [kennethreitz](https://github.com/kennethreitz/requests) - http://python-requests.org

*Thanks to James for helping teaching me the Python basics and helping me with the development!*
