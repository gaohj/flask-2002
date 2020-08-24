# Git

 

##  绑定远程仓库

```
git remote add origin https://github.com/gaohj/flask-2002.git # 你的远程仓库地址  
```



## 提交之前 从远程仓库拉取文件  

```
git pull origin master --allow-unrelated-histories  
```



## commit 之前 进行相关的配置  明确谁提交的   

```
配置用户名 : git config  user.name "lisi"    (区分责任人)
配置邮箱 : git config user.email "ls@126.com" (方便联系作者)
```



## 流程 

```
1·所有的代码都是在工作区写 git init  
2.git add . # .表示所有文件  将工作区所有的文件写入到 暂存区 
3. git commit -a -m '此次提交备注的信息' #-a 上次提交之后变化的部分   -m 备注信息   
4.git pull origin master --allow-unrelated-histories  
5.git push origin master 
```



## 冲突  

```
任何代码不要在远程仓库修改  
所有的代码 都在工作区写 写完以后 提交到暂存区 再到本地仓库 再到 远程仓库  
拉取到本地 在本地手动修改 
手动修改完成以后再提交
放平心态 
别删库 别删代码  

养成良好的代码习惯,先pull在修改,修改完立即commit和push
一定要确保自己正在修改的文件是最新版本的
分模块开发,各自开发各自的模块
如果要修改公共文件,一定要先确认有没有人正在修改
下班前一定要提交代码,上班第一件事拉取最新代码
一定不要擅自修改同事的代码

```



## 分支  

> a分支 下 新建文件    如果位于暂存区 和 本地仓库  那么其它分支是可以看到你的代码的   
>
>  如果代码提交到了 本地仓库  那么其它分支就看不到 了   



### 合并分支  

> develop 分支 写了代码   但是提交到本地仓库 master 分支看不到    
>
> 如果让master分支 看到 代码  必须通过合并分支  

```
1.切换到master 分支  # 这里边没有develop分支的代码   
2.git merge develop 

```



### 使用ssh提交 到远程仓库 

```
ssh-keygen -t rsa -b 4096 -C 你的邮箱     #生成密钥对  
$ ssh-keygen -t rsa -b 4096 -C dandan@163.com  #回车 
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/neyo/.ssh/id_rsa):#为了不覆盖 我们新写一个或者回车
/c/Users/neyo/.ssh/id_rsa already exists.
Overwrite (y/n)? y   #
Enter passphrase (empty for no passphrase): #回车
Enter same passphrase again: #回车
Your identification has been saved in /c/Users/neyo/.ssh/id_rsa
Your public key has been saved in /c/Users/neyo/.ssh/id_rsa.pub  #这里显示保存的位置   
The key fingerprint is:
SHA256:xAbSfJsEt5xUaARs8TfsMni1Rbto87xm8YBSbO1PYBw dandan@163.com
The key's randomart image is:
+---[RSA 4096]----+
|    .+==+o. .    |
|     .=B=+ .E.   |
|     . +O+=oo.   |
|       +o++==.   |
|      . So*+..   |
|       ..+.++ .  |
|         .  o*   |
|            o.o  |
|           o.    |
+----[SHA256]-----+


cd   /c/Users/neyo/.ssh  #切换到 密钥对保存的位置  

cat id_rsa.pub 
复制公钥内容 

https://github.com/settings/keys 全局设置 
你的项目地址/settings/keys #你的项目自己的设置  
两个地址都可以   

ssh -T git@github.com  


git push origin  master #查看是否成功  每次提交不需要输入远程仓库的用户名和密码 
```

