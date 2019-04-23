import sys
import json
from PIL import Image
from decimal import *

def get_object_class(region, file, names):
    try:        
        type = region['region_attributes']['Type']
        package = region['region_attributes']['package']
    except KeyError:
        print >> sys.stderr, "type or package info is missing in ", file

    name = type + " " + package
    index = [item.lower() for item in names].index(name.lower())
    
    return index

def get_dark_annotation(region, size):
        x = region['shape_attributes']['x']
        y = region['shape_attributes']['y']
        width = region['shape_attributes']['width']
        height = region['shape_attributes']['height']

        _x      = Decimal(x + width) / Decimal(2 * size[0]) # relative position of center x of rect
        _y      = Decimal(y + height) / Decimal(2 * size[1]) # relative position of center y of rect
        _width  = Decimal(width / size[0])
        _height = Decimal(height / size[1])

        return "{0:.10f} {0:.10f} {0:.10f} {0:.10f}".format(_x, _y, _width, _height)

def main():
    with open(sys.argv[1:][0]) as file:
        dict = json.load(file)
        
        try:        
            namesFile = sys.argv[1:][1]
            names = open(namesFile).read().split('\n')
        except IndexError:
            print >> sys.stderr, "names file's missing from argument.\n\tnamesFile = sys.argv[1:][1]\nIndexError: list index out of range"

        for key in dict.keys():
            data = dict[key]

            imageName = data['filename']
            filename = imageName.rsplit('.', 1)[0]
            
            regions = data['regions']

            try:        
                img = Image.open(imageName)
            except IOError:
                print >> sys.stderr, "No such file" , imageName

            content = ""
            for region in regions:
                obj_class = get_object_class(region, imageName, names)
                annotation = get_dark_annotation(region, img.size)
                content += "{} {}\n".format(obj_class, annotation)

            with open("{}.txt".format(filename), "w") as outFile:
                outFile.write(content)

if __name__ == "__main__":
    main()