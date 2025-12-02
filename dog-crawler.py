import platform
import os
import sys
import glob
import subprocess
import time

print("[+] Updating from git...")
os.system('git pull')

arc = platform.uname().machine.lower()
bit = platform.architecture()[0]

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def show_step_by_step_install():
    print("\n" + "="*60)
    print("[+] STEP-BY-STEP INSTALLATION")
    print("="*60)
    
    if arc in ["armv7l", "armv6l", "armhf", "aarch64"] or arc.startswith("arm"):
        print("\n[+] For ARM/Termux devices:")
        print("\n1. Install dependencies:")
        print("   \033[92mpkg update -y && pkg install -y git curl build-essential openssl readline libffi zlib\033[0m")
        
        print("\n2. Install pyenv:")
        print("   \033[92mcurl https://pyenv.run | bash\033[0m")
        
        print("\n3. Add pyenv to PATH (temporary for current session):")
        print("   \033[92mexport PATH=\"$HOME/.pyenv/bin:$PATH\"\033[0m")
        print("   \033[92meval \"$(pyenv init -)\"\033[0m")
        print("   \033[92meval \"$(pyenv virtualenv-init -)\"\033[0m")
        
        print("\n4. Install Python 3.12.0:")
        print("   \033[92mpyenv install 3.12.0\033[0m")
        
        print("\n5. Use Python 3.12.0 for current directory:")
        print("   \033[92mpyenv local 3.12.0\033[0m")
        
        print("\n6. Install required packages:")
        print("   \033[92mpip install requests>=2.28.0 fake-useragent>=1.1.0 colorama>=0.4.0 urllib3>=1.26.0 bs4>=0.0.2 cython>=3.2.2\033[0m")
        
        print("\n7. Run the tool:")
        print("   \033[92mpython dog-crawler.py\033[0m")
        
    else:
        print("\n[+] For Linux PC:")
        print("\n1. Install dependencies:")
        print("   \033[92msudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git\033[0m")
        
        print("\n2. Install pyenv:")
        print("   \033[92mcurl https://pyenv.run | bash\033[0m")
        
        print("\n3. Add pyenv to PATH (temporary for current session):")
        print("   \033[92mexport PATH=\"$HOME/.pyenv/bin:$PATH\"\033[0m")
        print("   \033[92meval \"$(pyenv init -)\"\033[0m")
        print("   \033[92meval \"$(pyenv virtualenv-init -)\"\033[0m")
        
        print("\n4. Install Python 3.13.0:")
        print("   \033[92mpyenv install 3.13.0\033[0m")
        
        print("\n5. Use Python 3.13.0 for current directory:")
        print("   \033[92mpyenv local 3.13.0\033[0m")
        
        print("\n6. Install required packages:")
        print("   \033[92mpip install requests>=2.28.0 fake-useragent>=1.1.0 colorama>=0.4.0 urllib3>=1.26.0 bs4>=0.0.2 cython>=3.2.2\033[0m")
        
        print("\n7. Run the tool:")
        print("   \033[92mpython dog-crawler.py\033[0m")
    
    print("\n" + "="*60)
    print("[+] IMPORTANT: Run steps 1-6 in order")
    print("[+] For permanent pyenv setup, add lines from step 3 to ~/.bashrc")
    print("="*60 + "\n")

def check_pyenv_installed():
    pyenv_path = os.path.expanduser("~/.pyenv")
    if os.path.exists(pyenv_path):
        return True
    return False

def check_python_version_installed(version):
    if not check_pyenv_installed():
        return False
    
    try:
        pyenv_bin = os.path.expanduser("~/.pyenv/bin")
        os.environ['PATH'] = pyenv_bin + os.pathsep + os.environ.get('PATH', '')
        
        result = subprocess.run(
            [os.path.join(pyenv_bin, 'pyenv'), 'versions', '--bare'],
            capture_output=True,
            text=True
        )
        
        installed_versions = result.stdout.strip().split('\n')
        return version in installed_versions
    except:
        return False

def setup_pyenv_temporarily():
    pyenv_path = os.path.expanduser("~/.pyenv")
    
    if not os.path.exists(pyenv_path):
        print("[!] pyenv not found. Please install it first.")
        show_step_by_step_install()
        return False
    
    pyenv_bin = os.path.join(pyenv_path, 'bin')
    os.environ['PATH'] = pyenv_bin + os.pathsep + os.environ.get('PATH', '')
    
    try:
        init_cmd = os.path.join(pyenv_bin, 'pyenv') + ' init -'
        result = subprocess.run(init_cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            exec(result.stdout)
    except:
        pass
    
    return True

def check_package_version(package_name, required_version):
    try:
        import importlib.metadata
        installed_version = importlib.metadata.version(package_name.replace("-", "_"))
        
        from packaging import version
        if version.parse(installed_version) >= version.parse(required_version):
            return True, installed_version
        else:
            return False, installed_version
    except:
        return False, None

def check_requirements():
    print("[+] Checking requirements...")
    
    current_version = sys.version_info
    print(f"[+] Current Python: {current_version.major}.{current_version.minor}.{current_version.micro}")
    
    required_version = None
    module_name = None
    
    if arc in ["armv7l", "armv6l", "armhf"] or arc.startswith("arm") and not arc.startswith("aarch"):
        required_version = (3, 12, 0)
        module_name = "ang32"
        required_version_str = "3.12.0"
    
    elif arc == "aarch64":
        required_version = (3, 12, 0)
        module_name = "ang64"
        required_version_str = "3.12.0"
    
    elif arc in ["i386", "i686", "x86"] or bit == "32bit":
        required_version = (3, 13, 0)
        module_name = "linux32"
        required_version_str = "3.13.0"
    
    elif arc == "x86_64" or bit == "64bit":
        required_version = (3, 13, 0)
        module_name = "linux64"
        required_version_str = "3.13.0"
    
    else:
        print("[+] Please Contact Admin Whatsapp - +94721986326")
        exit(f"[!] Unknown Device Architecture → {arc}")
    
    version_ok = False
    if (current_version.major, current_version.minor) == (required_version[0], required_version[1]):
        version_ok = True
    else:
        if check_pyenv_installed() and check_python_version_installed(required_version_str):
            print(f"[+] Required Python {required_version_str} is installed via pyenv")
            print("[+] Setting up pyenv temporarily...")
            if setup_pyenv_temporarily():
                pyenv_bin = os.path.expanduser("~/.pyenv/bin")
                subprocess.run([os.path.join(pyenv_bin, 'pyenv'), 'local', required_version_str])
                print(f"[+] Switched to Python {required_version_str}")
                print("[+] Please restart the script")
                exit(0)
    
    if not version_ok:
        print(f"[!] Wrong Python version!")
        print(f"[+] Required: Python {required_version[0]}.{required_version[1]}.x")
        print(f"[+] Current: Python {current_version.major}.{current_version.minor}.{current_version.micro}")
        
        if check_pyenv_installed():
            print(f"\n[+] pyenv is installed. You can switch to Python {required_version_str}:")
            print(f"    \033[92mcd {os.getcwd()}\033[0m")
            print(f"    \033[92mexport PATH=\"$HOME/.pyenv/bin:$PATH\"\033[0m")
            print(f"    \033[92meval \"$(pyenv init -)\"\033[0m")
            print(f"    \033[92mpyenv install {required_version_str}\033[0m")
            print(f"    \033[92mpyenv local {required_version_str}\033[0m")
            print(f"    \033[92mpython dog-crawler.py\033[0m")
        else:
            show_step_by_step_install()
        exit(1)
    
    module_found = False
    module_file = None
    
    so_files = glob.glob(f"{module_name}*.so")
    if so_files:
        module_found = True
        module_file = so_files[0]
    
    if not module_found and os.path.exists(f"{module_name}.py"):
        module_found = True
        module_file = f"{module_name}.py"
    
    if not module_found:
        print(f"[!] Module '{module_name}' not found!")
        print(f"[+] Looking for: {module_name}.so or {module_name}.py")
        print("[+] Available files:")
        for f in glob.glob("*"):
            print(f"  - {f}")
        print("\n[+] Please Contact Admin Whatsapp - +94721986326")
        exit(1)
    
    return module_name, module_file

def check_packages():
    print("[+] Checking packages...")
    
    packages_to_check = [
        ("requests", "2.28.0"),
        ("fake-useragent", "1.1.0"),
        ("colorama", "0.4.0"),
        ("urllib3", "1.26.0"),
        ("bs4", "0.0.2"),
        ("cython", "3.2.2")
    ]
    
    missing_packages = []
    outdated_packages = []
    
    try:
        import packaging
    except ImportError:
        print("[+] Installing packaging module for version checking...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "packaging"])
        import packaging
    
    for package_name, required_version in packages_to_check:
        try:
            import_name = package_name.replace("-", "_")
            __import__(import_name)
            
            version_ok, installed_version = check_package_version(package_name, required_version)
            
            if version_ok:
                print(f"[✓] {package_name} {installed_version} (>= {required_version})")
            else:
                print(f"[!] {package_name} {installed_version} (needs >= {required_version})")
                outdated_packages.append(f"{package_name}>={required_version}")
        except ImportError:
            print(f"[!] {package_name} - MISSING")
            missing_packages.append(f"{package_name}>={required_version}")
    
    if missing_packages or outdated_packages:
        all_packages = missing_packages + outdated_packages
        print(f"\n[!] Need to install/upgrade packages")
        print("[+] Install with:")
        print("    \033[92mpip install " + " ".join(all_packages) + "\033[0m")
        
        print("\n[+] Installing packages now...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + all_packages)
            print("[✓] Packages installed successfully")
            return True
        except:
            print("[!] Failed to install packages")
            return False
    
    return True

def run_module(module_name, module_file):
    clear_screen()
    print(f"[+] Architecture: {arc} ({bit})")
    print(f"[+] Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"[+] Running: {module_name}")
    print(f"[+] Module: {module_file}")
    print("-" * 50)
    
    try:
        __import__(module_name).main()
    except Exception as e:
        print(f"[!] Error running module: {str(e)[:100]}...")
        print("[+] Please Contact Admin Whatsapp - +94721986326")
        exit(1)

def main():
    print(f"[+] Architecture: {arc} ({bit})")
    
    module_name, module_file = check_requirements()
    
    if not check_packages():
        print("\n[!] Please install missing packages and run again")
        exit(1)
    
    print(f"\n[✓] Python version OK")
    print(f"[✓] Module found: {module_file}")
    print(f"[✓] All packages installed")
    os.system(f'xdg-open https://github.com/Prekarshamaxx123/dog-crawler')

    time.sleep(1)
    
    run_module(module_name, module_file)

if __name__ == "__main__":
    main()