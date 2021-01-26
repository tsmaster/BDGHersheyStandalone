import math
import random
import pathlib

import drawSvg as draw
import bdgmath as m

def unwrapFile(f):
    prevLine = None
    for line in f.readlines():
        while line and line[-1] in "\n\r":
            line = line[:-1]
        if not line:
            continue
            
        try:
            prefix = int(line[:5])

            if prevLine:
                yield prevLine
            prevLine = line
        except ValueError as ve:
            prevLine += line

    yield prevLine
            
        
def decodeCoord(c):
    cVal = ord(c)
    rVal = ord('R')
    return cVal - rVal

def drawHersheyChar(dwg, s, pos, scale):
    p = draw.Path(stroke_width = 2, stroke='black', fill='none')

    numVerts = int(s[5:8])

    leftPos = decodeCoord(s[8])
    rightPos = decodeCoord(s[9])

    remainder = s[10:]

    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    yFlip = True

    moveFlag = True
    for vi in range(0, numVerts - 1):
        cx = s[10 + 2 * vi]
        cy = s[11 + 2 * vi]

        if cx + cy == " R":
            moveFlag = True
            continue
        
        xVal = decodeCoord(cx)
        yVal = decodeCoord(cy)

        if yFlip:
            yVal = -yVal

        if vi == 0:
            minX = xVal
            maxX = xVal
            minY = yVal
            maxY = yVal
        else:
            minX = min(minX, xVal)
            maxX = max(maxX, xVal)
            minY = min(minY, yVal)
            maxY = max(maxY, yVal)

        pt = pos.addVec2(m.Vector2(xVal, yVal).mulScalar(scale))
        if moveFlag:
            p.M(*pt.components)
        else:
            p.L(*pt.components)
        moveFlag = False
    dwg.append(p)

    return (minX * scale, minY * scale, maxX * scale, maxY * scale)

def getHersheyBounds(s):
    numVerts = int(s[5:8])

    leftPos = decodeCoord(s[8])
    rightPos = decodeCoord(s[9])
    
    minX = min(leftPos, rightPos)
    maxX = max(leftPos, rightPos)
    minY = 0
    maxY = 0

    yFlip = True

    moveFlag = True
    for vi in range(0, numVerts - 1):
        cx = s[10 + 2 * vi]
        cy = s[11 + 2 * vi]

        if cx + cy == " R":
            moveFlag = True
            continue
        
        xVal = decodeCoord(cx)
        yVal = decodeCoord(cy)

        if yFlip:
            yVal = -yVal

        if vi == 0:
            minX = xVal
            maxX = xVal
            minY = yVal
            maxY = yVal
        else:
            minX = min(minX, xVal)
            maxX = max(maxX, xVal)
            minY = min(minY, yVal)
            maxY = max(maxY, yVal)

    return (minX, minY, maxX, maxY)




class HersheyFont:
    def __init__(self, filename):
        pp = pathlib.PurePath(filename)
        self.name = pp.stem

        self.lines = []
        self.bounds = {}

        self.extraCharSpacing = 0

        self.readFile(filename)

    def readFile(self, filename):
        with open(filename, "rt") as hf:
            for line in unwrapFile(hf):
                self.lines.append(line)

    def getCharBounds(self, charNum):
        if charNum in self.bounds.keys():
            return self.bounds[charNum]
        b = getHersheyBounds(self.lines[charNum])
        self.bounds[charNum] = b
        return b

    def drawChar(self, dwg, charNum, pos, scale):
        drawHersheyChar(dwg, self.lines[charNum], pos, scale)

    def charRange(self):
        return range(0, len(self.lines))

    def charToCharNum(self, c):
        c = ord(c)
        return c - 32

    def getCharWidth(self, c, scale):
        xMin, yMin, xMax, yMax = self.getCharBounds(self.charToCharNum(c))
        return (xMax - xMin) * scale

    def getStringWidth(self, w, scale):
        return sum([self.getCharWidth(c, scale) + self.extraCharSpacing * scale for c in w])

    def genLines(self, s, scale, lineLength):
        working = ""
        for w in s.split():
            if working:
                newWorking = working + " " + w
            else:
                newWorking = w
            workingLineLength = self.getStringWidth(newWorking, scale)
            
            if workingLineLength > lineLength:
                # adding this line would make the line too long
                yield working

                # this WORD is too long, just output it on a line by itself
                if self.getStringWidth(w, scale) > lineLength:
                    yield w
                    working = ""
                else:
                    working = w
            else:
                working = newWorking
        yield working
    
    def drawString(self, dwg, s, pos, scale):
        while s:
            c = s[0]
            s = s[1:]

            charNum = self.charToCharNum(c)
            if ((charNum >= 0) and
                (charNum < len(self.lines))):

                xMin, yMin, xMax, yMax = self.getCharBounds(charNum)
                charAdv = m.Vector2(-xMin * scale, 0)
                self.drawChar(dwg, charNum, pos.addVec2(charAdv), scale)
                advanceValue = xMax - xMin + self.extraCharSpacing
            else:
                advanceValue = 10 + self.extraCharSpacing
            pos = pos.addVec2(m.Vector2(advanceValue, 0).mulScalar(scale))

    def drawWrappedString(self, dwg, s, left, right, first, scale, lineAdvance):
        pos = m.Vector2(left, first)
        for line in self.genLines(s, scale, right - left):
            self.drawString(dwg, line, pos, scale)
            pos = pos.addVec2(m.Vector2(0, -lineAdvance))
            
        
        
