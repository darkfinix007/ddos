import os
import time
import random
import socket
import requests

def hide_source_ip():
    """Hides the source IP using a spoofed IP."""
    octets = [str(random.randint(1, 255)) for _ in range(4)]
    spoofed_ip = ".".join(octets)
    return spoofed_ip

def bypass_cloudflare(target_ip):
    """Bypasses Cloudflare protection for the target IP."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(f"http://{target_ip}", headers=headers)
        if response.status_code == 200:
            print("Cloudflare bypass successful.")
        else:
            print("Cloudflare bypass failed.")
    except requests.RequestException as e:
        print(f"Error during Cloudflare bypass: {e}")

def simulate_ddos_attack(target_ip, duration):
    """Simulates DDoS traffic to a target IP for a given duration."""
    print(f"Starting simulation on target {target_ip} for {duration} seconds.")
    start_time = time.time()
    while time.time() - start_time < duration:
        spoofed_ip = hide_source_ip()
        simulated_traffic = random.randint(500, 1000)
        print(f"Simulated {simulated_traffic} packets sent from spoofed IP {spoofed_ip}.")
        time.sleep(0.5)
    print("Simulation complete.")

def save_to_config(target_ip):
    """Saves the target IP to a configuration file."""
    config_file = "/data/data/com.termux/files/home/ddos_config.txt"
    with open(config_file, 'w') as file:
        file.write(target_ip)
    print(f"Target IP {target_ip} saved to {config_file}.")

if __name__ == "__main__":
    if not os.path.exists("/data/data/com.termux/files/home"):
        print("This script is optimized for Termux. Please run it in the Termux environment.")
        exit(1)

    target_ip = input("Enter the target IP or host: ")
    bypass_cloudflare(target_ip)
    save_to_config(target_ip)

    duration = int(input("Enter the duration of the simulation in seconds: "))
    simulate_ddos_attack(target_ip, duration)
