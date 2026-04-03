FROM python:3.12 as builder
WORKDIR /app
RUN apt install libpq-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
CMD ["python", "manage.py tailwind install"]

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD [ "python", "manage.py tailwind dev" ]