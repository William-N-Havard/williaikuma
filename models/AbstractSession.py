#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: AbstractSession.py (as part of project Williaikuma)
#   Created: 16/10/2022 16:34
#   Last Modified: 16/10/2022 16:34
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
import abc

from models.Tasks import TASKS
from models.utils import json_read, json_dump, now


class AbstractSession(abc.ABC):
    def __init__(self, name, path, data_path, speaker, task, last_access=now()):
        super(AbstractSession, self).__init__()

        # Default AbstractSession Metadata
        self.name = name
        self.path = path
        self.data_path = data_path
        self.speaker = speaker
        self.task = TASKS.from_string(task) if not isinstance(task, TASKS) else task
        self.last_access = now()

        # Metadata
        self.session_metadata_path = os.path.join(self.path, 'metadata_{}.json'.format(self.name))


    def start(self):
        try:
            self.data.load()
        except Exception as e:
            raise Exception(e)


    def previous(self):
        self.data.previous()
        self.update_current_data_item()


    def next(self):
        self.data.next()
        self.update_current_data_item()


    def override_index(self, value):
        self.data.index = value - 1
        self.update_current_data_item()

    @abc.abstractmethod
    def update_current_data_item(self):
        pass


    def save(self, other_metadata):
        if os.path.exists(self.session_metadata_path):
            existing_metadata = json_read(self.session_metadata_path)
        else:
            existing_metadata = False

        metadata = {
            'name': self.name,
            'path': self.path,
            'data_path': self.data_path,
            'speaker': self.speaker,
            'task': self.task.value,
            'last_access': now()
        }

        metadata.update(other_metadata)

        if existing_metadata:
            for k, v in metadata.items():
                if k == 'last_access': continue
                assert existing_metadata[k] == v, \
                    ValueError('Value between existing metadata file and '
                               'new metdata differ ({} v. {}'.format(
                        existing_metadata[k], v
                    ))
                if k not in metadata.keys():
                    metadata[k] = v

        json_dump(self.session_metadata_path, metadata)


    @staticmethod
    def read_metadata(metadata_file):
        return json_read(metadata_file)


    @classmethod
    @abc.abstractmethod
    def load(cls, session_json):
        pass
