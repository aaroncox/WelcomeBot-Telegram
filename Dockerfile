FROM python:3.8.3-slim-buster
ADD . /script
WORKDIR "/script"
RUN pip3 install -r requirements.txt
CMD [ "python", "/script/tgbot.py" ]
