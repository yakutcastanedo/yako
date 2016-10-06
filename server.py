# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

from wsgiref.simple_server import make_server

led = 10
GPIO.setmode(GPIO.BCM)

# Set GPIO no 10 to output mode
GPIO.setup(led, GPIO.OUT)

# Function that is ran when a http request comes in
def simple_app(env, start_response):

    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        #hint: set the pin low here 
        print("user asked for /on")
        GPIO.output(led, True)
        return  "<html><body> <a href=\"/off\">OFF!</a> </body></html>"
    elif env["PATH_INFO"] == "/off":
        # hint: set the pin to HIGH here
        GPIO.output(led, False)
        print("user asked for /off") #HINT: these print() lines show u
        return ("<html><body> <a href=\"on\">ON!</a> </body></html>")
    else:
       print("user asked for something else")
       return ("<html><body> <a href=\"/on\">ON!</a> </body></html>")
# (add some HTML insted of "Hello world")         

# Create a small python server
httpd = make_server("", 8001, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 wher"
print "Or if you run this server on your own computer then http://loca"
httpd.serve_forever() 
        

