#!/usr/bin/env python
# -*- coding: utf8 -*-
import MFRC522

class nTag:
    HEADER_PAGE = 0
    BODY_PAGE_START = 4
    PAGE_SIZE = 4

    pages = 0

    def __init__(self, reader, uid):
        self.uid = uid
        self.reader = reader

        self.readHeader()

    def readHeader(self):
        data = self.reader.read(self.HEADER_PAGE)
        self.pages = data[14] * 2

    def readBody(self):
        for page in range(self.BODY_PAGE_START, self.BODY_PAGE_START + self.pages):
            print(self.PAGE_SIZE * page)
            print(self.reader.read(self.PAGE_SIZE * page))
