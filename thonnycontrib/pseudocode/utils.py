
# Imports

from thonny import get_workbench

# Functions

def get_user_set_thonny_ui_language_code():
    return get_workbench().get_option('general.language')[0:2] or 'en'

def get_error_title(language_code: str) -> str:
    match language_code:
        case 'fr': return 'Erreur'

    return 'Error'

def get_error_message(language_code: str) -> str:
    match language_code:
        case 'fr':
            return 'Explication du code échouée ! Veuillez vértifier si votre code contient des erreurs de syntaxe et réessayer.'

    return 'Could not explain code! Please check for syntax errors and try again.'
