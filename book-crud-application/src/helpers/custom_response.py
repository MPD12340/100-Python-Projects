from typing import List, Union, Any, Dict
from books import ResponseModel
def custom_response(
    success: bool,
    data: Union[Dict[str, Any], List[Any], None] = None,
    error: Union[str, None] = None,
):
    return ResponseModel(success=success, data=data, error=error)