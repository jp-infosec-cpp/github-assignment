

network_inventory = [

    {
        "hostname": "Router-1-B1",
        "device_type": "router",
        "management_ip": "10.1.1.1",
        "location": "building-1",
        "status": "up",
        "cpu_usage": 15,
        "memory_usage": 42,
        "uptime": 89,
        "backup_status": "completed"
    },

    {
        "hostname": "Switch-1-B1",
        "device_type": "switch",
        "management_ip": "10.1.1.50",
        "location": "building-1",
        "status": "up",
        "cpu_usage": 8,
        "memory_usage": 33,
        "uptime": 156,
        "backup_status": "completed"
    },

    {
        "hostname": "Router-2-B2",
        "device_type": "router",
        "management_ip": "10.1.1.254",
        "location": "building-2",
        "status": "down",
        "cpu_usage": 34,
        "memory_usage": 67,
        "uptime": 45,
        "backup_status": "failed"
    },

    {
        "hostname": "Switch-2-B2",
        "device_type": "switch",
        "management_ip": "10.1.2.50",
        "location": "building-2",
        "status": "down",
        "cpu_usage": 12,
        "memory_usage": 40,
        "uptime": 4,
        "backup_status": "completed"
    },

    {
        "hostname": "Router-3-B3",
        "device_type": "router",
        "management_ip": "10.1.3.20",
        "location": "building-3",
        "status": "up",
        "cpu_usage": 22,
        "memory_usage": 51,
        "uptime": 60,
        "backup_status": "completed"
    },

    {
        "hostname": "Switch-3-B3",
        "device_type": "switch",
        "management_ip": "10.2.1.1",
        "location": "building-3",
        "status": "up",
        "cpu_usage": 5,
        "memory_usage": 22,
        "uptime": 12,
        "backup_status": "failed"
    },

    {
        "hostname": "Router-4-B4",
        "device_type": "router",
        "management_ip": "10.1.1.60",
        "location": "building-4",
        "status": "up",
        "cpu_usage": 82,
        "memory_usage": 55,
        "uptime": 210,
        "backup_status": "completed"
    },

    {
        "hostname": "Switch-4-B4",
        "device_type": "switch",
        "management_ip": "10.1.1.70",
        "location": "building-4",
        "status": "up",
        "cpu_usage": 28,
        "memory_usage": 86,
        "uptime": 98,
        "backup_status": "completed"
    }
]

print("=== NETWORK REPORT ===")
print(f"\nTotal devices monitored: {len(network_inventory)}")
print("\n--- DEVICE STATUS SUMMARY ---")

for device in network_inventory:
    status_indicator = "OK" if device["status"] == "up" else "NOK"
    print(
        f"{status_indicator} "
        f"{device['hostname']:15} | "
        f"{device['device_type']:12} | "
        f"{device['management_ip']:12} | "
        f"{device['location']:15} | "
        f"CPU: {device['cpu_usage']:5}% | "
        f"Memory: {device['memory_usage']:5}%"
    )

print("\n--- DEVICES BY TYPE ---")
total = {}
for x in network_inventory:
    ro_sw = x["device_type"]
    if ro_sw in total:
        total[ro_sw] += 1
    else:
        total[ro_sw] = 1

for x in total:
    print(f"{x}: {total[x]}")

