#!/usr/bin/env python3
"""
Generate dummy assets untuk Ren'Py game
Jalankan dari root directory game
"""

import os
import struct
from pathlib import Path

def create_dummy_image(filepath, width=1280, height=720):
    """Create minimal valid PNG (1x1 pixel, extend to desired size)"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Minimal PNG: 1x1 transparent pixel
    png_data = bytes([
        0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG signature
        0x00, 0x00, 0x00, 0x0D,  # IHDR chunk size
        0x49, 0x48, 0x44, 0x52,  # IHDR
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,  # 1x1
        0x08, 0x06, 0x00, 0x00, 0x00,  # bit depth, color type
        0x1F, 0x15, 0xC4, 0x89,  # CRC
        0x00, 0x00, 0x00, 0x0A,  # IDAT chunk size
        0x49, 0x44, 0x41, 0x54,  # IDAT
        0x78, 0x9C, 0x62, 0x00, 0x00, 0x00, 0x02, 0x00, 0x01,
        0xE5, 0x27, 0xDE, 0xFC,  # CRC
        0x00, 0x00, 0x00, 0x00,  # IEND chunk size
        0x49, 0x45, 0x4E, 0x44,  # IEND
        0xAE, 0x42, 0x60, 0x82,  # CRC
    ])
    
    with open(filepath, 'wb') as f:
        f.write(png_data)
    print(f"✓ Created: {filepath}")

def create_dummy_audio(filepath):
    """Create minimal valid WAV file (silent, 1 second)"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Minimal WAV: mono, 16-bit, 16kHz, 1 second silence
    sample_rate = 16000
    duration = 1  # second
    num_samples = sample_rate * duration
    
    wav_data = bytearray()
    wav_data += b'RIFF'
    wav_data += struct.pack('<I', 36 + num_samples * 2)
    wav_data += b'WAVE'
    wav_data += b'fmt '
    wav_data += struct.pack('<I', 16)  # subchunk1 size
    wav_data += struct.pack('<HHIIHH', 1, 1, sample_rate, sample_rate * 2, 2, 16)
    wav_data += b'data'
    wav_data += struct.pack('<I', num_samples * 2)
    wav_data += b'\x00' * (num_samples * 2)  # silence
    
    with open(filepath, 'wb') as f:
        f.write(wav_data)
    print(f"✓ Created: {filepath}")

def scan_and_create_dummies():
    """Scan game folder untuk reference images/audio, buat dummy-nya"""
    game_dir = Path('game')
    
    if not game_dir.exists():
        print("ERROR: 'game' folder tidak ditemukan!")
        return
    
    # Scan .rpy files untuk cari asset references
    image_refs = set()
    audio_refs = set()
    
    for rpy_file in game_dir.rglob('*.rpy'):
        try:
            content = rpy_file.read_text(encoding='utf-8', errors='ignore')
            
            # Simple regex untuk detect image/audio references
            import re
            
            # Image: image xxx = "path/to/file.png"
            img_matches = re.findall(r'image\s+\w+\s*=\s*["\']([^"\']+)["\']', content)
            image_refs.update(img_matches)
            
            # Audio: play sound "path/to/file.ogg"
            audio_matches = re.findall(r'(?:play\s+sound|music|bgm)\s*["\']([^"\']+)["\']', content)
            audio_refs.update(audio_matches)
            
        except Exception as e:
            print(f"Warning: {rpy_file} - {e}")
    
    # Create dummy images
    print("\n=== Creating Dummy Images ===")
    for img_ref in sorted(image_refs):
        img_path = game_dir / img_ref
        if not img_path.exists():
            create_dummy_image(str(img_path))
    
    if not image_refs:
        print("No image references found in .rpy files")
    
    # Create dummy audio
    print("\n=== Creating Dummy Audio ===")
    for audio_ref in sorted(audio_refs):
        audio_path = game_dir / audio_ref
        if not audio_path.exists():
            create_dummy_audio(str(audio_path))
    
    if not audio_refs:
        print("No audio references found in .rpy files")
    
    print("\n✅ Dummy assets generation complete!")

if __name__ == '__main__':
    scan_and_create_dummies()