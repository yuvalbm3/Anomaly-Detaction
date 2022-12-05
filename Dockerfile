FROM python:3.10-slim-buster
WORKDIR C:/Users/Ben/PycharmProjects/anamoally
COPY . .
RUN python3 -m pip install pandas
RUN python3 -m pip install flask

ADD app.py /

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

EXPOSE 5000