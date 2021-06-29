FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8000 3000
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requiremnts.txt
RUN pip install -r DjangoApp/DjangoAPI/requirements.txt
RUN python -m pip install django-cors-headers
COPY . /app
