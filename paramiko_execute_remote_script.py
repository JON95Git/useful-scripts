import paramiko

def execute_remote_script(host, port, username, password):
    """Execute remote script"""
    try:
        with paramiko.SSHClient() as ssh_client:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(
                hostname=host,
                username=username,
                password=password,
                allow_agent=False,
                look_for_keys=False,
                port=port,
            )

            _, stdout, stderr = ssh_client.exec_command(
                f"./remote_script.sh {username} {password}"
            )

            recv = stdout.channel.recv_exit_status()
            recv_err = stderr.channel.recv_stderr(65535).decode("utf-8")
            ssh_client.close()

            if recv:
                raise Exception(f"{recv_err}")
    except:
        raise Exception("Something went wrong")
    return []

