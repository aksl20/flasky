FROM python:3.5

ENV http_proxy http://172.21.25.4:8080
ENV no_proxy localhost,127.0.0.1

WORKDIR /app

EXPOSE 5000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python3", "/app/server/server.py runserver -h 0.0.0.0 -d"]
CMD ["/bin/bash"]
