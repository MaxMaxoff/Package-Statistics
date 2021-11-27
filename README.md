# DutyAdmins #

- CreatedBy: [MaxMaxoff](https://github.com/MaxMaxoff)

**Package_Statistics** command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. Command lite tool parse the file and output the statistics of the top 10 packages that have the most files associated with them.

## Requirements ##

- contextlib        (build-in)
- json              (build-in)
- gzip              (build-in)
- os                (build-in)
- sys               (build-in)
- urllib            (build-in)
- logging           (build-in)

## Description ##

Downloads the compressed Contents file, parse the file and output the statistics of the top 10 packages that have the most files associated with them.

### Installation ###

Clone git repo:

```bash
git clone ...Package_Statistics
```

Change work dir:

```bash
cd Package_Statistics
```

Change permissions, add execute bit:

```bash
chmod +x Package_Statistics/package_statistics.py
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install required packages:

```bash
pip install ...
```

### Usage ###

Run without arguments, will work with all architecture

```bash
Package_Statistics/package_statistics.py
```

or with arguments

```bash
Package_Statistics/package_statistics.py amd64
```

```bash
Package_Statistics/package_statistics.py amd64 arm64 i386
```
