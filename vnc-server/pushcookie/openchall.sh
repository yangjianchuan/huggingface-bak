#!/bin/bash
# Author : Bing
# Script follows here:

# Define a function to load a web page using chromium browser
load_page() {
  # The first argument is the web page url
  url=$1
  # Open the url in a new tab of chromium browser
  chromium --new-tab $url --window-position=0,0 --window-size=600,600

}

# Load the first web page
load_page "https://www.bing.com/turing/captcha/challenge"


