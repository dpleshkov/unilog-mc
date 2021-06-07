# Unilog

A super-simple script that combines all of your Minecraft 
server log files (`.log.gz` and `latest.log`) into one single `.log` file.
Tested on a Ubuntu 20.04 server. Requires Python 3.

**Installation:**

Make sure working directory is your `logs` directory.

Clone the repo:
```bash
git clone https://github.com/dpleshkov/unilog-mc
```
Copy the little script out of the directory:
```bash
cp unilog-mc/unilog.py unilog.py
```

**Usage:**

```bash
python3 unilog.py -o unilog.log  # combines all the log files into file unilog.log
```

or

```bash
python3 unilog.py  # prints unified log to STDOUT
```