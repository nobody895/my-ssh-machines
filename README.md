# my-ssh-machines
Simple Flask app for managing ssh machines

# Lab setup
The application is running on a raspberry pi, constantly on.
A table contains all the hosts defined in hosts (routes.py).
Each host has 2 actions: wakeonlan and hibernate.
The host machine will execute wakeonlan on pressing the Wake button, or hibernate on Hibernate button.
Wake (wakepc) is a shell script on the path of host machine.
Hibernate will do ssh to the target host and execute the hibernate script.
