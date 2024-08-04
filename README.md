# Storage-Optimization-Simulation
It features flash storage emulation with specified size, tracking write counts and data. Users can run simulations with sequential, random, or mixed write patterns and measure performance metrics, such as read and write speeds over time.

# Flash Storage Simulator

1. This Python code simulates a basic flash storage device and its performance under different usage patterns. It's a starting point for understanding how flash storage works and can be extended to explore:

2. Wear leveling algorithms: Implement and compare different wear leveling techniques to see how they impact the lifespan of the flash storage.

3. Garbage collection: Add a garbage collection mechanism to reclaim unused blocks and improve write performance.

4. Realistic performance metrics: Replace the dummy performance data with more accurate measurements by simulating read/write latencies, erase cycles, etc.

5. Error correction: Introduce error correction mechanisms to handle bit errors that occur in flash memory.

## How it works:

FlashStorage Class: Represents the flash storage device. --->  Stores data in a NumPy array. --->  Tracks the number of writes to each memory location for potential wear leveling implementation. --->  Provides write, read, and (placeholder for) garbage_collection methods.

Simulation Class: Simulates different usage scenarios. --->  Supports sequential, random, and mixed access patterns. --->  Provides a measure_performance method (currently using placeholder data).

Main Execution: Creates a FlashStorage object. --->  Creates a Simulation object, passing the storage object. --->  Runs the simulation using the specified access pattern (sequential, random, or mixed). --->  Measures and prints performance metrics.

## How to run:

1. Make sure you have Python installed along with the NumPy and Matplotlib libraries.

2. Save the code as a Python file (e.g., flash_simulator.py).

3. Run the code from your terminal using python flash_simulator.py.

## Customization:

``storage_size: Change the size of the simulated flash storage (in units of data).``

``pattern: Select the access pattern for the simulation.``

![image](https://github.com/user-attachments/assets/e2a252ae-7280-4f02-9475-7b03046e3323)

    Metrics: {'time': [0, 1, 2, 3, 4], 'read_speed': [25.565523345928874, 26.96690539580012, 19.808398168725503, 13.706971739587656, 29.9163058591927], 'write_speed': [6.293557610386996, 9.714573193542654, 5.680930992421066, 14.438508573508194, 14.649249408484396]}

## Future improvements:

1.Implement wear leveling algorithms to distribute writes evenly and extend lifespan.

2.Add a garbage collection mechanism to reclaim unused blocks.

3.Replace dummy performance data with more realistic measurements based on simulated operations.

4. Consider error correction techniques to handle bit errors.


5. Explore different flash memory technologies (SLC, MLC, TLC, QLC) and their characteristics.
