
class HersheyAsset:
    def __init__(self, name, char_spacing):
        self.name = name
        self.charSpacing = char_spacing

    def filename(self):
        return self.name + ".jhf"


assets = [
    HersheyAsset("astrology", 4),
    HersheyAsset("cursive", 0),
    HersheyAsset("cyrilc_1", 4),
    HersheyAsset("cyrillic", 4),
    HersheyAsset("futural", 4),
    HersheyAsset("futuram", 4),
    HersheyAsset("gothgbt", 4),
    HersheyAsset("gothgrt", 4),
    HersheyAsset("gothiceng", 4),
    HersheyAsset("gothicger", 4),
    HersheyAsset("gothicita", 4),
    HersheyAsset("gothitt", 4),
    HersheyAsset("greek", 4),
    HersheyAsset("greekc", 4),
    HersheyAsset("greeks", 4),
    HersheyAsset("japanese", 4),
    HersheyAsset("markers", 4),
    HersheyAsset("mathlow", 4),
    HersheyAsset("mathupp", 4),
    HersheyAsset("meteorology", 4),
    HersheyAsset("music", 4),
    HersheyAsset("rowmand", 4),
    HersheyAsset("rowmans", 4),
    HersheyAsset("rowmant", 4),
    HersheyAsset("scriptc", 0),
    HersheyAsset("scripts", 0),
    HersheyAsset("symbolic", 4),
    HersheyAsset("timesg", 4),
    HersheyAsset("timesi", 4),
    HersheyAsset("timesib", 4),
    HersheyAsset("timesr", 4),
    HersheyAsset("timesrb", 4),
    ]

def findByName(name):
    for a in assets:
        if a.name == name:
            return a

    hits = []
    for a in assets:
        if a in name:
            hits.append(a)
    return hits
