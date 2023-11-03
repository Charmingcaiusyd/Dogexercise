#!/bin/bash

# 切换到 Django 项目目录
cd /home/ubuntu/Group-15/main

# 获取 EC2 实例的 IP 地址和主机名
PUBLIC_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
PUBLIC_HOSTNAME=$(curl http://169.254.169.254/latest/meta-data/public-hostname)

# 设置 ALLOWED_HOSTS 环境变量
export ALLOWED_HOSTS="localhost,127.0.0.1,[::1],$PUBLIC_IP,$PUBLIC_HOSTNAME"

# 启动 MySQL
sudo systemctl start mysql

# 重启 Nginx
sudo systemctl restart nginx

# 修改 Django 项目的 settings.py 文件
sed -i "s/ALLOWED_HOSTS = \[.*\]/ALLOWED_HOSTS = \['localhost', '127.0.0.1', '[::1]', '$PUBLIC_IP', '$PUBLIC_HOSTNAME'\]/" mysite/settings.py

# 启动 Django 项目
python3 manage.py runserver 0.0.0.0:8000

