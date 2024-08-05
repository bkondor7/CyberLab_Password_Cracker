'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True
    except (RuntimeError):
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip().decode('utf-8')
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    return
                else:
                    print(f"[-] Attempted password: {password} - Incorrect")
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()