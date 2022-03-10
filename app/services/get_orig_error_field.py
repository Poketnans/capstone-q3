from sqlalchemy.exc import IntegrityError


def get_orig_error_field(error: IntegrityError):
    '''
        Resgata o campo associado ao erro de integridade gerado.
    '''

    err_msg = str(error.orig)

    field_associated = err_msg.split("Key")[1].split("=")[0][2:-1]

    return field_associated
