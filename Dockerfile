FROM python:3.11-rc-buster
WORKDIR /monitor
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "manage.py runserver"]