FROM python:alpine

ENV World_Of_Games_Home /usr/games/World_Of_Games

LABEL version="1.1"
LABEL maintainer="OmerKenig@gmail.com"
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python-pip python-dev && \
    mkdir -p $World_Of_Games

# Set the working directory to /app
WORKDIR $World_Of_Games_Home/
# Copy the current directory contents into the container as /app
COPY . /home/omerk/World_Of_Games/Docker
# Adding the Score.txt file
ADD /Scores.txt /home/omerk/World_Of_Games/Docker/Scores.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD ["python", "MainScores.py"]
