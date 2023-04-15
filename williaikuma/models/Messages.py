#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

import babel

from williaikuma.models.defaults import DEFAULT_LANGUAGE


# /!\ If ANY string is modified here, whatever the modification, localisation will not work anymore.
# Hence, each string modification here implies regeneration .pot, .po, and .mo files.

class MSG(Enum):
    BUTTON_CANCEL  = "Cancel"
    BUTTON_DETELE  = "Delete"
    BUTTON_GO      = "Go"
    BUTTON_PLAY    = "Play"
    BUTTON_RECORD  = "Record"
    BUTTON_RESPEAK = "Respeak"

    ERROR_UNABLE_CREATE_SESSION    = "Couldn't create this session!"
    ERROR_UNABLE_GENERATE_TEXTGRID = "There was a problem when generating the TextGrid files."
    ERROR_UNABLE_OPEN_SESSION      = "Couldn't open this session!"
    ERROR_UNABLE_READ_RECORDING    = "There is a problem with this recording!"
    ERROR_UNABLE_SESSION_START     = "Unable to start the session!"
    ERROR_UNKNOWN                  = "Unknown error!"

    EXCEPT_INDEX_NEGATIVE    = "Index can't be negative ({})!"
    EXCEPT_INDEX_NOT_INTEGER = "Index can only be an integer!"
    EXCEPT_MISSING_LINE_SEP  = "' ## ' not found on line {}."
    EXCEPT_READING_WAVE_FILE = "Error while reading the WAVE file. {}"
    EXCEPT_UNKNOWN_TASK      = "Unknown type of task `{}`."
    EXCEPT_METADATA_MISMATCH = 'Value between existing metadata file and '\
                               'new metadata differ ({} v. {})'

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

    STATUS_SESSION = "Line: {} | Speaker: {} | Session: {}"
    STATUS_WAITING = "Waiting..."

    TEXT_EXPLANATION                   = "Create a new project or open an existing one."
    TEXT_FILES                         = "Files"
    TEXT_INFORMATION_GENERATE_TEXTGRID = "Done! ({} generated, {} failures)\n"
    TEXT_MISSING_ITEMS                 = "Missing items"
    TEXT_PROMPT_DELETE_RECORDING       = "Delete this recording?"
    TEXT_PROMPT_SPEAKER                = "Enter speaker's name"
    TEXT_PROMPT_CHANGE_LOCALE          = "The application will have to restart to apply the changes. Restart?"

    TITLE_CHOOSE_FILE                  = "Choose a file"
    TITLE_DELETE                       = "Delete"
    TITLE_ERROR                        = "Error!"
    TITLE_INFORMATION                  = "Information"

    def __str__(self):
        return gettext(str(self.value)) # noqa: Unresolved Reference
