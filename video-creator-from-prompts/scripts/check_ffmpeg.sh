#!/bin/bash

echo '正在检查ffmpeg安装状态...'

if command -v ffmpeg &> /dev/null
then
    echo 'ffmpeg已安装'
    ffmpeg -version | head -n 1
    exit 0
else
    echo 'ffmpeg未安装，请先安装ffmpeg'
    echo ''
    echo '安装方法：'
    echo '  Ubuntu/Debian: sudo apt-get install ffmpeg'
    echo '  macOS: brew install ffmpeg'
    echo '  Windows: 从 https://ffmpeg.org/download.html 下载'
    exit 1
fi