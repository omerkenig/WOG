FROM python:alpine

# Set the working directory to /app
WORKDIR $World_Of_Games_Home/
ENV World_Of_Games_Home /usr/games/World_Of_Games
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0

LABEL version="1.1"
LABEL maintainer="OmerKenig@gmail.com"

# Copy the current directory contents into the container as /app
COPY requirements.txt ./
COPY . . /
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD /Scores.txt /home/omerk/World_Of_Games/Docker/Scores.txt
Add /MainScores.py /home/omerk/World_Of_Games/Docker/MainScores.py
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD ["python", "MainScores.py"]
