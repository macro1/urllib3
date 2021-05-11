# For backwards compatibility, provide imports that used to be here.
from .connection import is_connection_dropped
from .request import SKIP_HEADER, SKIPPABLE_HEADERS, make_headers
from .response import is_fp_closed
from .retry import Retry
from .ssl_ import (
    ALPN_PROTOCOLS,
    HAS_SNI,
    IS_PYOPENSSL,
    IS_SECURETRANSPORT,
    PROTOCOL_TLS,
    SSLContext,
    assert_fingerprint,
    resolve_cert_reqs,
    resolve_ssl_version,
    ssl_wrap_socket,
)
from .timeout import Timeout
from .url import Url, parse_url
from .wait import wait_for_read, wait_for_write

__all__ = (
    "HAS_SNI",
    "IS_PYOPENSSL",
    "IS_SECURETRANSPORT",
    "SSLContext",
    "PROTOCOL_TLS",
    "ALPN_PROTOCOLS",
    "Retry",
    "Timeout",
    "Url",
    "assert_fingerprint",
    "is_connection_dropped",
    "is_fp_closed",
    "parse_url",
    "make_headers",
    "resolve_cert_reqs",
    "resolve_ssl_version",
    "ssl_wrap_socket",
    "wait_for_read",
    "wait_for_write",
    "SKIP_HEADER",
    "SKIPPABLE_HEADERS",
)
