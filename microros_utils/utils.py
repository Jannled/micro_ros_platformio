import subprocess

def run_cmd(command, env=None):
    return subprocess.run(command,
        capture_output = False,
        shell = True,
        env=env
    )
