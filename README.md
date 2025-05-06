# audio-swapper
Audio output device switcher for Linux

Audio-swapper identifies the currently running audio output device and swaps it to an alternative.

This script assumes two audio output options, which are semi-hardcoded. You'll need to identify your own devices with `pactl list sinks` and modify the script with your own Sinks. My devices happen to be labeled Sink#55 and Sink#57. 
With the script switching your devices correctly just assign a hotkey to it and you're good to go. 
