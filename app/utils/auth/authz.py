from starlette.authentication import requires


is_authenticated = requires('authenticated')
