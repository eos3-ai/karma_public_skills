#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import yaml
import time
import requests
from pathlib import Path

class VideoCreator:
    def __init__(self, project_name='video_project'):
        self.project_name = project_name
        self.project_path = Path(project_name)
        self.prompts_dir = self.project_path / 'prompts'
        self.videos_dir = self.project_path / 'videos'
        self.output_dir = self.project_path / 'output'
        self.api_key = os.getenv('GEMINI_API_KEY')
        
    def init_project(self):
        """初始化项目文件夹结构"""
        self.project_path.mkdir(exist_ok=True)
        self.prompts_dir.mkdir(exist_ok=True)
        self.videos_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        print(f'项目初始化完成: {self.project_path}')
        
    def read_prompts(self, prompt_file):
        """读取提示词文件"""
        prompts = []
        file_path = Path(prompt_file)
        
        if file_path.suffix == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                prompts = [line.strip() for line in f if line.strip()]
        elif file_path.suffix in ['.yaml', '.yml']:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                prompts = data.get('videos', [])
        elif file_path.suffix == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                prompts = data.get('videos', [])
        
        print(f'读取到 {len(prompts)} 个提示词')
        return prompts
        
    def generate_video(self, prompt, index):
        """调用Gemini API生成单个视频"""
        video_name = f'{index:02d}.mp4'
        video_path = self.videos_dir / video_name
        
        if video_path.exists():
            print(f'视频 {video_name} 已存在，跳过')
            return video_path
            
        print(f'正在生成视频 {video_name}...')
        
        # 这里是Gemini API调用的示例代码
        # 实际使用时需要根据真实API接口调整
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            if isinstance(prompt, dict):
                prompt_text = prompt.get('prompt', '')
                duration = prompt.get('duration', 5)
                resolution = prompt.get('resolution', '1920x1080')
            else:
                prompt_text = prompt
                duration = 5
                resolution = '1920x1080'
                
            payload = {
                'prompt': prompt_text,
                'duration': duration,
                'resolution': resolution,
                'fps': 30
            }
            
            # 模拟API调用（实际使用时替换为真实API）
            time.sleep(2)
            print(f'视频 {video_name} 生成成功')
            return video_path
            
        except Exception as e:
            print(f'生成视频 {video_name} 失败: {e}')
            return None
            
    def merge_videos(self, output_name='final_video.mp4'):
        """使用ffmpeg合成所有视频"""
        video_files = sorted(self.videos_dir.glob('*.mp4'))
        
        if not video_files:
            print('没有找到视频文件')
            return
            
        filelist_path = self.videos_dir / 'filelist.txt'
        with open(filelist_path, 'w', encoding='utf-8') as f:
            for video in video_files:
                f.write(f"file '{video.name}'\n")
                
        output_path = self.output_dir / output_name
        cmd = f"ffmpeg -f concat -safe 0 -i {filelist_path} -c copy {output_path}"
        
        print(f'正在合成视频...')
        os.system(cmd)
        print(f'视频合成完成: {output_path}')
        return output_path
        
    def run(self, prompt_file):
        """执行完整工作流"""
        self.init_project()
        prompts = self.read_prompts(prompt_file)
        
        for i, prompt in enumerate(prompts, 1):
            self.generate_video(prompt, i)
            
        self.merge_videos()
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python generate_videos.py <提示词文件路径>')
        sys.exit(1)
        
    prompt_file = sys.argv[1]
    creator = VideoCreator()
    creator.run(prompt_file)