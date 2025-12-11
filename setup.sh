#!/bin/bash

# setup.sh
echo "[*] Mengupdate repository Termux..."
pkg update && pkg upgrade -y

echo "[*] Menginstal Python dan Git..."
pkg install python git -y

echo "[*] Menginstal Tools Pihak Ketiga..."
# Instalasi tool standar yang tersedia di repo Termux
pkg install nmap -y
pkg install sqlmap -y
pkg install hydra -y
pkg install john -y
pkg install gobuster -y

# Jika ada library python tambahan
pip install requests colorama

echo "[+] Instalasi Selesai! Jalankan: python launcher.py"
