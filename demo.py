# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:51:49 2020

@author: Praveen N/ Kaleelurrahaman U
"""

import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('uQU2I7Pe6IpGZRtJD4Bf4aJxdDRYMuOjsI3EWkKUHaGm')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com')


url = 'https://homepages.cae.wisc.edu/~ece533/images/airplane.png'
print("Source image load")
fakeImageUrl = ['https://homepages.cae.wisc.edu/~ece533/images/airplane.png',\
                'https://homepages.cae.wisc.edu/~ece533/images/arctichare.png',\
                'https://homepages.cae.wisc.edu/~ece533/images/boat.png']
print("Image Processing Starts")
threshold=0.0
classes_result = visual_recognition.classify(url=url).get_result()
for item in fakeImageUrl:
    classes_result2 = visual_recognition.classify(url=item).get_result()
    if(classes_result==classes_result2):
        print("****************************")
        print("The Image recognised is FAKE")
        print("****************************")
        break
print("Image Processing ends")
    


