
# Imports

from thonny import get_workbench
from tkinter.messagebox import showerror

from .pytopseu.pytopseu.common import \
    python_pseudocode_format, \
    language_pseudocode_dictionaries, \
    strip_annotations
from .pytopseu.pytopseu import annotate_code

from .utils import \
    get_user_set_thonny_ui_language_code, \
    get_error_title, \
    get_error_message

# Functions

def annotate_command_enabled():
    code = _get_current_code()
    return code is not None and code.strip() != ''

def _get_current_code() -> str:
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return ''
    return editor.get_code_view().text.get('1.0', 'end-1c')

def _set_code(code):
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return
    text_widget = editor.get_code_view().text
    text_widget.delete('1.0', 'end')
    text_widget.insert('1.0', code)

def execute_annotate_command():
    language_code = get_user_set_thonny_ui_language_code()
    pseudocode_dictionary = language_pseudocode_dictionaries[language_code]
    current_code = _get_current_code()

    annotation_result = annotate_code(
        current_code,
        python_pseudocode_format,
        pseudocode_dictionary
    )

    if annotation_result is None:
        showerror(
            get_error_title(language_code),
            get_error_message(language_code),
            parent=get_workbench()
        )
        return

    annotated_code = "\n".join(annotation_result.output)

    if current_code == annotated_code:
        _set_code(strip_annotations(current_code, pseudocode_dictionary))
    else:
        _set_code(annotated_code)
