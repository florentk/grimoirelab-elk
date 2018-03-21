#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Gerrit Ocean feeder
#
# Copyright (C) 2015 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#   Alvaro del Castillo San Felix <acs@bitergia.com>
#

'''Gerrit Ocean feeder'''

from .elastic import ElasticOcean
from ..elastic_mapping import Mapping as BaseMapping


class Mapping(BaseMapping):

    @staticmethod
    def get_elastic_mappings(es_major):
        """Get Elasticsearch mapping.

        :param es_major: major version of Elasticsearch, as string
        :returns:        dictionary with a key, 'items', with the mapping
        """

        if es_major != '2':
            mapping = '''
             {
                "dynamic":true,
                "properties": {
                    "data": {
                        "properties": {
                            "commitMessage": {
                                "type": "text"
                            },
                            "comments": {
                                "properties": {
                                    "message": {
                                        "type": "text",
                                        "index": true
                                    }
                                }
                            },
                            "subject": {
                                "type": "text",
                                "index": true
                            },
                            "patchSets": {
                                "properties": {
                                    "approvals": {
                                        "properties": {
                                            "description": {
                                                "type": "text",
                                                "index": true
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            '''

        else:
            mapping = '''
             {
                "dynamic":true,
                "properties": {
                    "data": {
                        "properties": {
                            "commitMessage": {
                                "type": "string"
                            },
                            "comments": {
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "index": "anaylzed"
                                    }
                                }
                            },
                            "subject": {
                                "type": "string",
                                "index": "anaylzed"
                            },
                            ,
                            "patchSets": {
                                "properties": {
                                    "approvals": {
                                        "properties": {
                                            "description": {
                                                "type": "string",
                                                "index": "anaylzed"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            '''

        return {"items": mapping}


class GerritOcean(ElasticOcean):

    mapping = Mapping