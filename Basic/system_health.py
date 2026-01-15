import psutil

def system_health():

    print("*****Checking System Health*****")

    print("=========CPU Usage===========")
    cpu=int(input("Enter CPU threshold value: "))
    current_cpu=int(psutil.cpu_percent(interval=1))
    print("Current CPU usage is: ", current_cpu)
    if current_cpu > cpu:
        print("Current CPU value is", current_cpu , "and exeeding the threshold CPU value of", cpu, "so an email alert is being generated..")
    else:
        print("CPU is healthy")

    print("=========Disk Usage===========")
    disk=int(input("Enter Disk threshold value: "))
    system_disk=psutil.disk_usage('.')
    current_disk_used=round(system_disk.percent)
    print("Current Disk usage is: ", current_disk_used)
    if current_disk_used > disk:
        print("Disk Alert emial sent...")
    else:
        print("Disk is healthy")

    print("=========Memory Usage===========")
    memory=int(input("Enter Memory threshold value: "))
    system_memory = psutil.virtual_memory()
    memory_used = round(system_memory.percent)
    print("Current Memory usage is: ", memory_used)
    if memory_used > memory:
        print("Memory Alert emial sent...")
    else:
        print("Memory is healthy")

    print("*****System Health Check Completed*****")


system_health()


