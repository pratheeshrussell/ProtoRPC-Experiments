import subprocess

# Start the twirp server and client concurrently
def start_all():
    main_server_process = subprocess.Popen(["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "10201"])
    client_process = subprocess.Popen(["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "10202"])

    # Wait for both processes to finish
    main_server_process.wait()
    client_process.wait()

# Start both applications
start_all()

# python main.py