#### Training project on [web-technologies course](https://stepic.org/course/154/) at [Stepic](https://stepic.org)

###### Starting environment

Run ```bash ./init.sh``` in cloned project to copy files, create folders, link configs and restart daemons. Script also updates django framework.

###### Reading logs
```
sudo less /var/log/gunicorn/hello.log
```
```
sudo less /var/log/gunicorn/ask.log
```

###### Checking server
```
wget localhost
```
```
wget "localhost:8080/?a=1&b=2&c=3"
cat "index.html?a=1&b=2&c=3"
```
```
wget localhost:8000/ask//popular/
```
_(one or more tests are wrong at 2.1.11 step)_
