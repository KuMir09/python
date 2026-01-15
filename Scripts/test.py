import psutil
import sys


def get_environment():
    """Get and validate environment input from user."""
    try:
        env = input("Enter your Environment: ").capitalize()
        valid_envs = thresholds.keys()

        if env not in valid_envs:
            raise ValueError(
                f"{env} is invalid. Valid environments: {', '.join(valid_envs)}"
            )

        return env

    except ValueError as error:
        print("ERROR:", error)
        sys.exit(1)


def check_cpu(threshold):
    """Check system CPU usage."""
    print("\n========== CHECKING SYSTEM CPU ==========")
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print("Current CPU Usage:", cpu_usage, "%")

        if cpu_usage > threshold:
            print(
                f"ALERT: CPU usage {cpu_usage}% exceeds threshold {threshold}%"
            )
        else:
            print("System CPU is Healthy")

    except Exception as error:
        print("ERROR: Unable to retrieve CPU usage.", error)


def check_disk(threshold):
    """Check system Disk usage."""
    print("\n========== CHECKING SYSTEM DISK ==========")
    try:
        disk_usage = round(psutil.disk_usage(".").percent)
        print("Current Disk Usage:", disk_usage, "%")

        if disk_usage > threshold:
            print(
                f"ALERT: Disk usage {disk_usage}% exceeds threshold {threshold}%"
            )
        else:
            print("System Disk is Healthy")

    except FileNotFoundError:
        print("ERROR: Disk path not found.")
    except Exception as error:
        print("ERROR: Unable to retrieve disk usage.", error)


def check_memory(threshold):
    """Check system Memory usage."""
    print("\n========== CHECKING SYSTEM MEMORY ==========")
    try:
        memory_usage = round(psutil.virtual_memory().percent)
        print("Current Memory Usage:", memory_usage, "%")

        if memory_usage > threshold:
            print(
                f"ALERT: Memory usage {memory_usage}% exceeds threshold {threshold}%"
            )
        else:
            print("System Memory is Healthy")

    except Exception as error:
        print("ERROR: Unable to retrieve memory usage.", error)


# ------------------- MAIN SCRIPT -------------------

print("********** CHECKING SYSTEM HEALTH **********")

thresholds = {
    "Test": 10,
    "Stage": 15,
    "Dev": 20,
    "QA": 25,
    "Prod": 30,
}

environment = get_environment()
env_threshold = thresholds[environment]

print(
    f"\nThreshold values for {environment} environment: {env_threshold}%"
)

check_cpu(env_threshold)
check_disk(env_threshold)
check_memory(env_threshold)

print("\n********** SYSTEM HEALTH CHECK COMPLETED **********")
