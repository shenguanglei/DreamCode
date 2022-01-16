
 # git学习
>>>>>>> 

## git和代码托管中心
代码托管中心的任务是：维护远程库
局域网环境下
  1、 Gitlab 服务器
外网环境
  1、github
  2、 码云

## Git命令行操作本地库初始化
​	创建一个文件夹mkdir  文件名称，
​	初始化目录 git init，
​	查看隐藏文件 ll ls-la
​	~ 家目录
​	less



## 设置签名
​	用户名
​	Email 地址
​	作用：区分不同的开发人员身份
​	辨析：这里设置的签名和登录远程库（代码托管中心）的账号、密码没有任何关系
​	命令：
​	项目级别/仓库级别：仅在当前本地库范围有效
​	git config user.name tom_pro
​	git config user.email goodMorming_pro@atguigu.com
​	信息保存目录
​	cat .git/config
​	系统用户级别：登录当前操作系统的用户范围
​	git config --global user.name tom_glb
​	git config --global user.email goodMorming_pro@atguigu.com
​	cat ~/.gitconfig
​	级别优先级
​	就近原则：项目级别优先于系统用户级别，二者都有时采用项目级别的签名
​	如果只有系统用户级别的签名就以系统用户级别的签名为准
​	二者都没有不允许



命令操作
git status

历史记录：
多屏显示控制方式
空格向下翻页
b向上翻页
q退出
git log --pretty=oneline

git log --oneline

git reflog

移动到当前需要移动的步数 HEAD@{1}:
前进后退
本质
HEAD

基于索引值操作（推荐）
git reset --hard 0ce5244
使用^符号 只能后退
git reset --hard HEAD^^ 一个符号一步 N个表示后退N 步
使用~符号 只能后退
      git reset --hard HEAD~ 5
reset 命令的三个参数对比
仅仅在本地库移动HEAD指针
mixed 参数
在本地库移动HEAD指针
重置暂存区
hard参数
     在本地库移动HEAD指针
     重置工作区
删除文件找回
前提：删除前，文件存在是的状态提交到了本地库
操作：git reset --hard[指针位置]
删除操作已经提交到本地库：指针回执指向历史记录
删除操作尚未提交到本地库：指针位置使用HEAD
## 文件比较
​	git diff  【文件名】
​	将工作区中的文件和暂存区进行比较
​	git diff  【本地库中历史版本】  【文件名】
​	将工作区中的文件和本地库历史记录比较
​	不带文件名比较多个文件
## 分支操作
​	master
​	feature_blue
​	feature_game
​	hot_fix（bug 分支）
​	分支的好处
​	同时并行推进多个功能开发

### 查看分支
   git branch -v 获取当前分支

###  创建分支
git branch hot_fix  创建新的分支

### 切换分支
git checkout hot_fix 切换到新的分支

### 合并分支
​	第一步：切换到接收修改的分支（被合并，增加新内容）上
​	git checkout[分支名]
​	第二步：
​	执行merge命令
​	git merge [被合并分支名]
​	冲突解决
​	第一步：编辑文件，删除特殊符号
​	第二步：把文件修改到满意的程度，保存退出
​	第三步：git add [文件名]
​	第四步： git commit -m "日志信息"
​	注意：此时commit一定不能带具体文件名
​	git 基本原理
​	hash

## 连接远程库

###  推送
git remote -v
git remote add origin 地址
git push origin master

###   克隆
git clone origin[远程地址]

###   效果
完整的把远程库下载到本地
创建origin远程地址别名
初始化本地库
setting 中添加团队成员
Add a collaborator to DreamCode
拉取
pull=fectch+merge
git fetch [远程库地址别名】【远程分支名】
git merge [远程库地址别名/远程分支名]
git  pull 远程库地址别名 远程分支名
解决冲突
如果不是基于GitHub远程库的最新版所做的修改，不能推送，必须先拉取
拉取下来后如果进入冲突状态，则按照“分支冲突解决”操作即可。





































