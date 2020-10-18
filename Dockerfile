FROM python:3.7-slim

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home egodaddy
WORKDIR /home/egodaddy
USER egodaddy

COPY update_dns.py .

CMD [ "python3", "./update_dns.py", "prod" ]

