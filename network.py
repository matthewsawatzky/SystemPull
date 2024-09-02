import psutil
import subprocess
import platform

def get_network_info():
    """Get network statistics and adapter information."""
    try:
        net_stats = psutil.net_if_stats()
        net_io_counters = psutil.net_io_counters(pernic=True)
        network_info = []
        for iface, stats in net_stats.items():
            io_counters = net_io_counters.get(iface, None)
            if io_counters:
                network_info.append({
                    'interface': iface,
                    'is_up': stats.isup,
                    'speed_mbps': stats.speed,
                    'bytes_sent': io_counters.bytes_sent,
                    'bytes_recv': io_counters.bytes_recv,
                    'packets_sent': io_counters.packets_sent,
                    'packets_recv': io_counters.packets_recv
                })
        return network_info
    except Exception as e:
        print(f"Error getting network info: {e}")
        return []

def get_ping(host='8.8.8.8'):
    """Ping a host and return the latency."""
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.splitlines()[-1]
            latency = output.split('time=')[-1].split(' ms')[0]
            return latency
        else:
            return 'N/A'
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return 'N/A'

def get_wifi_info():
    """Get information about Wi-Fi adapters."""
    try:
        if platform.system() == 'Windows':
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
            return result.stdout
        elif platform.system() == 'Linux':
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            return result.stdout
        else:
            return 'N/A'
    except Exception as e:
        print(f"Error getting Wi-Fi info: {e}")
        return 'N/A'