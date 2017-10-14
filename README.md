# Nitro Challenge
This is `python` based project. It was tested and executed on `python 2.7`
#### Installation
Make sure `python 2.7+` is installed. Then clone this repo to your location:
```sh
cd workspace/
git clone git@github.com:schernikov/nitro.git nitro_schernikov
cd nitro_schernikov/src
```
#### Building
There is no build step for python. It builds modules as they are executed.

#### Testing
First, make sure you are in the right location:
```
$ ls
counting.py  test
```
Test are located in `./test/tester.py`. Test can be executed as this:
```sh
python -m test.tester -v
```
#### Running
This tool as a CLI interface. Here is how it works:
```
$ python -m counting -h
usage: counting.py [-h] [-x X] n k

positional arguments:
  n           number of players
  k           count out every k player

optional arguments:
  -h, --help  show this help message and exit
  -x X        starting position for counting: 1 <= x <= n (default:1)
```
Examples:
* command:`python -m counting 3 2`
   output:`3`
* command:`python -m counting 3 3`
   output:`2`
* command:`python -m counting 12 2`
   output:`9`
* command:`python -m counting 10000000 100`
   output:`2444746`
