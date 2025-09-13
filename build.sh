#!/bin/bash

# 在GitHub Actions中，如果需要使用Go模块，首先初始化
if [ ! -f "go.sum" ]; then
    echo "初始化Hugo模块..."
    go mod tidy
fi

# 清理并构建
if [ -d "public" ]; then
    rm -rf public
fi

echo "构建Hugo网站..."
hugo --minify