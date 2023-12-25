import requests
from typing import Optional, Any
from requests.models import Response

class DockerException(Exception): ...

def create_api_error_from_http_exception(e: Exception) -> None: ...

class APIError(requests.exceptions.HTTPError, DockerException):
    response: Optional[Response]
    explanation: Optional[str]
    def __init__(
        self,
        message: str,
        response: Optional[Response] = None,
        explanation: Optional[str] = None,
    ) -> None: ...
    @property
    def status_code(self) -> int: ...
    def is_error(self) -> bool: ...
    def is_client_error(self) -> bool: ...
    def is_server_error(self) -> bool: ...

class NotFound(APIError): ...
class ImageNotFound(NotFound): ...
class InvalidVersion(DockerException): ...
class InvalidRepository(DockerException): ...
class InvalidConfigFile(DockerException): ...
class InvalidArgument(DockerException): ...
class DeprecatedMethod(DockerException): ...

class TLSParameterError(DockerException):
    msg: str
    def __init__(self, msg: str) -> None: ...

class NullResource(DockerException, ValueError): ...

class ContainerError(DockerException):
    container: Any
    exit_status: int
    command: str
    image: str
    stderr: str
    def __init__(
        self, container: Any, exit_status: int, command: str, image: str, stderr: str
    ) -> None: ...

class StreamParseError(RuntimeError):
    msg: str
    def __init__(self, reason: str) -> None: ...

class BuildError(DockerException):
    msg: str
    build_log: str
    def __init__(self, reason: str, build_log: str) -> None: ...

class ImageLoadError(DockerException): ...

def create_unexpected_kwargs_error(name: str, kwargs: dict[str, Any]) -> None: ...

class MissingContextParameter(DockerException):
    param: str
    def __init__(self, param: str) -> None: ...

class ContextAlreadyExists(DockerException):
    name: str
    def __init__(self, name: str) -> None: ...

class ContextException(DockerException):
    msg: str
    def __init__(self, msg: str) -> None: ...

class ContextNotFound(DockerException):
    name: str
    def __init__(self, name: str) -> None: ...
