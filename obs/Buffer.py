#!/usr/bin/env python
# title				: Next talk update for OBS
# description		: Displays current and next talk in OBS
# author			: DarkDrgn2k
# date				: 2018 06 26
# version			: 0.1
# usage				: python pyscript.py
# dependencies		: - Python 3.6 (https://www.python.org/)

import json
import obspython as obs
import os, time, datetime
import xml.etree.ElementTree as ET

try:
	from HTMLParser import HTMLParser
except ImportError:
	from html.parser import HTMLParser

working = True
enabled = True
check_frequency = 300
debug_mode = False

source_title=""
source_presenter=""
source_time=""
json_filename=""

# ------------------------------------------------------------
# OBS Script Functions
# ------------------------------------------------------------

def script_defaults(settings):
	global debug_mode
	if debug_mode: print("Calling defaults")

	global enabled
	global source_title
	global source_presenter
	global source_time
	global check_frequency
	global json_filename
	
	obs.obs_data_set_default_bool(settings, "enabled", enabled)
	obs.obs_data_set_default_int(settings, "check_frequency", check_frequency)	
	obs.obs_data_set_default_string(settings, "source_title", source_title)
	obs.obs_data_set_default_string(settings, "source_presenter", source_presenter)
	obs.obs_data_set_default_string(settings, "source_time", source_time)
	obs.obs_data_set_default_string(settings, "json_filename", json_filename)
	if debug_mode: print("defaults json_filename " + json_filename)
		

def script_description():
	global debug_mode
	if debug_mode: print("Calling description")

	return "<b>Buffer File</b>" + \
		"<hr>" + \
		"Updates text fields with current talk based on a json schedule." + \
		"<br/>" + \
		"<pre>[   {\n      \"title\":\"Registration and coffee\",\n      \"presenter\":\"Our Networks\",\n      \"startTime\":\"2018-06-25 08:30\",\n      \"endTime\":\"2018-06-25 09:00\"\n   }   \n]" + \
		"<br/><br/>" + \
		"<hr>"

def script_load(settings):
	global debug_mode
	if debug_mode: print("OBSBuffer Loaded script.")
	
def script_properties():
	global debug_mode
	if debug_mode: print("OBSBuffer Loaded properties.")

	props = obs.obs_properties_create()
	obs.obs_properties_add_bool(props, "enabled", "Enabled")
	obs.obs_properties_add_bool(props, "debug_mode", "Debug Mode")
	obs.obs_properties_add_int(props, "check_frequency", "Check frequency", 150, 10000, 100 )
	obs.obs_properties_add_text(props, "source_title", "Text Title", obs.OBS_TEXT_DEFAULT )
	obs.obs_properties_add_text(props, "source_presenter", "Text Presenter", obs.OBS_TEXT_DEFAULT )
	obs.obs_properties_add_text(props, "source_time", "Text Time", obs.OBS_TEXT_DEFAULT )
	obs.obs_properties_add_text(props, "json_filename", "Text Title", obs.OBS_TEXT_DEFAULT )

	
	return props

def script_save(settings):
	global debug_mode
	if debug_mode: print("OBSBuffer Saved properties.")

	script_update(settings)

def script_unload():
	global debug_mode
	if debug_mode: print("OBSBuffer Unloaded script.")
	
	obs.timer_remove(update_content)

def script_update(settings):
	global debug_mode
	if debug_mode: print("OBSBuffer Updated properties.")

	global enabled
	global display_text
	global check_frequency
	global source_presenter
	global source_time
	global json_filename
	global source_title
	global check_frequency
	
	if obs.obs_data_get_bool(settings, "enabled") is True:
		if (not enabled):
			if debug_mode: print("OBSBuffer Enabled buffer timer.")

		enabled = True
		obs.timer_add(update_content, check_frequency)
	else:
		if (enabled):
			if debug_mode: print("OBSBuffer Disabled buffer timer.")

		enabled = False
		obs.timer_remove(update_content)
			
	debug_mode = obs.obs_data_get_bool(settings, "debug_mode")
	source_presenter = obs.obs_data_get_string(settings, "source_presenter")
	source_title = obs.obs_data_get_string(settings, "source_title")
	source_time = obs.obs_data_get_string(settings, "source_time")
	check_frequency = obs.obs_data_get_int(settings, "check_frequency")
	json_filename = obs.obs_data_get_int(settings, "json_filename")


def update_content():
	global debug_mode
	global currentTalk
	global nextTalk

	#with open(json_filename, 'r') as myfile:
	with open("c:\\test\\test.json", 'r') as myfile:
		data=myfile.read()
	nextTalk=""
	data=json.loads(data)
	for value in data:
	
		#Format string from json into date/time for comparison
		value["startTime"]=datetime.datetime.strptime(value["startTime"], '%Y-%m-%d %H:%M')
		value["endTime"]=datetime.datetime.strptime(value["endTime"], '%Y-%m-%d %H:%M')
		
		#If no nextTalk set, set it to the first entry on the list
		if nextTalk=="":
			nextTalk=value
			
		# If Current Date is greater then value's start time but less then values end time, set it as current talk.
		if value["startTime"] < datetime.datetime.now() < value["endTime"]:
			currentTalk=value

		# If start time is less then the currently selected next talk 
		# Meaning it is no longer next because it started
		if nextTalk["startTime"] < datetime.datetime.now() :
			nextTalk=value

	#Update fields on OBS
	settings = obs.obs_data_create()
	obs.obs_data_set_string(settings, "text", currentTalk["title"])
	source = obs.obs_get_source_by_name(source_title)
	obs.obs_source_update(source, settings)
	obs.obs_data_release(settings)
	obs.obs_source_release(source)

	settings = obs.obs_data_create()
	obs.obs_data_set_string(settings, "text", currentTalk["presenter"])
	source = obs.obs_get_source_by_name(source_presenter)
	obs.obs_source_update(source, settings)
	obs.obs_data_release(settings)
	obs.obs_source_release(source)

	settings = obs.obs_data_create()
	obs.obs_data_set_string(settings, "text", datetime.datetime.strftime(currentTalk["startTime"], "%I:%M%p") + " - " +  datetime.datetime.strftime(currentTalk["endTime"], "%I:%M%p"))
	source = obs.obs_get_source_by_name(source_time)
	obs.obs_source_update(source, settings)
	obs.obs_data_release(settings)
	obs.obs_source_release(source)	
