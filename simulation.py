import os
import time
import random
import socket

def hide_source_ip():
    """Hides the source IP using a spoofed IP."""
    octets = [str(random.randint(1, 255)) for _ in range(4)]
    spoofed_ip = ".".join(octets)
    return spoofed_ip

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

if __name__ == "__main__":
    if not os.path.exists("/data/data/com.termux/files/home"):
        print("This script is optimized for Termux. Please run it in the Termux environment.")
        exit(1)
    target_ip = "192.168.0.1"  # Replace with a controlled environment IP
    duration = 10  # Simulate for 10 seconds
    simulate_ddos_attack(target_ip, duration)