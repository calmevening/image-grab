import os
import sys

def extract_bmp(input_file, output_dir):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    magic_numbers = [
        b'\x42\x4D\xDE\x1D\x02\x00\x00\x00\x00\x00\x36',
        b'\x42\x4D\x1E\xFD\x04\x00\x00\x00\x00\x00\x36',
        b'\x42\x4D\xB6\x42\x00\x00\x00\x00\x00\x00\x36',
        b'\x42\x4D\x86\xDB\x05\x00\x00\x00\x00\x00\x36'
    ]
    offsets = []
    for offset in range(len(data)):
        for magic in magic_numbers:
            if data[offset:offset + len(magic)] == magic:
                offsets.append(offset)
                break

    offsets = sorted(set(offsets))
    for i, offset in enumerate(offsets):
        start_offset = offset
        end_offset = offsets[i + 1] if i + 1 < len(offsets) else len(data)
        image_data = data[start_offset:end_offset]

        output_file = os.path.join(output_dir, f'image_{i+1}.bmp')
        with open(output_file, 'wb') as img_file:
            img_file.write(image_data)
        print(f'Image {i+1} saved as {output_file}')


input_file = sys.argv[1]
output_dir = 'output_images/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_bmp(input_file, output_dir)