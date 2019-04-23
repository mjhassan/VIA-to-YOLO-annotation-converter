# VIA-to-YOLO-annotation-converter

VGG Image Annotator ([VIA](http://www.robots.ox.ac.uk/~vgg/software/via/)) is an  open source image annotation tool, built on html and css. The main limitations of this tools is only two export format, csv and json.

You Only Look Once or YOLO is a Unified, Real-Time Object Detection system. It needs a specific type of data annotation, will be found at [How to train YOLOv2 to detect custom objects](https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36).

This python script will convert the VIA annotations into YOLO compatible format.

## How to use it
- Export VIA annotations as json, into the images directory. It will save as **via_region_data.json**.
- Download and copy this script into that directory.
- Create a text file with all the attributes are used in VIA annotations; let's call it **via.names**.
- Run the following command
```python
python via2dark.py via_region_data.json via.names
```
