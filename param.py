import paramiko

# Set your server and SSH credentials
server_address = '192.168.2.17'
server_port = 22
username = 'Marton'
password = '31473'

# Set up SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
ssh.connect(server_address, port=server_port, username=username, password=password)

# Set up port forwarding (replace local_port and remote_port with your desired values)
local_port = 8080
remote_port = 80
ssh.get_transport().request_port_forward('', local_port)

print(f"Port forwarding established: localhost:{local_port} -> {server_address}:{remote_port}")

# Now, you can access the service on your laptop through localhost:local_port
# For example, if the service on the server is running on port 80, you can access it on localhost:8080

# When you're done, close the SSH connection
ssh.close()
