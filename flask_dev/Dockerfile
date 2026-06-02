# Python Image
FROM python:3.12
ENV TZ UTC
ENV LANG zh_TW.UTF-8
ENV LANGUAGE zh_TW:zh
ENV LC_ALL zh_TW.UTF-8

WORKDIR /app

# Copy files
COPY app.py /app/
COPY weather.py /app/
COPY requirements.txt /app/
# COPY .env /app/
# COPY ssl.conf /app/
RUN mkdir /app/static
# RUN apt-get update && apt-get install -y apt-get install ffmpeg libsm6 libxext6
# RUN apt-get install libgl1


# Install package
RUN pip install --no-cache-dir -r requirements.txt

# CA certificate

# Expose flask port
EXPOSE 4000

CMD ["python", "app.py"]