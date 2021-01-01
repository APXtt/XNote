## 설명
## 윈도우의 와이파이 profile 파일을 수정해서 와이파이 설정에 접근한다.

import subprocess
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import re


## setting
filepath = 'C:\\Users\\gbytt\\Dropbox\\[A] 공유폴더\\[E] VScode\\WiPass\\'
finename = 'profile_1'

profile_name = 'HSP'
profile_hex = str(485350)
connectionType = 'ESS'
connectionMode = 'auto'
authentication = 'WPA2PSK'
encryption = 'AES'
useOneX = 'false'
keyType = 'PassPhrase'
protected = 'false'
keyMaterial = 'password'
enableRandomization = 'false'


## make profile.xml file
profile_WLANprofile = Element('WLANprofile')
profile_WLANprofile.attrib['xmlns'] = 'http://www.microsoft.com/networking/WLAN/profile/v1'
SubElement(profile_WLANprofile, 'name').text = profile_name
profile_profile_SSIDConfig = SubElement(profile_WLANprofile, 'SSIDConfig')
profile_SSID = SubElement(profile_profile_SSIDConfig, 'SSID')
SubElement(profile_SSID, 'hex').text = profile_hex
SubElement(profile_SSID, 'name').text = profile_name
SubElement(profile_WLANprofile, 'connectionType').text = connectionType
SubElement(profile_WLANprofile, 'connectionMode').text = connectionMode
profile_MSM = SubElement(profile_WLANprofile, 'MSM')
profile_security = SubElement(profile_MSM, 'security')
profile_authEncryption = SubElement(profile_security, 'authEncryption')
SubElement(profile_authEncryption, 'authentication').text = authentication
SubElement(profile_authEncryption, 'encryption').text = encryption
SubElement(profile_authEncryption, 'useOneX').text = useOneX
profile_sharedKey = SubElement(profile_security, 'sharedKey')
SubElement(profile_sharedKey, 'keyType').text = keyType
SubElement(profile_sharedKey, 'protected').text = protected
SubElement(profile_sharedKey, 'keyMaterial').text = keyMaterial
profile_MacRandomization = SubElement(profile_WLANprofile, 'MacRandomization')
profile_MacRandomization.attrib['xmlns'] = 'http://www.microsoft.com/networking/WLAN/profile/v3'
SubElement(profile_MacRandomization, 'enableRandomization').text = enableRandomization

def profile_tab(elem, level=0):
    i = "\n" + level*"   "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "   "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:  
            profile_tab(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i 
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

print(profile_WLANprofile.tail)
                
profile_tab(profile_WLANprofile)
profile_tree = ElementTree(profile_WLANprofile)
profile_tree.write(filepath + finename +'.xml')