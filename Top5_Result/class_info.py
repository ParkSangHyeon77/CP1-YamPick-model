import csv
import unicodedata

# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_class_info():
    class_data = []
    with open('/Users/dyson/Desktop/STUDY/CS/CP1/DE_return_top5/class_info.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            class_data = row
    return class_data 

def write_class_info():
    with open('/Users/dyson/Desktop/STUDY/CS/CP1/DE_return_top5/class_info.csv', 'w') as f:
        import os
        class_data = []
        for x in os.listdir('/Users/dyson/Desktop/STUDY/CS/CP1/Test_Image'):
            class_data.append(unicodedata.normalize('NFC',x))

        class_data.remove('.DS_Store')
        class_data.sort()

        write = csv.writer(f)
        write.writerow(class_data)
