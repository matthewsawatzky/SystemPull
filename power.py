import subprocess
import platform

def get_power_consumption():
    """Get power consumption metrics (if available)."""
    try:
        if platform.system() == 'Linux':
            result = subprocess.run(['cat', '/sys/class/power_supply/BAT0/power_now'], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else 'N/A'
        elif platform.system() == 'Windows':
            result = subprocess.run(['powercfg', '/batteryreport'], capture_output=True, text=True)
            return 'Power report generated. Check the system battery report.'
        else:
            return 'N/A'
    except Exception as e:
        print(f"Error getting power consumption: {e}")
        return 'N/A'