import os

def extract_jpgs(input_file, output_dir):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    # Find occurrences of JPEG magic number (start of image marker)
    magic_number = b'\xFF\xD8\xFF'
    offsets = [offset for offset in range(len(data)) if data[offset:offset+3] == magic_number]
    
    # Extract individual images
    for i, offset in enumerate(offsets):
        start_offset = offset
        end_offset = offsets[i + 1] if i + 1 < len(offsets) else len(data)
        image_data = data[start_offset:end_offset]
        
        # Write the image data to a separate file
        output_file = os.path.join(output_dir, f'image_{i+1}.jpg')
        with open(output_file, 'wb') as img_file:
            img_file.write(image_data)
        print(f'Image {i+1} extracted and saved as {output_file}')

# Usage
input_file = 'a.png'
output_dir = 'output_images/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_jpgs(input_file, output_dir)