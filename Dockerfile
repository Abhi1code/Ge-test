FROM python:3.6-stretch

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check our python environment
RUN python3 --version
RUN pip3 --version

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip --ignore-installed -r requirements1.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
