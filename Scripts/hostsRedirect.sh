#!/bin/bash
if ! grep -q 'argocd' /etc/hosts ; then
    echo '#argocd and kubernates dashboard' >> /etc/hosts
    echo '10.10.6.18 dashboard.da' >> /etc/hosts
    echo '10.10.6.18 argocd.da' >> /etc/hosts
    echo '10.10.6.18 sparc-archiver.da' >> /etc/hosts
    echo '10.10.6.18 sparc-console.da' >> /etc/hosts
    echo "hosts updated!"
else
    echo "hosts already exist!"
fi
