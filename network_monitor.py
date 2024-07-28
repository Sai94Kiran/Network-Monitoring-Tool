import scapy.all as scapy
import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import time

# Function to capture network packets
def capture_packets(packet_count=100):
    packets = scapy.sniff(count=packet_count)
    return packets

# Function to monitor CPU and memory usage
def monitor_system_usage(duration=60, interval=1):
    cpu_usage = []
    memory_usage = []
    timestamps = []
    end_time = time.time() + duration
    
    while time.time() < end_time:
        cpu = psutil.cpu_percent(interval=interval)
        memory = psutil.virtual_memory().percent
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        cpu_usage.append(cpu)
        memory_usage.append(memory)
        timestamps.append(timestamp)
        
        print(f"Time: {timestamp}, CPU Usage: {cpu}%, Memory Usage: {memory}%")
    
    return cpu_usage, memory_usage, timestamps

# Function to detect anomalies in network usage
def detect_anomalies(packets, threshold=1e6):
    anomalies = []
    for packet in packets:
        if hasattr(packet, 'len') and packet.len > threshold:
            anomalies.append(packet)
    return anomalies

# Function to visualize data
def visualize_data(cpu_usage, memory_usage, timestamps):
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, cpu_usage, label='CPU Usage (%)')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(timestamps, memory_usage, label='Memory Usage (%)', color='red')
    plt.xlabel('Time')
    plt.ylabel('Memory Usage (%)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    print("Starting network packet capture...")
    packets = capture_packets()
    
    print("Monitoring system usage...")
    cpu_usage, memory_usage, timestamps = monitor_system_usage()
    
    print("Detecting anomalies in network usage...")
    anomalies = detect_anomalies(packets)
    
    if anomalies:
        print(f"Detected {len(anomalies)} anomalies in network usage.")
    else:
        print("No anomalies detected.")
    
    print("Visualizing system usage data...")
    visualize_data(cpu_usage, memory_usage, timestamps)

if __name__ == "__main__":
    main()
