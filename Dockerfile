FROM python:3

WORKDIR /app

COPY requeriments.txt /app/
RUN python -m pip install -r requeriments.txt

COPY fibbo.py /app/

ENTRYPOINT ["python", "fibbo.py"]

CMD ["8"]