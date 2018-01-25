#!/usr/bin/env python
# -*- coding: utf8 -*-
import MFRC522

class nTag:
    HEADER_PAGE = 0
    BODY_PAGE_START = 1
    PAGE_SIZE = 4

    pages = 0

    def __init__(self, reader, uid):
        self.uid = uid
        self.reader = reader

        self.readHeader()

    def readHeader(self):
        data = self.reader.read(self.HEADER_PAGE)
        self.pages = data[14] / 2

    def readBody(self):
        result = []
        for page in range(0, self.pages):
            data = self.reader.read(self.PAGE_SIZE * (self.BODY_PAGE_START + page))
            result = result + data

        return result

    def readBodyAsString(self):
        rawBody = self.readBody()
        characters = map(chr, rawBody)
        return "".join(characters).strip(chr(0))

    def writeString(self, string):
        self.reader.writeString(string, self.BODY_PAGE_START * self.PAGE_SIZE)

