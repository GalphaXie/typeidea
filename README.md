# typeidea
实现一遍胡杨老师&lt;&lt;django企业开发实战&gt;&gt;一书的博客项目
- 1.尽可能的去符合更多优秀的开发实践规范
- 2.尽可能的保留迭代的过程;


### 1.commit 文档提交规范
参考: https://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html
```shell script
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```
#### type 标识符
>- feat：新功能（feature）
>- fix：修补bug
>- docs：文档（documentation）
>- style： 格式（不影响代码运行的变动）
>- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
>- test：增加测试
>- chore：构建过程或辅助工具的变动


#### 虚拟环境的构建

#### 1.目录或文件的说明:
- CHANGELOG.md 记录项目每次发布版本等变更; 也可以使用 git 来生成; 可以参考Django源码中  django/docs/release/
- LICENSE 开源项目版权声明(开源项目许可证)
- README.md 介绍项目信息: 项目目的, 开发背景, 项目结构和 依赖技术 等
- requirements.txt python三方库
    - 1.可以在文件首行配置 镜像源, 如配置豆瓣的 `-i http://pypi.doubanio.com/simple`, 你可以配置自己的源
    - 2.最后一行配置 `-e .`, 它表示从当前的 `setup.py` 中查找其他的依赖项.


#### 常用的执行命令收集, 后面做一个自动化部署的文档
`mkdir settings && touch settings/__init__.py && mv settings.py settings/base.py && touch settings/develop.py`

```shell script
# 提交到远端仓库
git remote add origin <远端仓库地址>
git push -u origin master

# 切换到主分支, 合并开发分之的代码;
git checkout master
git merge xxx
```


### 待解惑的问题:
1.setup.py 正式环境打包的运用
2.安装包的时候 ~= 的作用

3.开源项目 mkdocs 部署内网在线的文档系统

4.打包和自动化部署相关的配置

5.注释 `# NOQA` 的作用是, 让 PEP8 规范检测工具跳过 该注释所在行的 代码检测; 甚至我们可以在 文件的首行 加上 `flake8: NOQA` 来跳过整个文件的规范检测
 
6.替换:
```python
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
profile = os.environ.get("TYPEIDEA_PROFILE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)
```

7.关于忽略文件参考 github 上开源项目: `gitigonre` 里面有各种语言需要忽略的文件后缀

8.断点: `import pdb; pdb.set_trace()` 代码;

9.大型项目设计中, 需要借助一些辅助工具: UML, E-R图, 思维导图 等来帮助我们可视化地分析项目结构

10.老师是把  help_text  当作补充提示来使用的, 不是当作 verbose_name 相同内容的方式来使用的.

11.关于评论模块的理解:
> 作者采用了独立成模块的方式. 如果和文章紧耦合, 那么后期想要扩展的时候, 评论只能针对文章. 也许, 我们可能在不同的页面, 针对非文章的数据进行评论. 这个时候就没法用这个功能了. 确实不错的思路.

12.作者在 `INSTALL_APP` 中配置采用了 覆盖的方式, 这是一个很好的思路. 不过这是一个取舍, 有发生 依赖错误的风险.

13.删除指定文件: find . -name '*.exe' -type f -print -exec rm -rf {} \;  

14.要使用 sqlite 数据库, 同样要使用 `sudo apt-get install sqlite3 libsqlite3-dev` 安装相应的数据库环境

15.数据库迁移产生的 migrations 文件夹下的文件, 要及时提交到代码仓库中, 保证协作的时候, 不容易发生代码冲突.

16.参考资料:
```html
Django Model Meta: https://docs.djangoproject.com/en/1.11/ref/models/options/


```