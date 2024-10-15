# Docker File for Test Server Setup
# from python:3.9.18-slim
from python:alpine3.19

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /intranet

# Set the working directory to intranet
workdir /intranet

# Copy the Linux ODBC Driver to the container
copy Linux_ODBC/msodbcsql17_17.10.5.1-1_amd64.apk msodbcsql17_17.10.5.1-1_amd64.apk
copy Linux_ODBC/mssql-tools_17.10.1.1-1_amd64.apk mssql-tools_17.10.1.1-1_amd64.apk

# Run the ODBC Driver
RUN  apk add --allow-untrusted msodbcsql17_17.10.5.1-1_amd64.apk
RUN  apk add --allow-untrusted mssql-tools_17.10.1.1-1_amd64.apk

# Download the unix odbc libs
RUN apk update \
    && apk add  gcc \
    && apk add  g++ \
    && apk add  unixodbc unixodbc-dev

# Install any needed packages specified in requirements.txt
copy requirements.txt requirements.txt
run pip3 install -r requirements.txt

# Copy the current directory contents into the container
copy . .


# Make Migration is not needed here as iam running on local
# Run the Test Server
cmd ["python3", "manage.py", "runserver", "0.0.0.0:8000"]