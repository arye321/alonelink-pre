FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir yt-dlp

COPY index.py index.py
COPY templates templates

EXPOSE 5000


CMD ["flask", "--app","index", "run","--host=0.0.0.0"]