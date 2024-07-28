# Network-Monitoring-Tool

## Overview

This tool captures and analyzes network packets, monitors CPU and memory usage, and detects anomalies in network usage. It also visualizes the system usage data.

## Features

- Captures over 100 network packets per minute using Python and Scapy.
- Tracks CPU and memory usage in real-time with Psutil.
- Implements anomaly detection for network usage spikes exceeding 1MB/s.
- Visualizes data trends with Matplotlib.

## Prerequisites

- Python
- [Npcap](https://nmap.org/npcap/) installed for packet capturing on Windows.

## Requirements 
- Check out requirements.txt

## Usage
-Run the script with administrator permissions (required for packet capturing):- python network_monitor.py
-Run the script for 60 seconds and then you will visualised info regarding memory and cpu usage accordingly with the time and anamoly detection in yout terminal.
The script will start capturing network packets and monitoring system usage. It will detect anomalies and visualize the data after the monitoring period.
