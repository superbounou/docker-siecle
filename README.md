Docker Siecle
=============

Docker Siecle is job scheduler using Crontab syntax. It can execute jobs inside container.

# 1. HOWTO

## 1.1 Configure crontab

Crontab sample :

```
# m h  dom mon dow  container_name command
0 O * * *       mysql echo "everyfive five minute"
```

Save the crontab file as a volume. You have an example in `docker-compose.yml`.

## 1.2 Run the scheduler

```
./run.sh
```

# 2. Notes

It's an *experimantal* project. Feel free to contribute :)

# 3. Licence
