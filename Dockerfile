FROM python:3.9-slim

COPY botdodia.py taboas.py requirements.txt resposta.txt /

RUN pip install -r requirements.txt

CMD ["python", "./botdodia.py"]