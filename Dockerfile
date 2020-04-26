FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

CMD [ "python", "typeidea/manage.py" ]