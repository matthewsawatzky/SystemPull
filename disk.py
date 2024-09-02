import psutil

def get_disk_info():
    """Get information about all connected drives."""
    try:
        partitions = psutil.disk_partitions()
        disks = []
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info = {
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'total_size_mb': usage.total // (1024 ** 2),
                    'used_size_mb': usage.used // (1024 ** 2),
                    'free_size_mb': usage.free // (1024 ** 2),
                    'temperature': 'N/A'
                }
                disks.append(disk_info)
            except Exception as e:
                print(f"Error getting disk info for {partition.device}: {e}")
                disks.append({
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'total_size_mb': 'N/A',
                    'used_size_mb': 'N/A',
                    'free_size_mb': 'N/A',
                    'temperature': 'N/A'
                })
        return disks
    except Exception as e:
        print(f"Error getting disk info: {e}")
        return []