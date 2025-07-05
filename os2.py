import os
for i in range(1, 101):
    os.rename(f"data/day{i}", f"data/renamed{i}")
