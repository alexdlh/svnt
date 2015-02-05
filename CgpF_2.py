import xml.etree.ElementTree as et
import plistlib
import csv
from pprint import pprint

xmltext = """


<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    
    
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_00</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>Hello, how are you?</string>
        <key>lecture_sub_title</key>
        <string>Greetings</string>
        <key>video_intro</key>
        <string>lQIe1YBdQPs</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_03</string>
        <key>lecture_number</key>
        <integer>2</integer>
        <key>lecture_title</key>
        <string>Thanks a lot</string>
        <key>lecture_sub_title</key>
        <string>to Expressing Thanks</string>
        <key>video_intro</key>
        <string>NiDpMepulCU</string>
        <key>video_practice</key>
        <string>DpLlEylBYRg</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_09</string>
        <key>lecture_number</key>
        <integer>3</integer>
        <key>lecture_title</key>
        <string>What brand is your jacket?</string>
        <key>lecture_sub_title</key>
        <string>to asking for information (singular)</string>
        <key>video_intro</key>
        <string>ZgPtACYCeq0</string>
        <key>video_practice</key>
        <string>-84VboGelWA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_10</string>
        <key>lecture_number</key>
        <integer>4</integer>
        <key>lecture_title</key>
        <string>A cold is an illness</string>
        <key>lecture_sub_title</key>
        <string>to giving information</string>
        <key>video_intro</key>
        <string>9Foho3LZdsY</string>
        <key>video_practice</key>
        <string>7eeR-kWF0mE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_13</string>
        <key>lecture_number</key>
        <integer>5</integer>
        <key>lecture_title</key>
        <string>Where's the ladies' room?</string>
        <key>lecture_sub_title</key>
        <string>to asking about location (singular)</string>
        <key>video_intro</key>
        <string>0RBOa10k7lc</string>
        <key>video_practice</key>
        <string>GgCTT7HJJI0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_14</string>
        <key>lecture_number</key>
        <integer>6</integer>
        <key>lecture_title</key>
        <string>It's below the whiteboard</string>
        <key>lecture_sub_title</key>
        <string>to talking about location (singular)</string>
        <key>video_intro</key>
        <string>_2_uqlyl1yc</string>
        <key>video_practice</key>
        <string>0Yr3FH7JFeM</string>
    </dict>
 
</array>

</plist>


"""

#f = open('output.txt', 'w')

#writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

pl = plistlib.readPlistFromString(xmltext)
pprint(pl)
"""
tree = et.fromstring(xmltext)

# iterate over the dict elements
for dict_el in tree.iterfind('dict'):
    data = []
    # get the text contents of each non-key element
    for el in dict_el:
        if el.tag == 'string' :
            #print el.text
            data.append(el.text)
        # if it's an integer element convert to int so csv wont quote it
        elif el.tag == 'integer':
            data.append(int(el.text))
    #writer.writerow(data)
    print data"""