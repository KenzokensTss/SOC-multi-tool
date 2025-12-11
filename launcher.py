import os
import sys
import time

# Warna untuk tampilan (Opsional)
R = '\033[31m' # Merah
G = '\033[32m' # Hijau
C = '\033[36m' # Cyan
W = '\033[0m'  # Putih

def banner():
    os.system('clear')
    print(f"{C}========================================{W}")
    print(f"{C}       MY SOC ANALYST TOOLKIT           {W}")
    print(f"{C}========================================{W}")

def menu():
    banner()
    print(f"{G}[1]{W} OSINT / Recon (Nmap)")
    print(f"{G}[2]{W} SQL Injection Scanner (SQLmap)")
    print(f"{G}[3]{W} Brute Force (Hydra)")
    print(f"{G}[4]{W} Password Cracking (John The Ripper)")
    print(f"{G}[5]{W} Directory Busting (Gobuster)")
    print(f"{G}[0]{W} Keluar")
    print("-" * 40)

def main():
    while True:
        menu()
        pilihan = input(f"{C}Pilih menu > {W}")

        if pilihan == '1':
            target = input("Masukkan Target IP/Domain: ")
            # Menjalankan Nmap sebagai contoh Recon
            os.system(f"nmap -sV {target}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '2':
            url = input("Masukkan URL Target: ")
            os.system(f"sqlmap -u {url} --batch")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '3':
            print("Contoh: hydra -l admin -P passlist.txt ssh://192.168.1.1")
            cmd = input("Masukkan perintah Hydra lengkap: ")
            os.system(cmd)
            input("\nTekan Enter untuk kembali...")
        
        elif pilihan == '4':
            file_hash = input("Masukkan path file hash: ")
            os.system(f"john {file_hash}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '5':
            url = input("Masukkan URL Target: ")
            wordlist = input("Path wordlist (default: common.txt): ") or "common.txt"
            os.system(f"gobuster dir -u {url} -w {wordlist}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '0':
            print("Keluar...")
            sys.exit()
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
