from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Create factorial function
class FactorialServer:
    def calculate_factorial(self, n):

        if n < 0:
            return "Factorial not possible for negative numbers"

        result = 1

        for i in range(1, n + 1):
            result = result * i

        return result

# Restrict path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(("localhost", 8000),
                        requestHandler=RequestHandler) as server:

    server.register_instance(FactorialServer())

    print("Server is running...")

    server.serve_forever()