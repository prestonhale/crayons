# Crayons

## Backend
To setup the backend api, run the following commands

1. if you don't have a virtualenv setup, create one
```bash
virtualenv virtualenv -p python3.5
```

2. Install dependencies
```bash
make devsetup
```

3. Run tests
```bash
make tests
```

4. Run server
```bash
make devserver # to run local django server
make runserver # to run gunicorn server
```

5. Other helpful commands
```bash
make clean # nuke existing devsetup, will need to run make devsetup again
make coveragereport # will print out a report of test coverage, as per pytest
```
