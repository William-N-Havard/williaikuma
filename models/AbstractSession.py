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

from pkg_resources import parse_version
from models.Tasks import TASKS
from models.utils import json_read, json_dump, now, resolve_relative_path


class AbstractSession(abc.ABC):
    def __init__(self, name, path, data_path, speaker, task, version, last_access=now()):
        super(AbstractSession, self).__init__()

        # Default AbstractSession Metadata
        self.name = name

        self.path = path

        # Handle relative paths
        self._data_path = data_path

        self.speaker = speaker
        self.task = TASKS.from_string(task) if not isinstance(task, TASKS) else task
        self.last_access = now()
        self.version = version

        # Metadata
        self.session_metadata_path = os.path.join(self.path, 'metadata_{}.json'.format(self.name))

    @property
    def data_path(self):
        # Handle relative path for data paths
        #
        # Normally, this should never happen (the app always uses absolute paths when creating a session) but we
        # could encounter relative paths if the user changes the paths for some reason or another in the JSON
        # metadata file. This ensures the app will still be able to load the session's data.

        return resolve_relative_path(self.path, self._data_path)


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
            #'path': self._path,
            'data_path': self._data_path, # Put back the path we found in the metadata
            'speaker': self.speaker,
            'task': self.task.value,
            'last_access': now(),
            'version': self.version,
        }

        metadata.update(other_metadata)

        if existing_metadata:
            for k, v in metadata.items():
                if k in ['last_access', 'version']: continue
                assert existing_metadata.get(k, None) == v, \
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
    def load(cls, version, session_json):
        session_path, _ = os.path.split(session_json)
        session_metadata = json_read(session_json)

        parsed_session_version = parse_version(session_metadata.get('version', '0.0.0'))
        parsed_current_version = parse_version(version)

        # Update metadata
        if  parsed_session_version != parsed_current_version:
            if parsed_session_version <= parse_version('0.1.2'):
                if 'path' in session_metadata: session_metadata.pop('path')

        session_metadata['version'] = version

        return cls(path = session_path, **session_metadata)
