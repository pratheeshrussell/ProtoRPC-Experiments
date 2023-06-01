from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument
from generated import welcome_twirp, welcome_pb2

# Implementing the WelcomeService and FarewellService
class WelcomeService(object):
    async def SayHello(self, context,  request: welcome_pb2.Name) -> welcome_pb2.Result:
        message = f"Hello, {request.firstname} {request.lastname}!"
        return welcome_pb2.Result(message=message)

class FarewellService(object):
    async def SayBye(self, context,  request: welcome_pb2.Name) -> welcome_pb2.Result:
        message = f"Bye, {request.firstname} {request.lastname}!"
        return welcome_pb2.Result(message=message)
    
# Twirp Server
helloService = welcome_twirp.WelcomeServer(service=WelcomeService())
farewellService = welcome_twirp.FarewellServer(service=FarewellService())
app = TwirpASGIApp()

# Add the services
app.add_service(helloService)
app.add_service(farewellService)

# Start -> uvicorn server:app --host 0.0.0.0 --port 10201

