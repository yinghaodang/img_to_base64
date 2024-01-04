FROM python:3.10-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY app.py .

EXPOSE 33333

ENTRYPOINT ["python"]  

CMD ["app.py"]