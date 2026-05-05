import os
import sys

def extract_ogg(input_file, output_dir):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    magic_number = b'\x4F\x67\x67\x53\x00\x02\x00\x00'

    offsets = [offset for offset in range(len(data)) if data[offset:offset+8] == magic_number]
    
    for i, offset in enumerate(offsets):
        start_offset = offset
        end_offset = offsets[i + 1] if i + 1 < len(offsets) else len(data)
        audio_data = data[start_offset:end_offset]
        
        output_file = os.path.join(output_dir, f'audio_{i+1}.ogg')
        with open(output_file, 'wb') as audio_file:
            audio_file.write(audio_data)
        print(f'Audio {i+1} extracted and saved as {output_file}')

input_file = sys.argv[1]
output_dir = 'output_audio/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_ogg(input_file, output_dir)