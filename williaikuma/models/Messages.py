#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

import babel

from williaikuma.models.defaults import DEFAULT_LANGUAGE
from williaikuma.utilities.FrozenEnum import FrozenEnum


# /!\ If ANY string is modified here, whatever the modification, localisation will not work anymore.
#     Hence, each string modification here implies regenerating the .pot, .po, and .mo files.
class MSG(Enum, metaclass=FrozenEnum):
    BUTTON_CANCEL  = "Cancel"
    BUTTON_DETELE  = "Delete"
    BUTTON_GO      = "Go"
    BUTTON_PLAY    = "Play"
    BUTTON_RECORD  = "Record"
    BUTTON_RESPEAK = "Respeak"

    ERROR_UNABLE_CREATE_SESSION    = "Couldn't create this session!\n{}"
    ERROR_UNABLE_GENERATE_TEXTGRID = "There was a problem when generating the TextGrid files."
    ERROR_UNABLE_OPEN_SESSION      = "Couldn't open this session!"
    ERROR_UNABLE_READ_RECORDING    = "There is a problem with this recording!"
    ERROR_UNABLE_SESSION_START     = "Unable to start the session!\n{}"
    ERROR_UNKNOWN                  = "Unknown error!"

    EXCEPT_INDEX_NEGATIVE    = "Index can't be negative ({})!"
    EXCEPT_FILE_TYPES        = "Unknown file type (Accepted types: {})!"
    EXCEPT_INDEX_NOT_INTEGER = "Index can only be an integer!"
    EXCEPT_MISSING_LINE_SEP  = "' ## ' not found on line {}."
    EXCEPT_READING_WAVE_FILE = "Error while reading the WAVE file. {}"
    EXCEPT_UNKNOWN_TASK      = "Unknown type of task `{}`."
    EXCEPT_METADATA_MISMATCH = 'Value between existing metadata file and '\
                               'new metadata differ ({} v. {})'
    EXCEPT_CSV_FILE          = "Cannot read CSV file! Make sure field are encloded in `\"`"
    EXCEPT_CSV_COLUMN        = "Column 'sentence' and/or 'sentence_id' not found in CSV"

    MENU_DATA                 = "Data"
    MENU_DEFAULT_SESSION_DIR  = "Default Session Directory"
    MENU_EXIT                 = "Exit"
    MENU_FILE                 = "File"
    MENU_GENERATE_TEXTGRID    = "Generate TextGrid"
    MENU_LANGUAGE             = "Language"
    MENU_LANGUAGE_DEFAULT     = "Default ({})".format(babel.Locale.parse(DEFAULT_LANGUAGE).get_language_name())
    MENU_MISSING_ITEMS        = "View Missing Items"
    MENU_NEW                  = "New"
    MENU_NEW_RESPEAKING       = "New Respeaking"
    MENU_NEW_TEXT_ELICITATION = "New Text Elicitation"
    MENU_NONE                 = "None"
    MENU_OPEN                 = "Open"
    MENU_PREFERENCES          = "Preferences"
    MENU_RECENT               = "Recent"
    MENU_RESET                = "Reset"
    MENU_VERSION              = "Version"

    STATUS_SESSION = "Line: {} | Speaker: {} | Session: {}"
    STATUS_WAITING = "Waiting..."

    TEXT_EXPLANATION                   = "Create a new project or open an existing one."
    TEXT_FILES                         = "Files"
    TEXT_INFORMATION_GENERATE_TEXTGRID = "Done! ({} generated, {} failures)\n"
    TEXT_MISSING_ITEMS                 = "Missing items"
    TEXT_PROMPT_DELETE_RECORDING       = "Delete this recording?"
    TEXT_PROMPT_SPEAKER                = "Enter speaker's name"
    TEXT_PROMPT_CHANGE_LOCALE          = "The application will have to restart to apply the changes. Restart?"
    TEXT_VERSION                       = "Version: {}"

    TITLE_CHOOSE_FILE                  = "Choose a file"
    TITLE_DELETE                       = "Delete"
    TITLE_ERROR                        = "Error!"
    TITLE_INFORMATION                  = "Information"

    def _accessed(self):
        # This function has two roles:
        #   * it is called when a member of the enumeration is accessed
        #     which allows us to translate the text using gettext.gettext
        #   * it only returns the value of the member of the class instead of an Enum object.
        #     This allows to directly access the value without having to do item.value when called
        #     and allows us to directly have access to the string value without having to use the
        #     str() function on the class member (allowing to directly format the string using str.format())
        return gettext(self.value) # noqa: Unresolved reference 'gettext'


    @classmethod
    def values(cls):
        return (getattr(o, 'value') for o in list(cls))