FROM python:3.9

RUN pip install requests
COPY notify.py .
COPY global-entry.json .

CMD [ "python", "-u", "notify.py" ]
