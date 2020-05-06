# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='${version}',  # 环境变量中取动态的版本
    description='Blog System base on Django',
    author="anonymous",
    author_email='defaulttest@sina.com',
    url='https://www.guang.com',
    license='MIT',
    packages=find_packages('typeidea'),  # 指明要打入的包， 函数来帮助发现typeidea下面的所有py包
    package_dir={'': 'typeidea'},  # 指明上面的包都在那个目录下， 若是同级目录可不写
    # package_data={'': [    # 打包（非py的）数据文件，方法一
        # 'themes/*/*/*/*',  # 需要按目录层级匹配
    # ]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'django~=1.11',
        'gunicorn==19.8.1',
        'supervisor==4.0.0',
        'xadmin==0.6.1',
        'mysqlclient==1.3.12',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.3',
        'Pillow==5.2',
        'coreapi==2.3.3',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django-silk==2.0.0',
        'django-dotenv==1.4.2',
    ],

    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

)
