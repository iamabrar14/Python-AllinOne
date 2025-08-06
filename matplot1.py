import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 image with random grayscale values
image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

plt.imshow(image, cmap='gray')
plt.title("Random Grayscale Image")
plt.show()
