# -*- coding: cp1251 -*-
import xml.etree.ElementTree as et
import plistlib
import csv
from pprint import pprint

xmltext = """
<dict>
 
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
        <string>Where’s the ladies’ room?</string>
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
        <string>It’s below the whiteboard</string>
        <key>lecture_sub_title</key>
        <string>to talking about location (singular)</string>
        <key>video_intro</key>
        <string>_2_uqlyl1yc</string>
        <key>video_practice</key>
        <string>0Yr3FH7JFeM</string>
    </dict>
 

    
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_01</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>How are you getting along this month?</string>
        <key>lecture_sub_title</key>
        <string>to asking about other people</string>
        <key>video_intro</key>
        <string>Uat8fvD9MBM</string>
        <key>video_practice</key>
        <string>EfdfHHXF7vE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_02</string>
        <key>lecture_number</key>
        <integer>2</integer>
        <key>lecture_title</key>
        <string>I’m doing just fine</string>
        <key>lecture_sub_title</key>
        <string>to talking about people</string>
        <key>video_intro</key>
        <string>RB4mia2pwZ0</string>
        <key>video_practice</key>
        <string>HD-pnTrlq6w</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_03</string>
        <key>lecture_number</key>
        <integer>3</integer>
        <key>lecture_title</key>
        <string>What do you do for a living?</string>
        <key>lecture_sub_title</key>
        <string>to asking about jobs and interests</string>
        <key>video_intro</key>
        <string>rX1a0J2Cr0Y</string>
        <key>video_practice</key>
        <string>-MmmTYggiwU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_04</string>
        <key>lecture_number</key>
        <integer>4</integer>
        <key>lecture_title</key>
        <string>I do cardio at the gym</string>
        <key>lecture_sub_title</key>
        <string>to talking about jobs and interests</string>
        <key>video_intro</key>
        <string>DVvYuqSpRxo</string>
        <key>video_practice</key>
        <string>4PasiV6eGq0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_05</string>
        <key>lecture_number</key>
        <integer>5</integer>
        <key>lecture_title</key>
        <string>Have you been to Canada before?</string>
        <key>lecture_sub_title</key>
        <string>to Travel Experience Questions</string>
        <key>video_intro</key>
        <string>5fG5vhupcRY</string>
        <key>video_practice</key>
        <string>W3p-LvfYaiU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_06</string>
        <key>lecture_number</key>
        <integer>6</integer>
        <key>lecture_title</key>
        <string>She’s been to Italy six times</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel experiences</string>
        <key>video_intro</key>
        <string>2Xefdi3c_dY</string>
        <key>video_practice</key>
        <string>a4wQYID6ruo</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_07</string>
        <key>lecture_number</key>
        <integer>7</integer>
        <key>lecture_title</key>
        <string>She hasn’t been in a five star hotel</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel experiences negatively</string>
        <key>video_intro</key>
        <string>wF8Qk3pCQQM</string>
        <key>video_practice</key>
        <string>JpINuH8jBF0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_08</string>
        <key>lecture_number</key>
        <integer>8</integer>
        <key>lecture_title</key>
        <string>Are you going to see a movie at the new theater?</string>
        <key>lecture_sub_title</key>
        <string>to asking about personal plans</string>
        <key>video_intro</key>
        <string>54m2NrFvmpc</string>
        <key>video_practice</key>
        <string>TRl9ZgxTYg0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_09</string>
        <key>lecture_number</key>
        <integer>9</integer>
        <key>lecture_title</key>
        <string>Yes, I’m going to go on a guided tour</string>
        <key>lecture_sub_title</key>
        <string>to talking about personal plans</string>
        <key>video_intro</key>
        <string>BArZ9CEs9M8</string>
        <key>video_practice</key>
        <string>U6JHxVcP1Ac</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_10</string>
        <key>lecture_number</key>
        <integer>10</integer>
        <key>lecture_title</key>
        <string>I'm not going to catch a show</string>
        <key>lecture_sub_title</key>
        <string>to talking about personal plans negatively</string>
        <key>video_intro</key>
        <string>sOnwQ4bocUM</string>
        <key>video_practice</key>
        <string>v2WiUJavnrU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_11</string>
        <key>lecture_number</key>
        <integer>11</integer>
        <key>lecture_title</key>
        <string>What did you have for brunch?</string>
        <key>lecture_sub_title</key>
        <string>to asking about previous activities</string>
        <key>video_intro</key>
        <string>Xq3_cyl2XV0</string>
        <key>video_practice</key>
        <string>9KciTkE9eUg</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_12</string>
        <key>lecture_number</key>
        <integer>12</integer>
        <key>lecture_title</key>
        <string>I had a relaxing time on Sunday afternoon</string>
        <key>lecture_sub_title</key>
        <string>to talking about previous activities</string>
        <key>video_intro</key>
        <string>sVpp_9YaZ6A</string>
        <key>video_practice</key>
        <string>i_IrLku0Hq8</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_13</string>
        <key>lecture_number</key>
        <integer>13</integer>
        <key>lecture_title</key>
        <string>What do you think about the headline this morning?</string>
        <key>lecture_sub_title</key>
        <string>to asking opinions</string>
        <key>video_intro</key>
        <string>u5miqzz6tnI</string>
        <key>video_practice</key>
        <string>hPNIDD4S0QM</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_14</string>
        <key>lecture_number</key>
        <integer>14</integer>
        <key>lecture_title</key>
        <string>I think that the service today is okay</string>
        <key>lecture_sub_title</key>
        <string>to giving opinions</string>
        <key>video_intro</key>
        <string>fVIkw01SJgw</string>
        <key>video_practice</key>
        <string>hZFVFiWe97A</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_15</string>
        <key>lecture_number</key>
        <integer>15</integer>
        <key>lecture_title</key>
        <string>How are the desserts at this restaurant?</string>
        <key>lecture_sub_title</key>
        <string>Asking about quality -  present</string>
        <key>video_intro</key>
        <string>GFvalLiNqxw</string>
        <key>video_practice</key>
        <string>1p20fOB9YxA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_16</string>
        <key>lecture_number</key>
        <integer>16</integer>
        <key>lecture_title</key>
        <string>It’s out of sight and delish !</string>
        <key>lecture_sub_title</key>
        <string>Talking about quality -  present</string>
        <key>video_intro</key>
        <string>LBkwKyVq_MY</string>
        <key>video_practice</key>
        <string>Eai1dRf9aR0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_17</string>
        <key>lecture_number</key>
        <integer>17</integer>
        <key>lecture_title</key>
        <string>How was the concert on the lawn?</string>
        <key>lecture_sub_title</key>
        <string>Practicing asking about quality - Past</string>
        <key>video_intro</key>
        <string>BvDrx5_9TNc</string>
        <key>video_practice</key>
        <string>CcC4RZujZec</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_18</string>
        <key>lecture_number</key>
        <integer>18</integer>
        <key>lecture_title</key>
        <string>They were cool and really on!</string>
        <key>lecture_sub_title</key>
        <string>Talking about quality - past</string>
        <key>video_intro</key>
        <string>j5yNURWIPwY</string>
        <key>video_practice</key>
        <string>PlZ8E6W_SXs</string>
    </dict>



    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_00</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>Hello, how are you?</string>
        <key>lecture_sub_title</key>
        <string>Greetings</string>
        <key>lecture_section</key>
        <integer>1</integer>
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
        <key>lecture_section</key>
        <integer>1</integer>
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
        <key>lecture_section</key>
        <integer>1</integer>
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
        <key>lecture_section</key>
        <integer>1</integer>
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
        <string>Where’s the ladies’ room?</string>
        <key>lecture_sub_title</key>
        <string>to asking about location (singular)</string>
        <key>lecture_section</key>
        <integer>1</integer>
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
        <string>It’s below the whiteboard</string>
        <key>lecture_sub_title</key>
        <string>to talking about location (singular)</string>
        <key>lecture_section</key>
        <integer>1</integer>
        <key>video_intro</key>
        <string>_2_uqlyl1yc</string>
        <key>video_practice</key>
        <string>0Yr3FH7JFeM</string>
    </dict>



    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_03</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>Could you help my friend for a moment?</string>
        <key>lecture_sub_title</key>
        <string>asking questions when shopping</string>
        <key>video_intro</key>
        <string>5hRMsVUurF0</string>
        <key>video_practice</key>
        <string>6sa0qnPnSCU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_04</string>
        <key>lecture_number</key>
        <integer>2</integer>
        <key>lecture_title</key>
        <string>How are those jeans?</string>
        <key>lecture_sub_title</key>
        <string>making statements when shopping</string>
        <key>video_intro</key>
        <string>QuP8Mmnm2XA</string>
        <key>video_practice</key>
        <string>HGyztxkOVpY</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_12</string>
        <key>lecture_number</key>
        <integer>3</integer>
        <key>lecture_title</key>
        <string>I need a table for two near the window</string>
        <key>lecture_sub_title</key>
        <string>making reservations</string>
        <key>video_intro</key>
        <string>Y3-hAbE42pE</string>
        <key>video_practice</key>
        <string>gbX7IYu1jbA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_05</string>
        <key>lecture_number</key>
        <integer>4</integer>
        <key>lecture_title</key>
        <string>Could you bring me another glass of water?</string>
        <key>lecture_sub_title</key>
        <string>asking questions at a bar or restaurant</string>
        <key>video_intro</key>
        <string>BjMyC-zcUB4</string>
        <key>video_practice</key>
        <string>EX7331VFEPo</string>
    </dict>
    

    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_12</string>
        <key>lecture_number</key>
        <integer>5</integer>
        <key>lecture_title</key>
        <string>I’d like room service this evening please</string>
        <key>lecture_sub_title</key>
        <string>to asking a waiter</string>
        <key>video_intro</key>
        <string>E37oigI23LU</string>
        <key>video_practice</key>
        <string>05DS0G_jWIY</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_13</string>
        <key>lecture_number</key>
        <integer>6</integer>
        <key>lecture_title</key>
        <string>Can I try on that jacket please?</string>
        <key>lecture_sub_title</key>
        <string>to asking in a store</string>
        <key>video_intro</key>
        <string>E2cVAikvHbY</string>
        <key>video_practice</key>
        <string>vfpjRgd1IyM</string>
    </dict>
    
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_13</string>
        <key>lecture_number</key>
        <integer>7</integer>
        <key>lecture_title</key>
        <string>What do you think about the headline this morning?</string>
        <key>lecture_sub_title</key>
        <string>to asking opinions</string>
        <key>video_intro</key>
        <string>u5miqzz6tnI</string>
        <key>video_practice</key>
        <string>hPNIDD4S0QM</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_14</string>
        <key>lecture_number</key>
        <integer>8</integer>
        <key>lecture_title</key>
        <string>I think that the service today is okay</string>
        <key>lecture_sub_title</key>
        <string>to giving opinions</string>
        <key>video_intro</key>
        <string>fVIkw01SJgw</string>
        <key>video_practice</key>
        <string>hZFVFiWe97A</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_15</string>
        <key>lecture_number</key>
        <integer>9</integer>
        <key>lecture_title</key>
        <string>How are the desserts at this restaurant?</string>
        <key>lecture_sub_title</key>
        <string>Asking about quality -  present</string>
        <key>video_intro</key>
        <string>GFvalLiNqxw</string>
        <key>video_practice</key>
        <string>1p20fOB9YxA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_16</string>
        <key>lecture_number</key>
        <integer>10</integer>
        <key>lecture_title</key>
        <string>It’s out of sight and delish !</string>
        <key>lecture_sub_title</key>
        <string>Talking about quality -  present</string>
        <key>video_intro</key>
        <string>LBkwKyVq_MY</string>
        <key>video_practice</key>
        <string>Eai1dRf9aR0</string>
    </dict>

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
        <string>everyday_english_b_01</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>Is it possible to get a flight?</string>
        <key>lecture_sub_title</key>
        <string>to travel bookings</string>
        <key>video_intro</key>
        <string>GhEOM5cWr_s</string>
        <key>video_practice</key>
        <string>lxFYMPviKQg</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_02</string>
        <key>lecture_number</key>
        <integer>2</integer>
        <key>lecture_title</key>
        <string>My plane touches down at 7:55</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel plans and facts</string>
        <key>video_intro</key>
        <string>GI59L63bxP4</string>
        <key>video_practice</key>
        <string>QtBgtvWNaCE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_03</string>
        <key>lecture_number</key>
        <integer>3</integer>
        <key>lecture_title</key>
        <string>Can we get two coffees after take off please?</string>
        <key>lecture_sub_title</key>
        <string>to asking on flights</string>
        <key>video_intro</key>
        <string>QyyE7OXArmM</string>
        <key>video_practice</key>
        <string>-k8KefXHmBE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_04</string>
        <key>lecture_number</key>
        <integer>4</integer>
        <key>lecture_title</key>
        <string>Where can I rent a van for cheap?</string>
        <key>lecture_sub_title</key>
        <string>to asking about transportation using “where”</string>
        <key>video_intro</key>
        <string>lera9pYD234</string>
        <key>video_practice</key>
        <string>1JFF6BhYEik</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_05</string>
        <key>lecture_number</key>
        <integer>5</integer>
        <key>lecture_title</key>
        <string>How can I get back to the hotel tonight?</string>
        <key>lecture_sub_title</key>
        <string>to asking about transportation using “how”</string>
        <key>video_intro</key>
        <string>ck3mbg_wuAE</string>
        <key>video_practice</key>
        <string>Upk4m8LegjM</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_06</string>
        <key>lecture_number</key>
        <integer>6</integer>
        <key>lecture_title</key>
        <string>When does the train leave for downtown?</string>
        <key>lecture_sub_title</key>
        <string>to asking about transportation times</string>
        <key>video_intro</key>
        <string>ND1MOYep02U</string>
        <key>video_practice</key>
        <string>QGG1EqWICuA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_07</string>
        <key>lecture_number</key>
        <integer>7</integer>
        <key>lecture_title</key>
        <string>How do I get to the nearest pharmacy please?</string>
        <key>lecture_sub_title</key>
        <string>to asking for directions</string>
        <key>video_intro</key>
        <string>s8AwmbKnwr0</string>
        <key>video_practice</key>
        <string>J-nsQiNpWrs</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_08</string>
        <key>lecture_number</key>
        <integer>8</integer>
        <key>lecture_title</key>
        <string>Are there villas available with private pools?</string>
        <key>lecture_sub_title</key>
        <string>to asking about travel facilities</string>
        <key>video_intro</key>
        <string>v9TF6VaJ_wQ</string>
        <key>video_practice</key>
        <string>XBxGfrauNoA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_09</string>
        <key>lecture_number</key>
        <integer>9</integer>
        <key>lecture_title</key>
        <string>Yes, there are spaces available in the restaurant tonight.</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel facilities</string>
        <key>video_intro</key>
        <string>wLxqLkdM-II</string>
        <key>video_practice</key>
        <string>h02CHN8HDLc</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_10</string>
        <key>lecture_number</key>
        <integer>10</integer>
        <key>lecture_title</key>
        <string>No, there aren’t complimentary drinks upon arrival.</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel facilities negative answers</string>
        <key>video_intro</key>
        <string>nt-zLg_w9QM</string>
        <key>video_practice</key>
        <string>ehgr46vmvHg</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_11</string>
        <key>lecture_number</key>
        <integer>11</integer>
        <key>lecture_title</key>
        <string>I’d like room service this evening please</string>
        <key>lecture_sub_title</key>
        <string>to making requests at the hotel front desk</string>
        <key>video_intro</key>
        <string>HZUYaVZJNOU</string>
        <key>video_practice</key>
        <string>pXvwyxdcUxE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_12</string>
        <key>lecture_number</key>
        <integer>12</integer>
        <key>lecture_title</key>
        <string>I’d like room service this evening please</string>
        <key>lecture_sub_title</key>
        <string>to asking a waiter</string>
        <key>video_intro</key>
        <string>E37oigI23LU</string>
        <key>video_practice</key>
        <string>05DS0G_jWIY</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_b_13</string>
        <key>lecture_number</key>
        <integer>13</integer>
        <key>lecture_title</key>
        <string>Can I try on that jacket please?</string>
        <key>lecture_sub_title</key>
        <string>to asking in a store</string>
        <key>video_intro</key>
        <string>E2cVAikvHbY</string>
        <key>video_practice</key>
        <string>vfpjRgd1IyM</string>
    </dict>

    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_05</string>
        <key>lecture_number</key>
        <integer>14</integer>
        <key>lecture_title</key>
        <string>Have you been to Canada before?</string>
        <key>lecture_sub_title</key>
        <string>to Travel Experience Questions</string>
        <key>video_intro</key>
        <string>5fG5vhupcRY</string>
        <key>video_practice</key>
        <string>W3p-LvfYaiU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_06</string>
        <key>lecture_number</key>
        <integer>15</integer>
        <key>lecture_title</key>
        <string>She’s been to Italy six times</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel experiences</string>
        <key>video_intro</key>
        <string>2Xefdi3c_dY</string>
        <key>video_practice</key>
        <string>a4wQYID6ruo</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_07</string>
        <key>lecture_number</key>
        <integer>16</integer>
        <key>lecture_title</key>
        <string>She hasn’t been in a five star hotel</string>
        <key>lecture_sub_title</key>
        <string>to talking about travel experiences negatively</string>
        <key>video_intro</key>
        <string>wF8Qk3pCQQM</string>
        <key>video_practice</key>
        <string>JpINuH8jBF0</string>
    </dict>

    <dict>
        <key>lecture_key</key>
        <string>pre_beginner_a_00</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>Hello, how are you?</string>
        <key>lecture_sub_title</key>
        <string>Greetings</string>
        <key>lecture_section</key>
        <integer>1</integer>
        <key>video_intro</key>
        <string></string>
        <key>video_practice</key>
        <string></string>
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
        <key>lecture_section</key>
        <integer>1</integer>
        <key>video_intro</key>
        <string></string>
        <key>video_practice</key>
        <string></string>
    </dict>

    
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_01</string>
        <key>lecture_number</key>
        <integer>1</integer>
        <key>lecture_title</key>
        <string>I’m calling to make a reservation at 7pm tomorrow</string>
        <key>lecture_sub_title</key>
        <string>Starting a Call</string>
        <key>video_intro</key>
        <string>YBQFqbR_kYY</string>
        <key>video_practice</key>
        <string>YcqEB_w5Ejs</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_02</string>
        <key>lecture_number</key>
        <integer>2</integer>
        <key>lecture_title</key>
        <string>Would you like to leave a message?</string>
        <key>lecture_sub_title</key>
        <string>Understanding the Other Caller</string>
        <key>video_intro</key>
        <string>JZ8WYs9LnRM</string>
        <key>video_practice</key>
        <string>FDapkUtBEiA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_06</string>
        <key>lecture_number</key>
        <integer>3</integer>
        <key>lecture_title</key>
        <string>Is it possible to hire a caddy?</string>
        <key>lecture_sub_title</key>
        <string>asking questions at the golf course</string>
        <key>video_intro</key>
        <string>Pucxzbx_9-s</string>
        <key>video_practice</key>
        <string>FDapkUtBEiA</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_07</string>
        <key>lecture_number</key>
        <integer>4</integer>
        <key>lecture_title</key>
        <string>What do you recommend for a cold?</string>
        <key>lecture_sub_title</key>
        <string>asking questions at the pharmacy</string>
        <key>video_intro</key>
        <string>Tf0Esg0BnoI</string>
        <key>video_practice</key>
        <string>0qftAbmP6VE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_08</string>
        <key>lecture_number</key>
        <integer>5</integer>
        <key>lecture_title</key>
        <string>Yes, I have a cold</string>
        <key>lecture_sub_title</key>
        <string>making statements at the pharmacy</string>
        <key>video_intro</key>
        <string>PqPuVBbchT4</string>
        <key>video_practice</key>
        <string>A8ethlz2CXE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_09</string>
        <key>lecture_number</key>
        <integer>6</integer>
        <key>lecture_title</key>
        <string>Are you going to draw my blood for testing?</string>
        <key>lecture_sub_title</key>
        <string>asking questions at the medical center</string>
        <key>video_intro</key>
        <string>ITjPKOtHURU</string>
        <key>video_practice</key>
        <string>mdu81YuwMtg</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_10</string>
        <key>lecture_number</key>
        <integer>7</integer>
        <key>lecture_title</key>
        <string>I feel dizzy</string>
        <key>lecture_sub_title</key>
        <string>making statements at the medical center</string>
        <key>video_intro</key>
        <string>nRZvr3WcuZY</string>
        <key>video_practice</key>
        <string>b7feovFAGGc</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_11</string>
        <key>lecture_number</key>
        <integer>8</integer>
        <key>lecture_title</key>
        <string>Can I use one of the tanning beds?</string>
        <key>lecture_sub_title</key>
        <string>asking questions at the spa</string>
        <key>video_intro</key>
        <string>oOP8bmzpnX8</string>
        <key>video_practice</key>
        <string>5aJrePKeERE</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_13</string>
        <key>lecture_number</key>
        <integer>9</integer>
        <key>lecture_title</key>
        <string>He wants to wire money to Canada</string>
        <key>lecture_sub_title</key>
        <string>making statements at the bank</string>
        <key>video_intro</key>
        <string>pY3DbzHanr4</string>
        <key>video_practice</key>
        <string>LHf-kVD1vJ0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_14</string>
        <key>lecture_number</key>
        <integer>10</integer>
        <key>lecture_title</key>
        <string>Do you require a down payment?</string>
        <key>lecture_sub_title</key>
        <string>asking questions while looking for a Residence</string>
        <key>video_intro</key>
        <string>UQwMjxAStjo</string>
        <key>video_practice</key>
        <string>JYZRj0gssPQ</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_15</string>
        <key>lecture_number</key>
        <integer>11</integer>
        <key>lecture_title</key>
        <string>Yes, she’d like to rent a place in the country</string>
        <key>lecture_sub_title</key>
        <string>making statements while looking for a residence</string>
        <key>video_intro</key>
        <string>4oNqCaf6-t0</string>
        <key>video_practice</key>
        <string>AK5_w5dhXrM</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_c_16</string>
        <key>lecture_number</key>
        <integer>12</integer>
        <key>lecture_title</key>
        <string>Can I take your coat?</string>
        <key>lecture_sub_title</key>
        <string>Being a Host</string>
        <key>video_intro</key>
        <string>xWIwW7UjHD4</string>
        <key>video_practice</key>
        <string>AK5_w5dhXrM</string>
    </dict>


    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_03</string>
        <key>lecture_number</key>
        <integer>13</integer>
        <key>lecture_title</key>
        <string>What do you do for a living?</string>
        <key>lecture_sub_title</key>
        <string>to asking about jobs and interests</string>
        <key>video_intro</key>
        <string>rX1a0J2Cr0Y</string>
        <key>video_practice</key>
        <string>-MmmTYggiwU</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_04</string>
        <key>lecture_number</key>
        <integer>14</integer>
        <key>lecture_title</key>
        <string>I do cardio at the gym</string>
        <key>lecture_sub_title</key>
        <string>to talking about jobs and interests</string>
        <key>video_intro</key>
        <string>DVvYuqSpRxo</string>
        <key>video_practice</key>
        <string>4PasiV6eGq0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_08</string>
        <key>lecture_number</key>
        <integer>15</integer>
        <key>lecture_title</key>
        <string>Are you going to see a movie at the new theater?</string>
        <key>lecture_sub_title</key>
        <string>to asking about personal plans</string>
        <key>video_intro</key>
        <string>54m2NrFvmpc</string>
        <key>video_practice</key>
        <string>TRl9ZgxTYg0</string>
    </dict>
    <dict>
        <key>lecture_key</key>
        <string>everyday_english_a_09</string>
        <key>lecture_number</key>
        <integer>16</integer>
        <key>lecture_title</key>
        <string>Yes, I’m going to go on a guided tour</string>
        <key>lecture_sub_title</key>
        <string>to talking about personal plans</string>
        <key>video_intro</key>
        <string>BArZ9CEs9M8</string>
        <key>video_practice</key>
        <string>U6JHxVcP1Ac</string>
    </dict>



</dict>
"""

#f = open('output.txt', 'w')

#writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

#pl = plistlib.readPlistFromString(xmltext)
#pprint(pl)

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
