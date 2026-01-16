import psutil
import sys

print('**********CHECKING SYSTEM HEALTH**********')

env=input("Enter your Environment:", )
cpu_range={
    "Test": 10,
    "Stage": 15,
    "Dev": 20,
    "QA": 25,
    "Prod": 30
}
disk_range={
    "Test": 10,
    "Stage": 15,
    "Dev": 20,
    "QA": 25,
    "Prod": 30
}
memory_range={
    "Test": 10,
    "Stage": 15,
    "Dev": 20,
    "QA": 25,
    "Prod": 30
}

print("                                          ")
print('==========CHECKING SYSTEM CPU==========')


if env == "Test":
    print("Your CPU Threshold value for", env, "environment is:",cpu_range["Test"])
    cpu_threshold = (cpu_range["Test"])
elif env == "Stage":
    print("Your CPU Threshold value is:",cpu_range["Stage"])
    cpu_threshold = (cpu_range["Stage"])
elif env == "Dev":
    print("Your CPU Threshold value is:",cpu_range["Dev"])
    cpu_threshold = (cpu_range["Dev"])
elif env == "QA":
    print("Your CPU Threshold value is:",cpu_range["QA"])
    cpu_threshold = (cpu_range["QA"])
elif env == "Prod":
    print("Your CPU Threshold value is:",cpu_range["Prod"])
    cpu_threshold = (cpu_range["Prod"])
else:
    print(env, "is invalid environment. Valid Environments are Test, Stage, Dev, QA or Prod. Re-run the script by entering valid environment")
    sys.exit()

system_cpu_usage = int(psutil.cpu_percent(interval=1))
print("Your current system CPU usage is:", system_cpu_usage)
if system_cpu_usage > cpu_threshold:
    print("As your current CPU usage", system_cpu_usage, "exceeds the threshold value", cpu_threshold, "an Alert is being sent...")
else:
    print("System CPU is Healthy")

print("                                          ")
print('==========CHECKING SYSTEM DISK==========')


if env == "Test":
    print("Your Disk Threshold value for", env, "environment is:",disk_range["Test"])
    disk_threshold = (disk_range["Test"])
elif env == "Stage":
    print("Your Disk Threshold value is:",disk_range["Stage"])
    disk_threshold = (disk_range["Stage"])
elif env == "Dev":
    print("Your Disk Threshold value is:",disk_range["Dev"])
    disk_threshold = (disk_range["Dev"])
elif env == "QA":
    print("Your Disk Threshold value is:",disk_range["QA"])
    disk_threshold = (disk_range["QA"])
elif env == "Prod":
    print("Your Disk Threshold value is:",disk_range["Prod"])
    disk_threshold = (disk_range["Prod"])
else:
    print(env, "is invalid environment. Valid Environments are Test, Stage, Dev, QA or Prod. Re-run the script by entering valid environment")
    sys.exit()

disk_used=psutil.disk_usage('.')
system_disk_usage=round(disk_used.percent)
print("Your current Disk usage is: ", system_disk_usage)
if system_disk_usage > disk_threshold:
    print("As your current Disk usage", system_disk_usage, "exceeds the threshold value", disk_threshold, "an Alert is being sent...")
else:
    print("System Disk is healthy")


print("                                          ")
print('==========CHECKING SYSTEM MEMORY==========')

if env == "Test":
    print("Your Memory Threshold value for", env, "environment is:",memory_range["Test"])
    memory_threshold = (memory_range["Test"])
elif env == "Stage":
    print("Your Memory Threshold value is:",memory_range["Stage"])
    memory_threshold = (memory_range["Stage"])
elif env == "Dev":
    print("Your Memory Threshold value is:",memory_range["Dev"])
    memory_threshold = (memory_range["Dev"])
elif env == "QA":
    print("Your Memory Threshold value is:",memory_range["QA"])
    memory_threshold = (memory_range["QA"])
elif env == "Prod":
    print("Your Memory Threshold value is:",memory_range["Prod"])
    memory_threshold = (memory_range["Prod"])
else:
    print(env, "is invalid environment. Valid Environments are Test, Stage, Dev, QA or Prod. Re-run the script by entering valid environment")
    sys.exit()


memory_used = psutil.virtual_memory()
system_memory_used = round(memory_used.percent)
print("Your current Memory usage is: ", system_memory_used)
if system_memory_used > memory_threshold:
    print("As your current Memory usage", system_memory_used, "exceeds the threshold value", memory_threshold, "an Alert is being sent...")
else:
    print("System Memory is healthy")

print("                                          ")
print('**********SYSTEM HEALTH CHECK COMPLETED**********')
