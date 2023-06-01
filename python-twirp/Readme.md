# Twirp Python Implementation

In this demo we use TwirpASGIApp as RPC server and Fastapi based Python app as the RPC Client 

## Install requirements
### General requirements for twirp
* Install GO from the following [link](https://go.dev/dl/ "Golang")  
* Download the Protoc from [releases page](https://github.com/protocolbuffers/protobuf/releases) and add Environment path to the binary  
* Install the required GO plugins
```
go install github.com/twitchtv/twirp/protoc-gen-twirp@latest
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

```
### Python requirements
* Install the following plugin
```
go install github.com/verloop/twirpy/protoc-gen-twirpy@latest
```
* Create a virtual env  
```
python -m venv fastapienv
```
and activate it 

* Install the following  
```
pip install twirp
```

* Since we are using Fastapi as the client add that too  
```
pip install fastapi
pip install "uvicorn[standard]"
```

## Generate code from Proto files
Run the following command to generate class files required
```
protoc -I ./protos  --python_out=./generated --twirpy_out=./generated --pyi_out=./generated ./protos/welcome.proto
```
This should generate the required files

## Run the code
Start the Server and Client
```
python main.py
```

In case you want to start them seperately
```
# to start server
uvicorn server:app --host 0.0.0.0 --port 10201

# to start client
uvicorn client:app --host 0.0.0.0 --port 10202
```

Now you should be able to check the 2 services  
http://0.0.0.0:10202/welcome?firstname=Pratheesh&lastname=Russell  
http://0.0.0.0:10202/bye?firstname=Pratheesh&lastname=Russell  
