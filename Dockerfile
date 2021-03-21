FROM tensorflow/tensorflow:latest-gpu-py3
# Set the Dirc for the Docker Container 
WORKDIR /home/yuan/Documents/TEST_SOM/
#VOLUME /RES
# COPY all the files in SOM
COPY /SOM .

CMD [ "python", "./som_gc.py" ]
