from setuptools import setup, find_packages


setup(
    name="typeidea",
    version="0.0.1",
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
        'django~=1.11',
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
