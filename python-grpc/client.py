from fastapi import FastAPI
from fastapi.responses import JSONResponse

import grpc
from generated.welcome_pb2_grpc import WelcomeStub,FarewellStub
from generated.welcome_pb2 import Result, Name

def call_welcome_service(firstname: str, lastname: str) -> Result:
    channel = grpc.insecure_channel("localhost:10201")
    client = WelcomeStub(channel)
    request = Name(firstname =firstname,lastname=lastname)
    response = client.SayHello(request)
    return response

def call_farewell_service(firstname: str, lastname: str) -> Result:
    channel = grpc.insecure_channel("localhost:10201")
    client = FarewellStub(channel)
    request = Name(firstname=firstname,lastname=lastname)
    response = client.SayBye(request)
    return response
    

app = FastAPI()
@app.get('/welcome')
async def welcome(firstname: str, lastname: str):
    result: Result = call_welcome_service(firstname, lastname)
    return JSONResponse({'message': result.message})

@app.get('/bye')
async def welcome(firstname: str, lastname: str):
    result: Result = call_farewell_service(firstname, lastname)
    return JSONResponse({'message': result.message})

# uvicorn client:app --host 0.0.0.0 --port 10202