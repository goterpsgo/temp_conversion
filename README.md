# Heat And Temperature Conversion Sample

## Overview
This is some sample software to demonstrate:
 * How to create an object-oriented Python script
 * Use pytest to verify the class and its methods do what they're supposed to do 

## Installation
The steps below should be applicable to most platforms. This sample was written in Win64; your experience may vary slightly.
1. Install Python to your local environment. This sample was written using Python v3.6/Win64.
2. Create a directory for housing this codebase. Once done, run `virtualenv env` to create a Python environment local to the project.
3. Enable the environment: `source env/Scripts/activate`
    * NOTE: the `Scripts` subdirectory is used in Windows-based Python installations; your installation may not have it.
4. Use `pip` to install all dependencies: `pip install -r requirements.txt`

## Running the Software
There are two ways to run the software sample.
1. You can run the script directly. Call the script and pass the appropriate parameters.
    * You can get help by using the `-h` flag: `./temp_conversion.py -h`
    * An example of running the script and passing parameters: `./temp_conversion.py -i "84.2 fahrenheit" -u rankine -r 543.5`; the script will respond with a `correct` output.
    * An example of running the script and passing parameters: `./temp_conversion.py -i "317.33 kelvin" -u fahrenheit -r 110.5`; the script will respond with an `incorrect` output.
2. You can also use the `pytest` utility and it'll run a number of unit tests to verify proper behavior; run `./pytest` at the prompt.

## CI Pipeline integration
Integration with a CI pipeline would require the use of a descriptor file to describe how to set up the environment and run the tests. Some examples of how this can be done are:
* in Travis CI:
```
# .travis.yml
language: python
script:
    - python -m pytest -v
```
* in Gitlab CI:
```
# .gitlab-ci.yml
before_script:
    - pip install -r requirements.txt
    
stages:
    - test
   
test_suite:
    stage: test
    script: pyteset -q temp_conv_test.py
```
