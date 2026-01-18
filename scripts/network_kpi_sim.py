import numpy as np
import matplotlib.pyplot as plt

# Simulated number of active users per cell
users = np.arange(10, 110, 10)

# Simulated KPI models (illustrative, not vendor-accurate)
latency_4g_ms = 50 + users * 0.30
latency_5g_ms = 20 + users * 0.10

throughput_4g_mbps = 120 - users * 0.6
throughput_5g_mbps = 250 - users * 0.4

# ----- Plot 1: Latency under load -----
plt.figure()
plt.plot(users, latency_4g_ms, label="4G LTE Latency (ms)")
plt.plot(users, latency_5g_ms, label="5G Latency (ms)")
plt.xlabel("Active Users per Cell")
plt.ylabel("Latency (ms)")
plt.title("4G vs 5G Latency Under Load (Simulated)")
plt.legend()
plt.tight_layout()
plt.savefig("latency_under_load.png", dpi=200)

# ----- Plot 2: Throughput under load -----
plt.figure()
plt.plot(users, throughput_4g_mbps, label="4G LTE Throughput (Mbps)")
plt.plot(users, throughput_5g_mbps, label="5G Throughput (Mbps)")
plt.xlabel("Active Users per Cell")
plt.ylabel("Throughput (Mbps)")
plt.title("4G vs 5G Throughput Under Load (Simulated)")
plt.legend()
plt.tight_layout()
plt.savefig("throughput_under_load.png", dpi=200)

print("Saved: latency_under_load.png, throughput_under_load.png")

