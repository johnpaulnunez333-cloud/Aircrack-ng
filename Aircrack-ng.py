import subprocess
import os
import sys
import time

def print_banner():
    banner = r"""
    ###############################################################
    #                                                             #
    #     ___   _________  __________  ___   __________ __  _______ #
    #    /   | /  _/ __ \/ ____/ __ \/   | / ____/ __//_/ / ____/ #
    #   / /| | / // /_/ / /   / /_/ / /| |/ /   / /_ / / / / __   #
    #  / ___ |/ // _, _/ /___/ _, _/ ___ / /___/ __// / / /_/ /   #
    # /_/  |_/___/_/ |_|\____/_/ |_/_/  |_\____/_/  /_/  \____/    #
    #                                                             #
    #        [ INDUSTRIAL AUDIT TOOL - TERMUX V2.0 ]              #
    #                                                             #
    ###############################################################
    """
    print(banner)

def setup_environment():
    print("[*] Initializing system dependencies...")
    subprocess.call(["pkg", "update", "-y"])
    subprocess.call(["pkg", "install", "aircrack-ng", "python", "-y"])
    print("[+] Dependencies verified successfully.")

def check_file_health(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(file_path) / (1024 * 1024)
        print(f"[#] Verified: {os.path.basename(file_path)} ({size:.2f} MB)")
        return True
    return False

def run_audit_session(wordlist, cap_file):
    if not check_file_health(wordlist) or not check_file_health(cap_file):
        print("[!] ERROR: Critical files missing. Check paths.")
        return

    print("\n[!] WARNING: High CPU Usage Detected.")
    print("[!] Ensure device is near a cooling source.")
    confirm = input("[?] Proceed with Audit? (y/n): ")
    
    if confirm.lower() == 'y':
        start_time = time.time()
        print(f"[*] Audit Started at: {time.ctime()}")
        
        try:
            # Main Execution
            subprocess.call(["aircrack-ng", "-a", "2", "-w", wordlist, cap_file])
        except KeyboardInterrupt:
            print("\n[!] Session paused by user.")
        
        end_time = time.time()
        duration = (end_time - start_time) / 60
        print(f"[*] Session Duration: {duration:.2f} minutes.")
    else:
        print("[*] Audit aborted.")

def main():
    os.system('clear')
    print_banner()
    
    print("--- OPERATIONAL DASHBOARD ---")
    print("1. System Update & Tool Setup")
    print("2. Run WPA/WPA2 Audit (RockYou Method)")
    print("3. File Health Check")
    print("4. Exit")
    
    cmd = input("\n[>] Terminal Command: ")

    if cmd == '1':
        setup_environment()
    elif cmd == '2':
        cap = input("[Input] Path to .cap file: ").strip("'\" ")
        wd = input("[Input] Path to rockyou.txt: ").strip("'\" ")
        run_audit_session(wd, cap)
    elif cmd == '3':
        f = input("[Input] File to check: ").strip("'\" ")
        check_file_health(f)
    elif cmd == '4':
        sys.exit()
    else:
        print("Invalid Selection.")

if __name__ == "__main__":
    main()
