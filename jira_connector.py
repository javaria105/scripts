#!/bin/python

'''
	Salt Script for exposing formatted pillar data for Jira
'''

# Import Flask
from flask import Flask, jsonify
app = Flask(__name__)
log = app.logger


# Import Salt Configs
import salt.config
import salt.runner


#### GLOBAL VARS ####
PORT = "5000"
IP = "0.0.0.0"


# Retrieve Master Config
opts = salt.config.master_config('/etc/salt/master')
	

# Create Runner Client 
runner = salt.runner.RunnerClient(opts)


@app.route("/")
def get_hostnames():
	hostnames = maintain_hostnames()
	return jsonify(hostnames)


# Upon Request Update Hostnames
def maintain_hostnames(): 
	# Run Cache.Pillar to retrieve Pillar information
	pillars = runner.cmd('cache.pillar', print_event=False)

	hostnames = list()

	# Transform pillar to Jira Format
	for index, (key, value) in enumerate(pillars.iteritems()):
		hostnames.append({
			"id": index,
			"host": key,
			"senv": value.get('senv', 'unknown'),
			"role": value.get('role', 'unknown'),
			"contact": value.get('contact', 'unkown')
		})

	return { "machines" : hostnames }


def start():
	app.run(host=IP, port=PORT)


if __name__ == "__main__":
	app.run(host=IP, port=PORT)
