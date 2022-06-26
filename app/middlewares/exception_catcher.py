"""App exception catcher."""
import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.core import errors


async def exception_catcher(request: Request, call_next):
    """
    Global exception handler for app.

    Add errors as needed otherwise errors will be generalized into a 500
    server error .
    """
    try:
        return await call_next(request)
    except errors.WritePermissionError as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.RecordNotFoundError as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.ModelNotFoundError as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidEnvironment as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidUserId as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.FilterSchemasMismatch as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidFilterClass as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidOrderField as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidOrderType as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.InvalidTestingEnvironment as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except errors.DuplicateObjectError as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    except IntegrityError as e:
        return JSONResponse(
            status_code=500,
            content={"detail": f"orig: '{e.orig}', statment: '{e.statement}'"},
        )
    except Exception as e:
        print(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)},
        )
