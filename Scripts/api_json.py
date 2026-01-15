import psutil
import sys

print('********** CHECKING SYSTEM HEALTH **********')

env = input("Enter your Environment: ").capitalize()

thresholds = {
    "Test": 10,
    "Stage": 15,
    "Dev": 20,
    "QA": 25,
    "Prod": 30
}

if env not in thresholds:
    print(f"{env} is an invalid environment. Valid options: Test, Stage, Dev, QA, Prod")
    sys.exit()

threshold = thresholds[env]

print("\n========== CHECKING SYSTEM CPU ==========")
print(f"CPU Threshold for {env}: {threshold}%")

cpu_usage = psutil.cpu_percent(interval=1)
print("Current CPU Usage:", cpu_usage, "%")

if cpu_usage > threshold:
    print(f"ALERT: CPU usage {cpu_usage}% exceeds threshold {threshold}%")
else:
    print("System CPU is Healthy")

print("\n========== CHECKING SYSTEM DISK ==========")
disk_usage = round(psutil.disk_usage('.').percent)
print("Current Disk Usage:", disk_usage, "%")

if disk_usage > threshold:
    print(f"ALERT: Disk usage {disk_usage}% exceeds threshold {threshold}%")
else:
    print("System Disk is Healthy")

print("\n========== CHECKING SYSTEM MEMORY ==========")
memory_usage = round(psutil.virtual_memory().percent)
print("Current Memory Usage:", memory_usage, "%")

if memory_usage > threshold:
    print(f"ALERT: Memory usage {memory_usage}% exceeds threshold {threshold}%")
else:
    print("System Memory is Healthy")

print("\n********** SYSTEM HEALTH CHECK COMPLETED **********")
