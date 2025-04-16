from PIL import Image

def convert_image_to_c_array(image_path, output_path):
    img = Image.open(image_path).convert('1')  # Convert to black & white
    img = img.resize((128, 32))  # Resize to 128x32 (W x H)

    pixels = img.load()

    data = []
    for y_block in range(0, 32, 8):
        for x in range(128):
            byte = 0
            for bit in range(8):
                y = y_block + bit
                if pixels[x, y] == 255:  # White pixel
                    byte |= (1 << bit)
            data.append(byte)

    # Write to C file
    with open(output_path, 'w') as f:
        f.write("uint8_t image_data[512] = {\n")
        for i in range(512):
            f.write(f"0x{data[i]:02X}")
            if i < 511:
                f.write(", ")
            if (i + 1) % 128 == 0:
                f.write("\n")
        f.write("};\n")

    print("Conversion terminée")

# Utilisation
convert_image_to_c_array("image.png", "image_output.c")
