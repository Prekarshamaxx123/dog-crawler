import platform
import os
import sys
import subprocess
import importlib.util
import pkg_resources


os.system('git pull')


arc = platform.uname().machine.lower()
bit = platform.architecture()[0]


REQUIRED_PACKAGES = [
    "requests>=2.28.0",
    "beautifulsoup4>=4.11.0",
    "fake-useragent>=1.1.0",
    "colorama>=0.4.0",
    "urllib3>=1.26.0",
    "bs4>=0.0.2",
    "cython>=3.2.2"
]

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def check_python_version(required_version_range):
    try:
        current_version = tuple(map(int, sys.version_info[:3]))
        min_version, max_version = required_version_range.split('-')
        min_ver = tuple(map(int, min_version.split('.')))
        max_ver = tuple(map(int, max_version.split('.')))
        
        return min_ver <= current_version <= max_ver
    except:
        return False

def install_python_version(version):
    print(f"[+] Installing Python {version}...")
    
    pyenv_path = os.path.expanduser("~/.pyenv")
    
    if os.path.exists(pyenv_path):
        print("[✓] pyenv already installed")
    else:
        print("[+] Installing pyenv and dependencies...")
        if 'termux' in sys.prefix.lower():
            termux_cmd = "pkg install -y git curl build-essential openssl readline libffi zlib"
            if subprocess.call(termux_cmd, shell=True) != 0:
                print("[!] Failed to install Termux dependencies")
                return False
            
            curl_cmd = "curl https://pyenv.run | bash"
            result = subprocess.call(curl_cmd, shell=True)
            if result != 0:
                print("[!] Failed to install pyenv")
                return False
            
            
            zshrc_path = os.path.expanduser("~/.zshrc")
            env_vars = '\nexport PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"'
            with open(zshrc_path, 'a') as f:
                f.write(env_vars)
            
            
            subprocess.call("source ~/.zshrc", shell=True)
        else:
            
            linux_cmd = "sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev git"
            if subprocess.call(linux_cmd, shell=True) != 0:
                print("[!] Failed to install Linux dependencies")
                return False
            
            curl_cmd = "curl https://pyenv.run | bash"
            result = subprocess.call(curl_cmd, shell=True)
            if result != 0:
                print("[!] Failed to install pyenv")
                return False
            
            
            bashrc_path = os.path.expanduser("~/.bashrc")
            env_vars = '\nexport PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"'
            with open(bashrc_path, 'a') as f:
                f.write(env_vars)
            
            
            subprocess.call("source ~/.bashrc", shell=True)
    
    
    print(f"[+] Installing Python {version} with pyenv...")
    print(f"[+] We Want One Minutes. Wait ...")

    install_cmd = f"~/.pyenv/bin/pyenv install {version} --skip-existing"
    if subprocess.call(install_cmd, shell=True) != 0:
        print(f"[!] Failed to install Python {version}")
        return False
    
    
    set_cmd = f"~/.pyenv/bin/pyenv local {version}"
    subprocess.call(set_cmd, shell=True)
    
    
    os.execv(sys.executable, [sys.executable] + sys.argv)

def check_and_install_packages():
    print("[+] Checking required packages...")
    
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    for package_spec in REQUIRED_PACKAGES:
        package_name = package_spec.split('>=')[0].split('==')[0].strip()
        required_version = package_spec.split('>=')[1] if '>=' in package_spec else None
        
        try:
            current_version = pkg_resources.get_distribution(package_name).version
            if required_version and pkg_resources.parse_version(current_version) < pkg_resources.parse_version(required_version):
                print(f"[!] {package_name} version {current_version} is older than required {required_version}")
                print(f"[+] Upgrading {package_name}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_spec])
            else:
                print(f"[✓] {package_name} {current_version} is installed")
        except pkg_resources.DistributionNotFound:
            print(f"[!] {package_name} is not installed")
            print(f"[+] Installing {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_spec])
        except Exception as e:
            print(f"[!] Error checking {package_name}: {e}")
            print(f"[+] Trying to install {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_spec])

def check_module_exists(module_name):
    possible_paths = [
        f"./{module_name}.py",
        f"./{module_name}/__init__.py"
    ]
    return any(os.path.exists(path) for path in possible_paths)

def run_module():
    module_to_run = None
    python_version_needed = None
    
    # ARM 32-bit (Termux/Linux)
    if arc in ["armv7l", "armv6l", "armhf"] or arc.startswith("arm") and not arc.startswith("aarch"):
        print("[+] ARM 32-bit architecture detected")
        if not check_python_version("3.12.0-3.12.99"):
            python_version_needed = "3.12.0"
        if check_module_exists("ang32"):
            module_to_run = "ang32"
        else:
            print("[!] ang32 module not found")
    
    # ARM 64-bit (Termux/Linux)  
    elif arc == "aarch64":
        print("[+] ARM 64-bit architecture detected")
        if not check_python_version("3.12.0-3.12.99"):
            python_version_needed = "3.12.0"
        if check_module_exists("ang64"):
            module_to_run = "ang64"
        else:
            print("[!] ang64 module not found")
    
    # Linux 32-bit (PC)
    elif arc in ["i386", "i686", "x86"] or bit == "32bit":
        print("[+] Linux 32-bit architecture detected")
        if not check_python_version("3.13.0-3.13.99"):
            python_version_needed = "3.13.0"
        if check_module_exists("ang32"):
            module_to_run = "ang32"
        else:
            print("[!] linux32 module not found")
    
    # Linux 64-bit (PC)
    elif arc == "x86_64" or bit == "64bit":
        print("[+] Linux 64-bit architecture detected")
        if not check_python_version("3.13.0-3.13.99"):
            python_version_needed = "3.13.0"
        if check_module_exists("linux64"):
            module_to_run = "linux64"
        else:
            print("[!] linux64 module not found")
    
    # Unknown Device
    else:
        print("[+] Please Contact Admin Whatsapp - +94721986326")
        exit(f"[!] Unknown Device Architecture → {arc}")
    
    
    if python_version_needed:
        print(f"[!] Python version {python_version_needed} required")
        if install_python_version(python_version_needed):
            print(f"[✓] Python {python_version_needed} installed successfully")
        else:
            print("[!] Failed to install required Python version")
            print("[+] Please Contact Admin Whatsapp - +94721986326")
            exit(1)
    
    
    check_and_install_packages()
    
    
    clear_screen()
    
    
    if module_to_run:
        try:
            print(f"[+] Running {module_to_run} module...")
            __import__(module_to_run).main()
        except Exception as e:
            print(f"[!] Error running module: {e}")
            print("[+] Please Contact Admin Whatsapp - +94721986326")
            exit(1)
    else:
        print("[!] No suitable module found for this architecture")
        print("[+] Please Contact Admin Whatsapp - +94721986326")
        exit(1)

if __name__ == "__main__":
    run_module()