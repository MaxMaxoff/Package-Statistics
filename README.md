# Package_Statistics #

Canonical interview.

>Hello Maxim,
>
>Debian uses *deb packages to deploy and upgrade software. The packages
are stored in repositories and each repository contains the so called "Contents
index". The format of that file is well described here
<https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices>
>
>Your task is to develop a python command line tool that takes the
architecture (amd64, arm64, mips etc.) as an argument and downloads the
compressed Contents file associated with it from a Debian mirror. The
program should parse the file and output the statistics of the top 10
packages that have the most files associated with them.
An example output could be:
>
>./package_statistics.py amd64
>
>1. <package name 1>         <number of files>
>2. <package name 2>         <number of files>
>
>......
>
>10. <package name 10>         <number of files>
>
>You can use the following Debian mirror
<http://ftp.uk.debian.org/debian/dists/stable/main/>. Please do try to
follow Python's best practices in your solution. Hint: there are tools
that can help you verify your code is compliant. In-line comments are
appreciated.
>
>It will be good if the code is accompanied by a 1-page report of the
work that you have done including the time you actually spent working on it.
>
>Please return your work in approximately 24 hours.
>
>Note1: The focus is not to write the perfect Python code, but to see how
you'll approach the problem and how you organize your work.
>
>Note2: Please do not upload your results to a public website such as GitHub or GitLab.

## Main ##

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
