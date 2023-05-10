import matplotlib.pyplot as plt
import numpy as np

def read_data(filename) :
    data = []
    file = open(filename, 'r')
    line = file.readline()

    while line :
        line = line.strip()
        data.append(line.split(','))
        line = file.readline()
    
    file.close()

    for i in range(0, len(data)):
        count = 0
        while count < len (data[i]):
            data[i][count] = float(data[i][count])
            count+=1
    return data

APM1_arr = np.array(read_data ("APM1_metrics.csv"))
APM2_arr = np.array(read_data ("APM2_metrics.csv"))
APM3_arr = np.array(read_data ("APM3_metrics.csv"))
APM4_arr = np.array(read_data ("APM4_metrics.csv"))
APM5_arr = np.array(read_data ("APM5_metrics.csv"))
APM6_arr = np.array(read_data ("APM6_metrics.csv"))
sys_metrics_arr = np.array (read_data ("system_metrics.csv"))


# CPU Utilization
plt.plot(APM1_arr [:, 0], APM1_arr [:, 1], color='blue', label='APM1')
plt.plot(APM2_arr [:, 0], APM2_arr [:, 1], color='black', label='APM2')
plt.plot(APM3_arr [:, 0], APM3_arr [:, 1], color='red', label='APM3')
plt.plot(APM4_arr [:, 0], APM4_arr [:, 1], color='green', label='APM4')
plt.plot(APM5_arr [:, 0], APM5_arr [:, 1], color='yellow', label='APM5')
plt.plot(APM6_arr [:, 0], APM6_arr [:, 1], color='cyan', label='APM6')
plt.legend(loc='upper right')
plt.ylabel('CPU (%)')
plt.xlabel('Time (seconds)')
plt.title('CPU Utilization')
plt.xlim (5, 900)
plt.ylim (0, 100)
plt.savefig('cpu.png')
plt.close()

# Memory Utilization
plt.plot(APM1_arr [:, 0], APM1_arr [:, 2], color='blue', label='APM1')
plt.plot(APM2_arr [:, 0], APM2_arr [:, 2], color='black', label='APM2')
plt.plot(APM3_arr [:, 0], APM3_arr [:, 2], color='red', label='APM3')
plt.plot(APM4_arr [:, 0], APM4_arr [:, 2], color='green', label='APM4')
plt.plot(APM5_arr [:, 0], APM5_arr [:, 2], color='yellow', label='APM5')
plt.plot(APM6_arr [:, 0], APM6_arr [:, 2], color='cyan', label='APM6')
plt.legend(loc='upper right')
plt.ylabel('Memory (%)')
plt.xlabel('Time (seconds)')
plt.title('Memory Utilization')
plt.xlim (5, 900)
plt.ylim(0, 15)
plt.savefig('memory.png')
plt.close()

# Bandwidth Utilization
plt.plot(sys_metrics_arr [:, 0], sys_metrics_arr [:, 1], color='blue', label="RX Data Rate")
plt.plot(sys_metrics_arr [:, 0], sys_metrics_arr [:, 2], color='red', label="TX Data Rates")
plt.legend(loc='upper right')
plt.ylabel('Data Rate (Kb/sec)')
plt.xlabel('Time (seconds)')
plt.title('Bandwidth Utilization')
plt.xlim (5, 900)
plt.ylim (0, 100)
plt.savefig('bandwidth.png')
plt.close()

# Hard Disk Access Rates
plt.plot(sys_metrics_arr [:, 0], sys_metrics_arr [:, 3], color='blue')
plt.ylabel('Disk Writes (Kb/s)')
plt.xlabel('Time (seconds)')
plt.title('Hard Disk Access Rates')
plt.xlim (5, 900)
plt.savefig('disk_access.png')
plt.close()

# Hard Disk Utilization
plt.plot(sys_metrics_arr [:, 0], sys_metrics_arr [:, 4], color='blue')
plt.ylabel('Disk Capacity (MB)')
plt.xlabel('Time (seconds)')
plt.title('Hard Disk Utilization')
plt.xlim (5, 900)
plt.savefig('disk_util.png')
plt.close()