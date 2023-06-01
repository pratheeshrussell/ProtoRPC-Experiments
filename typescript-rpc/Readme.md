# Typescript RPC

generating classes for Typescript with protoc

```
npm install -g protoc-gen-js
npm install ts-protoc-gen

# Path to this plugin
PROTOC_GEN_TS_PATH="./node_modules/.bin/protoc-gen-ts"

protoc -I protos --plugin="protoc-gen-ts=${PROTOC_GEN_TS_PATH}"  --js_out="import_style=commonjs,binary:./generated" --ts_out="service=grpc-web:./generated"  ./protos/welcome.proto

```