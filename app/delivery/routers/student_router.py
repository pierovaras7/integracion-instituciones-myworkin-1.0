from fastapi import APIRouter, Request

from app.core.limiter import limiter
from app.config.di_student import register_student_use_case
from app.delivery.schemas.student_ulima_dto import StudentULimaDTO
from app.delivery.schemas.student_ucv_dto import StudentUCVDTO
from app.infrastructure.mapper.student_ulima_mapper import ulima_to_domain
from app.infrastructure.mapper.student_ucv_mapper import ucv_to_domain

router = APIRouter()

# -------------------------------------------------
# ULIMA
# -------------------------------------------------
@router.post("/students/ulima")
@limiter.limit("100/minute")
async def register_ulima_student(
    request: Request,
    body: StudentULimaDTO
):
    try:
        uc = register_student_use_case()
        result = uc.execute(ulima_to_domain(body))
        return {"status": result}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "error": str(e),
            "type": type(e).__name__
        }


# -------------------------------------------------
# UCV
# -------------------------------------------------
@router.post("/students/ucv")
@limiter.limit("10/minute")
def register_ucv_student(
    request: Request,
    body: StudentUCVDTO
):
    uc = register_student_use_case()
    return {"status": uc.execute(ucv_to_domain(body))}
