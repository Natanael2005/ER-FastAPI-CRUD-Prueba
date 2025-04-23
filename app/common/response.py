# app/common/response.py
from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel
from app.common.messages import SUCCESS_OPERATION

# Definimos un tipo genérico para el payload
PayloadType = TypeVar("PayloadType")

class ResponseModel(GenericModel, Generic[PayloadType]):
    """
    Modelo de respuesta genérico con tres campos:
      - ok: indica si la operación fue exitosa
      - message: mensaje de resultado
      - payload: datos devueltos (cada endpoint decide su tipo)
    """
    ok: bool
    message: str
    payload: Optional[PayloadType]


def success_response(
    payload: PayloadType,
    message: str = SUCCESS_OPERATION
) -> ResponseModel[PayloadType]:
    """
    Construye un ResponseModel de éxito.
    """
    return ResponseModel(
        ok=True,
        message=message,
        payload=payload
    )


def error_response(
    message: str,
    payload: Any = None
) -> ResponseModel[Any]:
    """
    Construye un ResponseModel de error.
    """
    return ResponseModel(
        ok=False,
        message=message,
        payload=payload
    )