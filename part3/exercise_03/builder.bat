git clone https://github.com/psJnttl/%1
cd %1
docker build . -t tempname
docker login
docker tag tempname %2
docker push %2
pause