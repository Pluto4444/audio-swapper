#!/usr/bin/python
import subprocess


sink55 = subprocess.check_output("pactl list sinks | grep -A 3 -i 'sink #55'", shell=True, universal_newlines=True)
sink57 = subprocess.check_output("pactl list sinks | grep -A 3 -i 'sink #57'", shell=True, universal_newlines=True)
sink55name = sink55.splitlines()[2].split()[1]
sink57name = sink57.splitlines()[2].split()[1]



if "RUNNING" in sink55:
	subprocess.run(['pactl', 'set-default-sink', sink57name])
else:
	subprocess.run(['pactl', 'set-default-sink', sink55name])

