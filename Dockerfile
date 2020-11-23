# Run with: docker run -itd -p 5001:5000 --name myapp myapp:v01
FROM ubuntu:focal

RUN apt update && apt install -y python3-pip
RUN pip3 install flask pysqlite3 
RUN mkdir /app
COPY myapp.py /app/myapp.py 
RUN chmod +x /app/myapp.py 
EXPOSE 5000 
CMD ["/app/myapp.py"]