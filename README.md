# JPE to Image Converter

Quick batch tool to convert `.jpe` images to `.png` or `.jpg`.

## Setup

Before running the script, you need to install a free add-on called **Pillow**:

```bash
pip install Pillow
```

> **Why is this needed?**  
> Basic Python does not know how to open, read, or convert picture files on its own. **Pillow** is a trusted image-processing library that gives Python the "eyes" and tools to load `.jpe` files, adjust their colors, and save them out as fresh `.png` or `.jpg` images. You only need to run this command once.

## How to Use

1. Drop your `.jpe` files into the `input_images/` folder.
2. Open terminal in the project root:
   ```bash
   python main.py
   ```
3. Type `png` or `jpg` when prompted and hit Enter.

Converted images will appear in the `converted/` folder.
