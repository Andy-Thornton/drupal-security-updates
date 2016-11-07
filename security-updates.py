#!/usr/bin/env python
import subprocess, os, sys
import colorama
from colorama import Fore, Back, Style

# Store paths and connection info
sourcetree = "/home/flux/Projects/hackday"
gitlabapi = ""
drupalbootstrap = sourcetree + "/drupal/includes/bootstrap.inc"
contrib = sourcetree + "/all/modules/contrib"
rpmmodules = sourcetree + "/drupal/modules"
rssDrupalCore = "http://drupal.org/security/rss.xml"
rssDrupalContrib = "http://drupal.org/security/contrib/rss.xml"
doAPI = "https://www.drupal.org/api-d7/node.json?type=project_module&field_project_machine_name="

# Start with Drupal core
print Fore.BLUE + ("=" * 7) + " Drupal Core " + ("=" * 7) + Style.RESET_ALL
print Fore.GREEN
with open(drupalbootstrap, 'r') as searchfile:
    for line in searchfile:
        if """define('VERSION',""" in line:
            drupalversion =  line.split("'")
            print "-- Drupal Core: " + drupalversion[3]
print Style.RESET_ALL

# Function to iterate through a module path and pull the version numbers
def modulelist(modpath):
    print Fore.BLUE + ("=" * 7) + " " + modpath + " " + ("=" * 7) + Style.RESET_ALL
    dirs = os.listdir(modpath)
    print Fore.GREEN
    for module in dirs:
        info = modpath  + "/" +  module + "/" + module + ".info"
        try:
            with open(info, 'r') as searchfile:
                for line in searchfile:
                    if """version = """ in line:
                        moduleversion = line.split("version =")
                        if not "VERSION" in moduleversion[1]:
                            print "-- " + module + " " + moduleversion[1].replace('\"','')
        except:
            pass
    print Style.RESET_ALL

modulelist(contrib)
modulelist(rpmmodules)
