import platform
import os

# Git update
os.system('git pull')

# Architecture detection
arc = platform.uname().machine.lower()
bit = platform.architecture()[0]


def run_module():
    # ARM 32-bit (Termux/Linux)
    if arc in ["armv7l", "armv6l", "armhf"] or arc.startswith("arm") and not arc.startswith("aarch"):
        print("[+] Running ARM 32-bit version")
        __import__("pre32").main()
    
    # ARM 64-bit (Termux/Linux)  
    elif arc == "aarch64":
        print("[+] Running ARM 64-bit version")
        __import__("ang64").main()
    
    # Linux 32-bit (PC)
    elif arc in ["i386", "i686", "x86"] or bit == "32bit":
        print("[+] Running Linux 32-bit version")
        __import__("pre32").main()
    
    # Linux 64-bit (PC)
    elif arc == "x86_64" or bit == "64bit":
        print("[+] Running Linux 64-bit version")
        __import__("linux64").main()
    
    # Unknown Device
    else:
        print("[+] Please Contact Admin Whatsapp - +94721986326")
        exit(f"[!] Unknown Device Architecture → {arc}")

if __name__ == "__main__":
    run_module()
