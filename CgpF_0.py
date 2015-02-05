import xml.etree.ElementTree as et
import csv

xmltext = '''
<dict>
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_00</string>
            <key>lecture_number</key>
            <integer>0</integer>
            <key>lecture_title</key>
            <string>Hello, how are you?</string>    	
            <key>lecture_sub_title</key>
            <string>Greetings</string>            
        </dict>        
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_01</string>
            <key>lecture_number</key>
            <integer>1</integer>
            <key>lecture_title</key>
            <string>What do you do for fun?</string>
            <key>lecture_sub_title</key>
            <string>Asking about jobs, hobbies and interests</string>
        </dict>
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_02</string>
            <key>lecture_number</key>
            <integer>2</integer>
            <key>lecture_title</key>
            <string>I like watching movies</string>
            <key>lecture_sub_title</key>
            <string>to talking about jobs, hobbies and interests</string>
        </dict>
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_03</string>
            <key>lecture_number</key>
            <integer>3</integer>
            <key>lecture_title</key>
            <string>Thanks a lot</string>
            <key>lecture_sub_title</key>
            <string>to Expressing Thanks</string>
        </dict>
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_04</string>
            <key>lecture_number</key>
            <integer>4</integer>
            <key>lecture_title</key>
            <string>It’s a great day</string>
            <key>lecture_sub_title</key>
            <string>to talking about the weather</string>
        </dict>
        <dict>
            <key>lecture_key</key>
            <string>pre_beginner_a_05</string>
            <key>lecture_number</key>
            <integer>5</integer>
            <key>lecture_title</key>
            <string>Is that your briefcase?</string>
            <key>lecture_sub_title</key>
            <string>to asking about possessions (singular)</string>
        </dict>

</dict>
'''

#f = open('output.txt', 'w')

#writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

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
    print data