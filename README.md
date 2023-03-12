# Datacenter-Power-Assessment-Tool
## What it is
A small script that makes an assessment of all the power and heat generated from your server racks based on what equipment is in them. The features of this are not terribly robust, but it should be more than enough data to run a CFD analysis or to understand your server rooms current PUE.

## How to use
Currently, you'll need to place all the files in the same directory and edit the "rackTemplate.json" to fit your racks needs. When creating new racks, stick the demonstrated format of "Rack_n", with n being the current rack you are describing. For an example of the data that you will be getting, look through "rackAssessment.json".

If you would like to go through and fill out all the information manually, open "assessment.py" and change the "mode" variable to 0. This will allow you to create all of the data in "rackTemplate.json" manually, line by line.

## Notes
I plan on updating this script in the future so it can be run as a command in terminal with additional options for different file input/output. But these updates will come when I have time.
