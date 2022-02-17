#!/usr/bin/env bash

apt update
apt install vim nano curl ansible ufw python3-pip python3-apt -yq
pip3 install pika