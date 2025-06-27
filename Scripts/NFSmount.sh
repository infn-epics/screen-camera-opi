#!/bin/bash
if ! grep -q 'sparcstorage' /etc/fstab ; then
    mkdir -p /nfs/data
    mkdir -p /nfs/autosave
    mkdir -p /nfs/config
    echo '#sparcstorage' >> /etc/fstab
    echo '192.168.197.157:/sparcstorage/space2/SparcData /nfs/data nfs defaults 0 0' >> /etc/fstab
    echo '192.168.197.157:/data_epik8s/autosave /nfs/autosave nfs defaults 0 0' >> /etc/fstab
    echo '192.168.197.157:/data_epik8s/config /nfs/config nfs defaults 0 0' >> /etc/fstab
    echo "nfs mounts created!"
else
    echo "nfs mounts already exist!"
fi
