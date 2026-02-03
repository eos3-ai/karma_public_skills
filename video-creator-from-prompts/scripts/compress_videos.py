#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

def compress_video(input_path, output_path, crf=23):
    """压缩单个视频文件"""
    cmd = f"ffmpeg -i {input_path} -c:v libx264 -crf {crf} -preset medium -c:a aac {output_path}"
    print(f'正在压缩: {input_path.name}')
    os.system(cmd)
    
    original_size = input_path.stat().st_size / (1024 * 1024)
    compressed_size = output_path.stat().st_size / (1024 * 1024)
    ratio = (1 - compressed_size / original_size) * 100
    
    print(f'原始大小: {original_size:.2f}MB')
    print(f'压缩后: {compressed_size:.2f}MB')
    print(f'压缩率: {ratio:.1f}%')
    print('')

def main(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    video_files = list(input_path.glob('*.mp4'))
    print(f'找到 {len(video_files)} 个视频文件')
    print('')
    
    for video in video_files:
        output_file = output_path / f'compressed_{video.name}'
        compress_video(video, output_file)
        
    print('所有视频压缩完成')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: python compress_videos.py <输入目录> <输出目录>')
        sys.exit(1)
        
    main(sys.argv[1], sys.argv[2])