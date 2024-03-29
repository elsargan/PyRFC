# SPDX-FileCopyrightText: 2013 SAP SE Srdjan Boskovic <srdjan.boskovic@sap.com>
#
# SPDX-License-Identifier: Apache-2.0

import datetime
from configparser import ConfigParser
from os import path
from pprint import pprint

from pyrfc import Connection

imp = {
    "RFCINT1": 0x7F,  # INT1: Integer value (1 byte)
    "RFCINT2": 0x7FFE,  # INT2: Integer value (2 bytes)
    "RFCINT4": 0x7FFFFFFE,  # INT: integer value (4 bytes)
    "RFCFLOAT": 1.23456789,  # FLOAT
    "RFCCHAR1": "a",  # CHAR[1]
    "RFCCHAR2": "ij",  # CHAR[2]
    "RFCCHAR4": "bcde",  # CHAR[4]
    "RFCDATA1": "k" * 50,
    "RFCDATA2": "l" * 50,  # CHAR[50] each
    "RFCTIME": datetime.time(
        12,
        34,
        56,
    ),  # TIME
    "RFCDATE": datetime.date(
        2012,
        10,
        3,
    ),  # DATE
    "RFCHEX3": b"\x66\x67\x68",  # BYTE[3]: String with 3 hexadecimal values (='fgh')
}


def main():
    config = ConfigParser()
    config.read(
        path.join(
            path.dirname(path.abspath(__file__)),
            "pyrfc.cfg",
        )
    )
    params_connection = dict(config.items("coevi51"))

    with Connection(**params_connection) as client:
        pprint(
            client.call(
                "STFC_STRUCTURE",
                IMPORTSTRUCT=imp,
            )
        )


if __name__ == "__main__":
    main()
