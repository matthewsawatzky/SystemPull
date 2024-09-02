import psutil

def get_cpu_usage():
    """Get CPU usage statistics."""
    try:
        system_cpu = psutil.cpu_percent(interval=1)
        per_cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        num_cores = psutil.cpu_count(logical=True)
        return {
            'system_cpu_usage': system_cpu,
            'user_cpu_usage': per_cpu_usage,
            'num_cores': num_cores
        }
    except Exception as e:
        print(f"Error getting CPU usage: {e}")
        return {
            'system_cpu_usage': 'N/A',
            'user_cpu_usage': 'N/A',
            'num_cores': 'N/A'
        }