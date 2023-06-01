from concurrent import futures
import grpc
from generated.welcome_pb2 import Result, Name
from generated import welcome_pb2_grpc

# Implementing the WelcomeService and FarewellService
class WelcomeService(welcome_pb2_grpc.WelcomeServicer):
   def SayHello(self, request: Name, context) -> Result:
        message = f"Hello, {request.firstname} {request.lastname}!"
        return (Result(message=message))

class FarewellService(welcome_pb2_grpc.FarewellServicer):
    def SayBye(self,  request: Name, context) -> Result:
        message = f"Bye, {request.firstname} {request.lastname}!"
        return (Result(message=message))

# Create the grpc server
def serve():
    port = 10201
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
        )
    # Add the services
    welcome_pb2_grpc.add_WelcomeServicer_to_server(WelcomeService(), server)
    welcome_pb2_grpc.add_FarewellServicer_to_server(FarewellService(), server)


    server.add_insecure_port(f'[::]:{port}')
    print(f"Server started on port: {port} ")
    server.start()
    server.wait_for_termination()

# serve()
if __name__ == "__main__":
    serve()

# Start -> python server.py

