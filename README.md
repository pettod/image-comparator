# Image Comparator (imco)

Compare image similarity with metrics printed automatically below every image. See example image below.

![comparison_image](https://user-images.githubusercontent.com/33998401/120776358-d522e980-c52c-11eb-9f12-70332ea9f42f.png)

## Installation

```bash
pip install imco
```

To get the latest version, install:

```bash
pip install git+https://github.com/pettod/imco.git@main
```

## Usage

Import following function:

```python
from imco import compareImages
```

Here is a sample code to use the comparison function:

```python
import cv2

# Paths to images
image_paths = [
    "path/to/image_1.png",
    "path/to/image_2.png",
    "path/to/image_3.png",
]

# Read images
images = [cv2.imread(image_path) for image_path in image_paths]

# Define image names
names = ["Input", "Prediction 1", "Ground Truth"]

# Create comparison image
comparison_image = compareImages(images, names, True, 256, (10, 30))
cv2.imwrite("comparison_image.png", comparison_image)
```

## License

[License](LICENSE)
