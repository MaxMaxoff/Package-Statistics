#!./.venv/bin/python3

# region Import
from contextlib import closing
import json
import gzip
import os
import sys
import urllib.request

import logging as log
# region Logging
log.basicConfig(format='%(asctime)s'
                ' - %(name)s'
                ' - %(levelname)s'
                ' - %(message)s',
                level=log.WARNING)
                # level=log.INFO)
# endregion

# endregion

if sys.version_info < (3,7):
    log.error(f"Current verison {sys.version_info}."
              f" Must be using Python 3.7 or above")
    raise Exception("Must be using Python 3.7 or above")
else:
    log.info(f"Python verison {sys.version_info}")

CONF_FILE = (f"{os.path.dirname(os.path.realpath(__file__))}"
             f"/_conf/package_statistics.json")


class Config:
    """Class for work with configuration:
    read configuration from json file
    and save configuration to json file if it's needed
    
    Note! This Class can be moved to external script file
    """
    def __init__(self, conf_filename):
        """Default constructor
    
        Args:
            conf_filename (String): name of the file with script params
        """
        self.filename = conf_filename
        self.settings = {}
        self.read_settings()

    def read_settings(self):
        """Read parameters from file
        """
        try:
            with closing(open(self.filename, "r")) as json_file:
                self.settings = json.load(json_file)
        except Exception as err:
            log.error(self.filename, err)


def get_file(url):
    """Download file and save it to the disk

    Args:
        url (String): file URL
    """

    file_name = url.split('/')[-1]
    with urllib.request.urlopen(url) as u:
        file_size = int(u.headers['Content-Length'])
        if (not os.path.exists(file_name)
                or file_size != os.stat(file_name).st_size):
            log.info(f"Downloading: {file_name} Bytes: {file_size}")
            file_size_dl = 0
            block_sz = 8192 * 32
            with closing(open(file_name, 'wb')) as dest_file:
                while True:
                    try:
                        buffer = u.read(block_sz)
                        if not buffer:
                            break
                    except Exception as err:
                        log.error(err)
                        break

                    file_size_dl += len(buffer)

                    try:
                        dest_file.write(buffer)
                    except Exception as err:
                        log.error(err)
                        break

                    log.info(f"{file_size_dl} bytes "
                             f"{(file_size_dl * 100. / file_size):.2f}%")
            log.info(f"Downloaded: {file_name} Bytes: {file_size_dl}")
        else:
            log.info(f"File {file_name} exist "
                     f"with the same size {file_size} bytes")


def proceed_file(mirror_url, sarch):
    """Proceed requested file

    Args:
        mirror_url (String): Debian mirror 
        sarch (String): architecture (amd64, arm64, mips etc.)
    """
    filename = f"Contents-{sarch}.gz"
    url = f"{mirror_url}/{filename}"
    get_file(url)
    freq_array = {}
    with gzip.open(filename, 'rb') as f:
        for line in f:
            values = line.decode().strip().split()
            for key in values[1].split(','):
                k = key.split('/')[-1]
                if freq_array.get(k):
                    freq_array[k] += 1
                else:
                    freq_array[k] = 1
    result = dict(
        sorted(freq_array.items(), key=lambda item: item[1], reverse=True))
    idx = 1
    for key in result:
        print(f"{idx}. {key} {result[key]}")
        idx += 1
        if idx > 10:
            break


def main():
    """Main function
    """
    settings = Config(CONF_FILE).settings
    if settings.get("mirror_url"):
        mirror_url = settings["mirror_url"]
    else:
        log.info("Mirror URL not found, exit")
        sys.exit()

    if settings.get("SARCH"):
        sarch = settings["SARCH"]
    else:
        log.info("Types not found, exit")
        sys.exit()

    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg in sarch:
                proceed_file(mirror_url, arg)
    else:
        proceed_file(mirror_url, "all")


if __name__ == "__main__":
    main()
