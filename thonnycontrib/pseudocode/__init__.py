
# Imports

import os.path

from thonny import get_workbench
from thonny.ui_utils import select_sequence

from .utils import get_user_set_thonny_ui_language_code
from .plugin import annotate_command_enabled, execute_annotate_command

# Constants

COMMAND_LABELS = {
    'en': 'Explain with pseudocode',
    'fr': 'Expliquer avec du pseudocode'
}

# Functions

def load_plugin():
    language = get_user_set_thonny_ui_language_code()

    icon_path = os.path.join(os.path.dirname(__file__), 'res', 'icon.png')
    get_workbench().add_command(
        command_id='annotate_with_pseudocode',
        menu_name='tools',
        command_label=COMMAND_LABELS[language],
        handler=execute_annotate_command,
        tester=annotate_command_enabled,
        default_sequence=select_sequence('<Control-e>', '<Command-e>'),
        group=120,
        image=icon_path,
        caption=COMMAND_LABELS[language],
        include_in_toolbar=True
    )
