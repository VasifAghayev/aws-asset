## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Prerequisites](#prerequisites) 
* [Usage example](#usage-example)
* [Report](#report)

## General info
This program is designed to automatically create reports in xlsx format, based on the output of [awless](https://github.com/wallix/awless) program (**awless list**)

## Technologies
Program is created and tested with:
* Python version: 3.6 (3.6.3)

There are two versions of the program:
* awless.py
* awless_v2.py

**awless.py** program requires only one input – aws profile name aka aws account.
   - **Pros:** one run for each account. Covers all regions.
   - **Cons:** execution time is much longer.

**awless_v2.py** program requires two inputs - region name and aws profile name (aka aws account) - and should be rerun each time for new region.
   - **Pros:** execution time is accordingly less.
   - **Cons:** multiple reruns per regions for each account.
	
## Prerequisites
To run this program:
1. Install Python version 3.6 and pip
2. Install [awless](https://github.com/wallix/awless/releases)
3. Install **awscli**
```
pip install awscli --upgrade
```
4. Install requirements
```
pip install -r requirements.txt
```
5. Configure each aws account with aws cli. For consitency, profile name should be identical to aws account name.
 ```
aws configure --profile [profile_name]
```

## Usage example
awless.py:
 
![Alt text](/screens/awless1.JPG?raw=true "awless Example")

awless_v2.py:

![Alt text](/screens/awless2.JPG?raw=true "awless-v2 Example")

## Report
