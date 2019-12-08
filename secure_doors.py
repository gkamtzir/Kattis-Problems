from enum import Enum

# Defining the status enumeration
# needed for the status description.
class Status(Enum):
    ENTRY = "entry"
    EXIT = "exit"

n = int(input())

log = {}

# Main loop.
for i in range(n):
    status, name = input().split()
    
    if status == Status.ENTRY.value:
        if log.get(name) is not None:
            print(f"{name} entered (ANOMALY)")
        else:
            log[name] = True
            print(f"{name} entered")
    else:
        if log.get(name) is None:
            print(f"{name} exited (ANOMALY)")
        else:
            log[name] = None
            print(f"{name} exited")
            
        
