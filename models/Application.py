#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Application.py (as part of project Williaikuma)
#   Created: 24/10/2022 00:22
#   Last Modified: 24/10/2022 00:22
# -----------------------------------------------------------------------------
#   Author: William N. Havard
#           Postdoctoral Researcher
#
#   Mail  : william.havard@ens.fr / william.havard@gmail.com
#  
#   Institution: ENS / Laboratoire de Sciences Cognitives et Psycholinguistique
#
# ------------------------------------------------------------------------------
#   Description: 
#       • 
# -----------------------------------------------------------------------------

import os
from datetime import datetime

from models.Session import Session
from models.utils import json_dump, json_read

class Application(object):
    def __init__(self, version):
        super(Application, self).__init__()

        self.name = "Williaikuma"
        self.version = version

        # Session
        self.session = None

        # Other
        self._config_file = '.williaikuma.json'
        self._config = self._read_config()
        self._session_path = self.config.get('session_path', os.path.realpath('sessions'))


    @property
    def config(self):
        return self._config

    @property
    def session_path(self):
        return os.path.realpath(self._session_path)

    @session_path.setter
    def session_path(self, value):
        self._session_path = os.path.realpath(value)
        self.update_config(session_path=self._session_path)

    @property
    def recent_sessions(self):
        return [(name, path) for name, path, *_ in self.config['recent']]


    def reset_recent_sessions(self):
        self.config['recent'] = []
        self.update_config()

    #
    #   Session handler
    #
    def session_load(self, session_json):
        try:
            self.session = Session.load(session_json=session_json,
                                        version=self.version)
        except Exception as e:
            raise Exception(e)

    def session_init(self, **kwargs):
        try:
            self.session = Session.init(**kwargs, version=self.version)
        except Exception as e:
            raise Exception(e)

    def session_start(self):
        self.update_config(recent=self.session)

        try:
            self.session.start()
        except Exception as e:
            raise Exception(e)

    #
    #   Application configuration
    #
    def _read_config(self):
        if not os.path.exists(self._config_file):
            json_dump(self._config_file, {
                "recent": []
            })

        config = json_read(self._config_file)
        config['recent'] = [[name, path, date] for name, path, date in config['recent'] if os.path.exists(path)]
        config['recent'] = list(sorted(config['recent'],
                                       key=lambda tup: datetime.strptime(tup[-1], "%d/%m/%Y %H:%M:%S"), reverse=True))
        json_dump(self._config_file, config)

        return config

    def update_config(self, **kwargs):
        config = self.config
        for k, v in kwargs.items():
            if k == "recent":
                cur_sess = v
                config.setdefault(k, [])
                recent = [cur_sess.name, cur_sess.session_metadata_path, cur_sess.last_access]

                recent_names = [name for name, _, _ in config[k]]
                if cur_sess.name not in recent_names:
                    config[k].insert(0, recent)
                else:
                    idx = recent_names.index(cur_sess.name)
                    config[k][idx][-1] = cur_sess.last_access

                config[k] = sorted(config[k][:5],
                                   key=lambda tup: datetime.strptime(tup[-1], "%d/%m/%Y %H:%M:%S"), reverse=True)
            else:
                config[k] = v
        json_dump(self._config_file, config)
