from setuptools import setup, find_packages


setup(
    name="typeidea",
    version="0.1.1",
    description="Blog System base on Django",
    author="anonymous",
    author_email='defaulttest@sina.com',
    url="https://www.typeidea.com",
    license="MIT",
    packages=find_packages('typeidea'),  # 指明要打入的包
    package_dir={"": "typeidea"},  # 指明上面找到的包都在那个目录下， 如果在setup.py同级目录则可不写
    # package_data 指明除.py文件之外， 还需要打包那些文件到最终的安装包里。对应的值需要是字典格式。
    # key 目录， value 是list， 支持通配符， 标识要查找的具体文件。如果key为空，表示所有包。
    package_data={"": [  # 方法一： 打包数据文件
        'themes/*/*/*/*',  # 需要按照目录层级匹配
    ]},
    # include_package_date=True  # 方法二(更常用)： 配合 MANIFEST.in 文件  # 同package_data， 不同在于需要依赖MANIFEST.in
    install_requires=[  # 指明依赖版本，安装当前项目时，先去安装依赖包。
        'autopep8==1.5.1',
        'backcall==0.1.0',
        'bcrypt==3.1.7',
        'certifi==2020.4.5.1',
        'cffi==1.14.0',
        'chardet==3.0.4',
        'coreapi==2.3.3',
        'coreschema==0.0.4',
        'cryptography==2.9',
        'decorator==4.4.2',
        'defusedxml==0.6.0',
        'diff-match-patch==20181111',
        'Django==1.11.29',
        'django-autocomplete-light==3.5.1',
        'django-ckeditor==5.9.0',
        'django-crispy-forms==1.9.0',
        'django-debug-toolbar==1.11',
        'django-debug-toolbar-line-profiler==0.6.1',
        'django-dotenv==1.4.2',
        'django-formtools==2.2',
        'django-import-export==2.0.2',
        'django-js-asset==1.2.2',
        'django-redis==4.11.0',
        'django-rest-framework==0.1.0',
        'django-reversion==3.0.7',
        'django-silk==3.0.4',
        'djangorestframework==3.11.0',
        'djdt-flamegraph==0.2.13',
        'et-xmlfile==1.0.1',
        'Fabric3==1.14.post1',
        'future==0.18.2',
        'gprof2dot==2019.11.30',
        'gunicorn==20.0.4',
        'hiredis==0.3.1',
        'httplib2==0.9.2',
        'idna==2.9',
        'itypes==1.1.0',
        'jdcal==1.4.1',
        'jedi==0.16.0',
        'Jinja2==2.11.1',
        'line-profiler==3.0.2',
        'MarkupPy==1.14',
        'MarkupSafe==1.1.1',
        'meld3==2.0.1',
        'mistune==0.8.4',
        'mysqlclient==1.4.6',
        'odfpy==1.4.1',
        'openpyxl==3.0.3',
        'paramiko==2.7.1',
        'parso==0.7.0',
        'pexpect==4.8.0',
        'pickleshare==0.7.5',
        'Pillow==5.4.1',
        'prompt-toolkit==3.0.5',
        'ptyprocess==0.6.0',
        'pycodestyle==2.5.0',
        'pycparser==2.20',
        'Pygments==2.6.1',
        'Pympler==0.8',
        'PyNaCl==1.3.0',
        'python-dateutil==2.8.1',
        'pytz==2019.3',
        'PyYAML==5.3.1',
        'redis==3.4.1',
        'requests==2.23.0',
        'six==1.14.0',
        'sqlparse==0.3.1',
        'supervisor==4.0.0.dev0',
        'tablib==1.1.0',
        'traitlets==4.3.3',
        'uritemplate==3.0.1',
        'urllib3==1.25.8',
        'wcwidth==0.1.9',
        'xadmin==0.6.1',
        'xlrd==1.2.0',
        'xlwt==1.3.0',
    ],
    extras_require={  # 额外依赖。
        'ipython': ['ipython~=6.2']
    },
    scripts=[  # 指明要放到bin目录下的可执行文件
        'typeidea/manage.py',  # 配置之后安装后可以通过manage.py runserver 启动项目
    ],
    entry_points={  # 入口
        'console_scripts': [
            'typeidea_manage = manage:main',  # 生成可执行文件到bin目录下。这里会生成`typeidea_manage`命令，等价于manage.py中的main方法
        ]
    },
    classifiers=[  # 用来说明当前项目的状况(Alpha or Beta阶段， 面向人群， 依赖python版本) # Optional
        # 软件成熟度如何？
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 指明项目的受众
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Libraries",

        # 选择项目的许可证(License)
        'License :: OST Approved :: MIT License',

        # 指定项目需要使用的Python版本
        "Programming Language :: Python :: 3.7"
    ],
)
