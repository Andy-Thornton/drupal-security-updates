#!/usr/bin/env python
import subprocess

#Store paths and connection info
sourcetree = "/home/flux/Projects/hackday"
gitlabapi = ""
drupalbootstrap = sourcetree + "/drupal/includes/bootstrap.inc"
rssDrupalCore = "http://drupal.org/security/rss.xml"
rssDrupalContrib = "http://drupal.org/security/contrib/rss.xml"

#Start with Drupal core
print("\033[1;34;40m") + "======= Drupal Core ========\033[0;37;40m"
with open(drupalbootstrap, 'r') as searchfile:
    for line in searchfile:
        if """define('VERSION',""" in line:
            drupalversion =  line.split("'")
            print "Drupal Core = " + drupalversion[3]

#Iterate modules ignoring core.
print("=" * 7) + " Contributed Modules " + ("=" * 7)
