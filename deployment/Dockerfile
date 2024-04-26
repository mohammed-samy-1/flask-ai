FROM ubuntu:latest AS builder
LABEL authors="medos"
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
RUN pip3 install tensorflow
RUN pip3 install transformers
RUN pip3 install torch
RUN pip3 install tf-keras
WORKDIR /app
COPY .. .

# Stage 2: Runtime environment
FROM ubuntu:latest
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
WORKDIR /app
COPY --from=builder /app .

CMD [ "python3","flask_app.py", "-m", "flask", "run", "--host=0.0.0.0"]