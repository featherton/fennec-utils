# Import everything needed
import os
import sys

# Define all of the functions that will be used in the program

def help():
    print('''
    fennec-utils avalible commands:

    --mount-vdi  | Mount a given vdi disk image
    --unmount    | Unmount and disconnect all mounted drives
    --reset      | Reset modules in case of an error
    --help       | Print this menu
    ========================================================
    fennec-utils is created by: Featherton
    ''')

def mountvdi():
    if len(sys.argv) == 2:
        print("No disk image was given.")
    else:
        print("Attmempting to unload existing nbd modules...")
        os.system("sudo rmmod nbd")
        print("Attempting to load nbd module...")
        os.system("sudo modprobe nbd max_part=16")
        os.system("sudo qemu-nbd -c /dev/nbd0 " + sys.argv[2])
        print("Assuming everything completed without error.")
        print("Everything should be mounted correctly now...")
        print("If something did fail, run fennec-utils with --reset before trying again")

def unmount():
    input("Please eject all vdi partitions and strike [enter]")
    print("Disconnecting nbd device...")
    os.system("sudo qemu-nbd -d /dev/nbd0")
    print("Disconnected nbd device, trying to unload nbd...")
    os.system("sudo rmmod nbd")
    print("Disconnected nbd module...")

def reset():
    print("Resetting...")
    os.system("sudo qemu-nbd -d /dev/nbd0")
    os.system("sudo rmmod nbd")

def parseArguments():
    if len(sys.argv) == 1:
        print("No command line arguments given...")
    else:
        if sys.argv[1] == "--help":
            help()
        elif sys.argv[1] == "--unmount":
            unmount()
        elif sys.argv[1] == "--reset":
            reset()
        elif sys.argv[1] == "--mount-vdi":
            mountvdi()
            
parseArguments()
