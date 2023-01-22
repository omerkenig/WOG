FROM python:alpine
# Set the working directory to /app
WORKDIR /home/omerk/World_Of_Games/Docker
# Copy the current directory contents into the container as /app
COPY . /home/omerk/World_Of_Games/Docker
# Adding the Score.txt file
ADD /Scores.txt /home/omerk/World_Of_Games/Docker/Scores.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD python MainScores.py
