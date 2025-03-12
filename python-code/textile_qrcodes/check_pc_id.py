import subprocess

def get_windows_uuid():
    try:
        result = subprocess.check_output(
            ["powershell", "-Command", "Get-WmiObject -Class Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID"],
            text=True
        ).strip()
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

print(get_windows_uuid())
