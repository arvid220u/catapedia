# saytex api


## Installation

Install:

```
./setup.sh
```

Copy config and modify if need be:

```
cp config_template.py config.py
vim config.py
```


## Running

Activate the virtualenv:

```
source venv/bin/activate
```

Run in production:

```
./run-production.sh
```

Kill in production:

```
killall gunicorn
```
