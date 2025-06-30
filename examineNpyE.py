import numpy as np
from pathlib import Path

def print_first_three_arrays(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    data = np.load(file_path)
    print(f"Loaded file: {file_path.name}")
    print(f"Shape: {data.shape}\n")

    # Print first three arrays (2x3 each)
    for i in range(min(3, data.shape[0])):
        print(f"Array {i} (shape {data[i].shape}):")
        print(data[i])
        print()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python print_first_three_arrays.py path/to/file.npy")
    else:
        print_first_three_arrays(sys.argv[1])

