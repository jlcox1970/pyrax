#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c)2013 Rackspace US, Inc.

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from __future__ import print_function

import os
import sys
import pyrax
from pyrax import utils

f=open(os.devnull, 'w')

sys.stderr = f



region=sys.argv[1]

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file ,region=region)
cnw = pyrax.cloud_networks

# List initial status
nets = cnw.list()
for net in nets:
    print("Network: %s; cidr=%s; id=%s" % (net.label, net.cidr, net.id))
print()

