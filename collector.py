import os
import platform
import shutil
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path


class GhostCollector:
    def __init__(self):
        self.data = {
            "project": "GHOST",
            "started_at": datetime.now(timezone.utc).isoformat(),
            "system": {},
            "resources": {},
            "environment": {},
            "filesystem": {}
        }

    def collect(self):
        self._collect_system()
        self._collect_resources()
        self._collect_environment()
        self._collect_filesystem()
        self.data["finished_at"] = datetime.now(timezone.utc).isoformat()
        return self.data

    def _collect_system(self):
        self.data["system"] = {
            "operating_system": platform.system(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor() or "Unavailable",
            "architecture": platform.architecture()[0],
            "hostname": socket.gethostname(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "executable": sys.executable
        }

    def _collect_resources(self):
        usage = shutil.disk_usage(Path.home())
        self.data["resources"] = {
            "cpu_logical_cores": os.cpu_count(),
            "home_disk_total_bytes": usage.total,
            "home_disk_used_bytes": usage.used,
            "home_disk_free_bytes": usage.free
        }

    def _collect_environment(self):
        allowed_keys = ["LANG", "LC_ALL", "LC_CTYPE", "TZ", "TERM"]
        self.data["environment"] = {
            key: os.environ[key]
            for key in allowed_keys
            if key in os.environ
        }

    def _collect_filesystem(self):
        home = Path.home()
        self.data["filesystem"] = {
            "home_directory_name": home.name,
            "home_directory_exists": home.exists(),
            "home_directory_is_directory": home.is_dir()
        }
