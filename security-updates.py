#!/usr/bin/env python
import subprocess, os, sys
import colorama
from colorama import Fore, Back, Style

# Store paths and connection info
sourcetree = "/home/flux/Projects/hackday"
gitlabapi = ""
drupalbootstrap = sourcetree + "/drupal/includes/bootstrap.inc"
contrib = sourcetree + "/all/modules/contrib"
rssDrupalCore = "http://drupal.org/security/rss.xml"
rssDrupalContrib = "http://drupal.org/security/contrib/rss.xml"

# Start with Drupal core
print Fore.BLUE + ("=" * 7) + " Drupal Core " + ("=" * 7) + Style.RESET_ALL
print Fore.GREEN
with open(drupalbootstrap, 'r') as searchfile:
    for line in searchfile:
        if """define('VERSION',""" in line:
            drupalversion =  line.split("'")
            print "-- Drupal Core: " + drupalversion[3]
print Style.RESET_ALL

# Iterate modules ignoring core.
print Fore.BLUE + ("=" * 7) + " Contributed Modules under /modules " + ("=" * 7) + Style.RESET_ALL

# Start with the drupal /modules directory as this is where RPM's install
# TODO: Exclude all files with package "Core"
rpmmodules = sourcetree + "/drupal/modules"
dirs = os.listdir(rpmmodules)
print Fore.GREEN
for module in dirs:
    info = sourcetree + "/drupal/modules/" + module + "/" + module + ".info"
    try:
        with open(info, 'r') as searchfile:
            for line in searchfile:
                if """version = """ in line:
                    moduleversion = line.split("version =")
                    if not "VERSION" in moduleversion[1]:
                        if moduleversion[1] <> "VERSION":
                            print "-- " + module + " " + moduleversion[1]
    except:
        pass
print Style.RESET_ALL

# Now look at the contrib folder
print Fore.BLUE + ("=" * 7) + " Contributed Modules under /all/modules/contrib "  + ("=" * 7) + Style.RESET_ALL
rpmmodules = contrib
dirs = os.listdir(rpmmodules)
print Fore.GREEN
for module in dirs:
    info = contrib  + "/" +  module + "/" + module + ".info"
    try:
        with open(info, 'r') as searchfile:
            for line in searchfile:
                if """version = """ in line:
                    moduleversion = line.split("version =")
                    if not "VERSION" in moduleversion[1]:
                        print "-- " + module + " " + moduleversion[1]
    except:
        pass
print Style.RESET_ALL
