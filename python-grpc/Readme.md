# GRPC Python Implementation

In this demo we use Grpc server as RPC server and Fastapi based Python app as the RPC Client 

## Install requirements
* Create a virtual env  
```
python -m venv fastapienv
```
and activate it 

* Install the following  
```
pip install grpcio-tools
```

* Since we are using Fastapi as the client add that too  
```
pip install fastapi
pip install "uvicorn[standard]"
```

## Generate code from Proto files
Run the following command to generate class files required
```
python -m grpc_tools.protoc -I ./protos  --python_out=./generated --grpc_python_out=./generated --pyi_out=./generated ./protos/welcome.proto
```
This should generate the required classes


## Run the code
Start the Server and Client
```
python main.py
```

In case you want to start them seperately
```
# to start server
python server.py

# to start client
uvicorn client:app --host 0.0.0.0 --port 10202
```

NOTE: In case you get an error `ModuleNotFoundError: No module named 'welcome_pb2'` then Edit `generated/welcome_pb2_grpc.py` and replace the following
```
# change
import welcome_pb2 as welcome__pb2

# to 
from . import welcome_pb2 as welcome__pb2
```


Now you should be able to check the 2 services  
http://0.0.0.0:10202/welcome?firstname=Pratheesh&lastname=Russell  
http://0.0.0.0:10202/bye?firstname=Pratheesh&lastname=Russell  
