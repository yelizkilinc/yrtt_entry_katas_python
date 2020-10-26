# Python Entry Katas

This repository contains tasks for you to undertake to secure and prepare you for a place on the Tech Returners course. We will be checking over your solutions, so please ensure you push to GitHub regularly (little and often is key). 

You may find these exercises challenging but they give you the opportunity to showcase your growth mindset and commitment to learning, programming, and trying your best. You can always come to us if you are having any trouble.

If you need reminding of any key Python concepts to solve these tasks we recommend the 'Codecademy: Learn Python 3' (free) course: https://www.codecademy.com/learn/learn-python-3

**NOTE: You are not required to purchase any PRO content from Codecademy.**

We also recommend this visual guide if you are unfamiliar with GitHub: https://agripongit.vincenttunru.com/

Remember to break down problems to help you solve them and that Google is your friend!

### Instructions

To complete these challenges you will need to have Python (version 3.3 onwards) installed on your computer.

Follow this link to download and install Python for your laptop:

https://www.python.org/downloads/

Once you've got Python installed you can make a start!

### Completing the tasks

Firstly you will need to [fork this GitHub repository](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) to your own GitHub profile and then clone your forked repository down to your laptop.

**NOTE: You do NOT have to submit Pull Requests to us.**

After cloning this repository, it is recommended to enable a virtual environment and install dependencies.

If you haven't got virtualenv installed you can install it by running:

    sudo pip3 install virtualenv

Then proceed to create the environment and install the dependencies

    virtualenv tech_returners_tasks -p python3

    source tech_returners_tasks/bin/activate

    pip3 install -r requirements.txt

If you look inside the **tasks** directory you will find a file of functions to implement.

To understand how these functions work, take a look in the corresponding test file where the desired functionality is described.

To run the tests, run

    pytest

Work through each test 1 by 1 until you have them all passing. Initially, you'll have a lot of failing tests and a lot of output on the console. To focus on a single test, you can run specific tests such as:
    
    pytest tests/test_exercise001.py

# The tasks

You can see the first task in [exercise001.py](./tasks/exercise001.py)
