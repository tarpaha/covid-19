# covid-19

## Description
Draws graph of infection cases with logistical curve approximation and inflection point on latest infection data from Johns Hopkins
## Requirements
* windows or something that can run CMD file (bash file is trivial and will be added later)
* wget
* python3 with numpy, scipy and matplotlib
## How to run
Run `process.cmd`, it will:
* Download latest infection cases from https://github.com/CSSEGISandData/COVID-19
* Filter country
* Make graph with logistical curve approximation, inflection point and store it in PNG image
## Example
<img src="images/example.png"/>
