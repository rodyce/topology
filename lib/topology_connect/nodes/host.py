# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_connect base node module.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from logging import getLogger

from ..node import ConnectNode
from ..shell import SshShell


log = getLogger(__name__)


class HostNode(ConnectNode):
    """
    FIXME: Document.
    """
    def __init__(self, identifier, **kwargs):
        super(HostNode, self).__init__(identifier, **kwargs)
        self._shells['bash'] = SshShell('(^|\n)root@.*:.*# ')


class UncheckedHostNode(ConnectNode):
    """
    FIXME: Document.
    """
    def __init__(self, identifier, **kwargs):
        super(UncheckedHostNode, self).__init__(identifier, **kwargs)
        self._shells['bash'] = SshShell(
            '(^|\n)root@.*:.*# ',
            options=['StrictHostKeyChecking=no']
        )


__all__ = ['HostNode', 'UncheckedHostNode']
