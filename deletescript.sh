#!/bin/bash
while read -r item
do
    salt-key -yd "${item}"
    etcdctl ls --recursive /store/"${item}" >> /tmp/jsarwar_script.output
    etcdctl rm --recursive /store/"${item}"
    echo "Removed ${item}"
    salt-cloud -d ${item}
done < host_file.txt
