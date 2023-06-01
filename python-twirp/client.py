from fastapi import FastAPI
from fastapi.responses import JSONResponse

from twirp.context import Context
from twirp.exceptions import TwirpServerException
from generated import welcome_twirp, welcome_pb2

def call_welcome_service(firstname: str, lastname: str) -> welcome_pb2.Result:
    client = welcome_twirp.WelcomeClient("http://localhost:10201")
    try:
        response = client.SayHello(ctx=Context(), 
                        request=welcome_pb2.Name(firstname=firstname,lastname=lastname))
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())

def call_farewell_service(firstname: str, lastname: str) -> welcome_pb2.Result:
    client = welcome_twirp.FarewellClient("http://localhost:10201")
    try:
        response = client.SayBye(ctx=Context(), 
                        request=welcome_pb2.Name(firstname=firstname,lastname=lastname))
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())


app = FastAPI()
@app.get('/welcome')
async def welcome(firstname: str, lastname: str):
    result = call_welcome_service(firstname, lastname)
    return JSONResponse({'message': result.message})

@app.get('/bye')
async def welcome(firstname: str, lastname: str):
    result = call_farewell_service(firstname, lastname)
    return JSONResponse({'message': result.message})

# uvicorn client:app --host 0.0.0.0 --port 10202