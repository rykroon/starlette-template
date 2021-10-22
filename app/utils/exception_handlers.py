from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse


def http_exception_handler(request, exc):
    return JSONResponse({
        'error': exc.detail,
        'error_description': ''
    }, status_code=exc.status_code)


exception_handlers = {
    HTTPException: http_exception_handler
}