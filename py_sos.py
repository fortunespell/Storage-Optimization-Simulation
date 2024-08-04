import numpy as np
import matplotlib.pyplot as plt
import time

class FlashStorage:
    def __init__(self, size):
        self.size = size
        self.storage = np.zeros(size)
        self.write_count = np.zeros(size)
        self.total_writes = 0

    def write(self, address, data):
        if 0 <= address < self.size:
            self.storage[address] = data
            self.write_count[address] += 1
            self.total_writes += 1
            # Implement wear leveling here if needed
        else:
            raise IndexError("Address out of range")

    def read(self, address):
        if 0 <= address < self.size:
            return self.storage[address]
        else:
            raise IndexError("Address out of range")

    def garbage_collection(self):
        # Implement garbage collection here
        pass

class Simulation:
    def __init__(self, storage):
        self.storage = storage

    def run(self, pattern):
        if pattern == 'sequential':
            self.sequential_pattern()
        elif pattern == 'random':
            self.random_pattern()
        elif pattern == 'mixed':
            self.mixed_pattern()
        else:
            raise ValueError("Unknown pattern")

    def sequential_pattern(self):
        for i in range(self.storage.size):
            self.storage.write(i, i % 256)
            time.sleep(0.01)  # Simulate time delay for the write operation

    def random_pattern(self):
        np.random.seed(0)  # For reproducibility
        for _ in range(self.storage.size):
            address = np.random.randint(0, self.storage.size)
            self.storage.write(address, np.random.randint(0, 256))
            time.sleep(0.01)  # Simulate time delay for the write operation

    def mixed_pattern(self):
        self.sequential_pattern()
        self.random_pattern()

    def measure_performance(self):
        # Dummy performance data
        times = np.arange(0, 5)
        read_speeds = np.random.uniform(10, 30, size=len(times))
        write_speeds = np.random.uniform(5, 15, size=len(times))
        
        return {
            'time': times.tolist(),
            'read_speed': read_speeds.tolist(),
            'write_speed': write_speeds.tolist()
        }

def plot_metrics(metrics):
    if metrics is None:
        print("No metrics to plot")
        return
    
    plt.plot(metrics['time'], metrics['read_speed'], label='Read Speed', marker='o')
    plt.plot(metrics['time'], metrics['write_speed'], label='Write Speed', marker='x')
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (MB/s)')
    plt.title('Performance Metrics')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    storage_size = 1024  # Size of the flash storage
    storage = FlashStorage(size=storage_size)
    simulation = Simulation(storage)
    
    pattern = 'mixed'  # Choose from 'sequential', 'random', 'mixed'
    simulation.run(pattern)
    
    metrics = simulation.measure_performance()
    print(f"Metrics: {metrics}")  # Debugging line
    if metrics:
        plot_metrics(metrics)
    else:
        print("No metrics data returned")
