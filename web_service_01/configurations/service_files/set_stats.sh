#!/bin/bash

ip addr | grep inet > /home/service/service_stats.log

chmod 777 /home/service/service_stats.log
