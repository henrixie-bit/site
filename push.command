#!/bin/bash
cd ~/Downloads/henri-site
git add .
git commit -m "更新网站"
git push
echo "✅ 推送成功！等待1~2分钟后刷新网站即可。"
read -p "按回车键关闭..."
