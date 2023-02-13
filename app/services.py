import os
import paramiko
import subprocess

def create_ssh(host, user, keyfile):
    ssh = paramiko.SSHClient()
    k = paramiko.RSAKey.from_private_key_file(keyfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, pkey=k)
    return ssh

def service_hibernate(host_item):
    print(f"cwd={os.getcwd()}")
    print(host_item)
    key_file_name = host_item['keyfile']
    key_path = os.path.join(os.getcwd(), "keys", key_file_name)
    ssh = create_ssh(host_item['host'], host_item['user'], key_path)
    stdin, stdout, stderr = ssh.exec_command("shutdown_hi.bat")
    for line in stdout.readlines():
        print(line.strip())
    # with open(os.path.join(os.getcwd(), "keys", key_file_name), 'r') as f:
    #     print(f.readlines())

def service_wake(host_item):
    cmd = "wakepc"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(f'output={output}')