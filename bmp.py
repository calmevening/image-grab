import os
import sys

def extract_bmp(input_file, output_dir):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    magic_number = b'\x42\x4D'
    offsets = [offset for offset in range(len(data)) if data[offset:offset+2] == magic_number]
    
    for i, offset in enumerate(offsets):
        start_offset = offset
        end_offset = offsets[i + 1] if i + 1 < len(offsets) else len(data)
        image_data = data[start_offset:end_offset]
        
        output_file = os.path.join(output_dir, f'image_{i+1}.bmp')
        with open(output_file, 'wb') as img_file:
            img_file.write(image_data)
        print(f'Image {i+1} extracted and saved as {output_file}')

input_file = sys.argv[1]
output_dir = 'output_images/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_bmp(input_file, output_dir)
