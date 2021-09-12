FROM python:3.9

RUN pip install requests
COPY notifier.py .
COPY global-entry.json .

CMD [ "python", "-u", "notify.py" ]
