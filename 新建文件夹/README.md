### pycharm 与 GitHub 结合使用
1. download: https://git-scm.com/download/win
2. 配置pycharm：File>Settings>Version Control>Github，填写GitHub的用户名密码
    File>Settings>Version Control>Git，填写正确第一步安装的git.exe的Path 路径
3. VCS>Import into Version Control>Share project on Github
4. 第三步骤需要在git中认证邮箱、用户名：进入工程目录，右键Git Bash Here，输入以下两个命令：
    git config --global user.email "XX@XX.com"
    git config --global user.name "XX"

# 20170418
[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
## git bash
问题：fatal: Not a git repository
解决方案：git init
## Git常用命令查找
![Git 常用命令查找](http://images2015.cnblogs.com/blog/602207/201606/602207-20160618090147620-1421667287.jpg)
```
git init  # 初始化
git clone <url>  # 复制远程仓库
git pull  # 更新到本地
git add .  # 添加
git commit -m "comments"  # 提交
git push  # 更新到远程
```

### 业务流程
