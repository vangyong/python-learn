
from suds.client import Client

if __name__ == '__main__':
    try:
        hello_client = Client('http://localhost:7789/?wsdl')
        result = hello_client.service.say_hello("Dave", 5)
        print result
    except ImportError:
        print "Error: example server code requires Python >= 2.5"
