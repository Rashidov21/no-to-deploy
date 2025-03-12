import subprocess

def get_windows_uuid():
    try:
        result = subprocess.check_output(
            ["powershell", "(Get-CimInstance -Class Win32_ComputerSystemProduct).UUID"],
            text=True
        ).strip()
        return result
    except:
        return None

print(get_windows_uuid())
