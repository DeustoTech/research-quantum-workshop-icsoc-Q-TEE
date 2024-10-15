FROM python:3.12.5

EXPOSE 5000/tcp

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD ["python", "main.py" ]