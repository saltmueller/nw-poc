#!/usr/bin/env python
#
#
#
#  Copyright (c) Stephan Altmueller
#  Copyright (c) 2011-2013 Corey Goldberg (http://goldb.org)
#
#  This file is part of linux-metrics
#
#  License :: OSI Approved :: MIT License:
#      http://www.opensource.org/licenses/mit-license
# 
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#


""" example usage of linux-metrics """


import linux_metrics as lm
import time
import mosquitto

def send_metrics():
    client = mosquitto.Mosquitto("metrics-client")
    client.connect("localhost")

    while True:
        result = ""

        # cpu
        result += 'procs running: %d\n' % lm.cpu_stat.procs_running()
        cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
        result += 'cpu utilization: %.2f%%\n' % (100 - cpu_pcts['idle']) 
        
        # disk
        result += 'disk busy: %s%%\n' % lm.disk_stat.disk_busy('sda', sample_duration=1)
        r, w = lm.disk_stat.disk_reads_writes('sda1')    
        result += 'disk reads: %s\n' % r
        result += 'disk writes: %s\n' % w
        
        # memory
        used, total, _, _, _, _ = lm.mem_stat.mem_stats()
        result += 'mem used: %s\n' % used
        result += 'mem total: %s\n' % total

        # network
        rx_bits, tx_bits = lm.net_stat.rx_tx_bits('wlan3')   
        result += 'net bits received: %s\n' % rx_bits
        result += 'net bits sent: %s\n' % tx_bits 

        client.publish("linux/metrics", result)
        client.loop(0)

        # time.sleep(0.1)


if __name__ == '__main__':   
    send_metrics()

