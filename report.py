from datetime import datetime


def _format_bytes(value):
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(value)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024


def print_report(data):
    print()
    print("=" * 58)
    print("                 G H O S T")
    print("          SYSTEM COLLECTION REPORT")
    print("=" * 58)

    print(f"Started:  {data['started_at']}")
    print(f"Finished: {data['finished_at']}")

    print("\n[SYSTEM]")
    for key, value in data["system"].items():
        print(f"{key.replace('_', ' ').title():28} {value}")

    print("\n[RESOURCES]")
    resources = data["resources"]
    print(f"{'CPU logical cores':28} {resources['cpu_logical_cores']}")
    print(f"{'Home disk total':28} {_format_bytes(resources['home_disk_total_bytes'])}")
    print(f"{'Home disk used':28} {_format_bytes(resources['home_disk_used_bytes'])}")
    print(f"{'Home disk free':28} {_format_bytes(resources['home_disk_free_bytes'])}")

    print("\n[SELECTED ENVIRONMENT]")
    if data["environment"]:
        for key, value in data["environment"].items():
            print(f"{key:28} {value}")
    else:
        print("No selected environment variables were available.")

    print("\n[FILESYSTEM]")
    for key, value in data["filesystem"].items():
        print(f"{key.replace('_', ' ').title():28} {value}")

    print("\n" + "=" * 58)
    print("              COLLECTION COMPLETE")
    print("=" * 58)
    print()
