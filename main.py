from pathlib import Path
from PIL import Image

def get_target_format() -> str:
    """Prompts the user to pick jpg or png."""
    while True:
        choice = input("Enter target format (png / jpg): ").strip().lower()
        if choice in ("png", "jpg", "jpeg"):
            return "png" if choice == "png" else "jpeg"
        print("Invalid choice. Please type 'png' or 'jpg'.")

def convert_images(input_folder: str = "input_images", output_folder: str = "converted"):
    in_dir = Path(input_folder)
    out_dir = Path(output_folder)

    # 1. Ensure directories exist
    in_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 2. Find all .jpe files (case-insensitive)
    jpe_files = [
        f for f in in_dir.iterdir() 
        if f.is_file() and f.suffix.lower() == ".jpe"
    ]

    if not jpe_files:
        print(f"\n[!] No '.jpe' files found in: {in_dir.resolve()}")
        print("    Drop your .jpe files into that folder and run this script again.")
        return

    print(f"\nFound {len(jpe_files)} '.jpe' image(s).")
    target_format = get_target_format()
    target_ext = "jpg" if target_format == "jpeg" else "png"

    # 3. Process each image
    success_count = 0
    print(f"\nConverting to .{target_ext.upper()}...")

    for file_path in jpe_files:
        destination = out_dir / f"{file_path.stem}.{target_ext}"
        try:
            with Image.open(file_path) as img:
                # JPG does not support alpha (transparency) or CMYK without adjustments
                if target_format == "jpeg":
                    if img.mode in ("RGBA", "LA", "P"):
                        img = img.convert("RGB")
                    elif img.mode == "CMYK":
                        img = img.convert("RGB")

                img.save(destination, format=target_format.upper())
                print(f"  [✓] {file_path.name} -> {destination.name}")
                success_count += 1
        except Exception as err:
            print(f"  [✗] Error converting {file_path.name}: {err}")

    print(f"\nFinished! Converted {success_count}/{len(jpe_files)} images.")
    print(f"Saved to: {out_dir.resolve()}\n")

if __name__ == "__main__":
    convert_images()