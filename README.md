Docker Siecle
=============

Docker Siecle is job scheduler using Crontab syntax. It can execute jobs inside containers.

# Quickstart

## Demo

```
docker run -v /var/run/docker.sock:/var/run/docker.sock --name siecle superbounou/siecle
```

## Setup the crontab

The syntax is exactly the same as a classical crontab. The only difference is the add of the container name.

```
# m h  dom mon dow   container        command

* * * * *            siecle           /bin/sh -c "echo 'hi there' && sleep 42"
```

Or use `docker-compose.yml`.

# Notes

It's an *experimental* project. Feel free to contribute :)

# Licence

This program is under BEER-WARE LICENSE ;)
