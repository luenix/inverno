# Inverno 📈

Inverno is a flexible investments portfolio tracker.


## How does it work ?

Inverno will take as input a configuration file containing a list of transactions and generate an html report.

You can see an example report [here](https://ret2libc.com/static/inverno_report/).

![preview](https://user-images.githubusercontent.com/10875013/124403088-68b62880-dd2c-11eb-8332-7dfd50c710ba.png)


## Installation ✨

### Install from PyPI

To install from PyPI simply run:
```
$ pip install inverno
```

Once Inverno is installed you should have access to the cli:

```
$ inverno --help
```

### Build from the repository

Fetch a copy of the repository:
```
$ git clone https://github.com/werew/inverno.git
```

Make sure you have [Poetry](https://python-poetry.org/) installed in your sistem, then run:

```
$ poetry install
```

Next, enable Poetry's shell in order run the Inverno cli:

```
$ poetry shell
$ inverno --help
```
