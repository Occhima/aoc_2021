FROM python:latest
RUN pip install click

WORKDIR /aoc
COPY . /aoc

CMD ["python3", "main.py"]
