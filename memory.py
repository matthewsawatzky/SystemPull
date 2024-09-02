import psutil

def get_memory_usage():
    """Get memory usage statistics."""
    try:
        mem = psutil.virtual_memory()
        return {
            'memory_used': mem.used // (1024 ** 2),
            'memory_free': mem.available // (1024 ** 2)
        }
    except Exception as e:
        print(f"Error getting memory usage: {e}")
        return {
            'memory_used': 'N/A',
            'memory_free': 'N/A'
        }