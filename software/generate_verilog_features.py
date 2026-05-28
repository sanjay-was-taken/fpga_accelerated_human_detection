import numpy as np

# Load fixed-point weights
w = np.load("../output/dense2_weights_fixed.npy").flatten()

# Load bias
b = np.load("../output/dense2_biases_fixed.npy")

# Generate Verilog parameters
for i, val in enumerate(w):
    print(f"parameter w{i+1} = {val};")

print(f"parameter b = {b[0]};")