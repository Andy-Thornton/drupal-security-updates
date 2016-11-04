#!/usr/bin/env python
import subprocess

# Store paths and connection info
sourcetree = "/home/flux/Projects/hackday"
gitlabapi = ""
drupalbootstrap = sourcetree + "/drupal/includes/bootstrap.inc"
rssDrupalCore = "http://drupal.org/security/rss.xml"
rssDrupalContrib = "http://drupal.org/security/contrib/rss.xml"

# Start with Drupal core
print("=" * 7) + " Drupal Core " + ("=" * 7)
with open(drupalbootstrap, 'r') as searchfile:
    for line in searchfile:
        if """define('VERSION',""" in line:
            drupalversion =  line.split("'")
            print "-- Drupal Core: " + drupalversion[3]

# Iterate modules ignoring core.
print("=" * 7) + " Contributed Modules " + ("=" * 7)

# Start with the drupal /modules directory as this is where RPM's install
# Exclude all files with package "Core"
rpmmodules = sourcetree + "drupal/modules"
print("--- Scanning " + rpmmodules + " directory for non core modules")
