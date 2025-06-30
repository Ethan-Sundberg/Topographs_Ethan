import numpy as np
from pathlib import Path

# === CONFIG: folder to scan ===
folder = Path("./log_dir/")  # Change to any folder, like Path("data/")

# === Loop over all .npy files ===
npy_files = sorted(folder.glob("*.npy"))

if not npy_files:
    print("No .npy files found in", folder.resolve())
else:
    for f in npy_files:
        try:
            data = np.load(f)
            print(f"\n📁 File: {f.name}")
            print(f"   Shape: {data.shape}")
            print(f"   Dtype: {data.dtype}")
            print(f"   First few values:\n{data.flatten()[:5]}")
        except Exception as e:
            print(f"⚠️  Could not load {f.name}: {e}")

