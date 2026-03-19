import ctypes
import time
from pathlib import Path

from log import init_logging


def load_add_lib() -> ctypes.CDLL:
    lib_path = Path("/app/native/libadd.so")
    if not lib_path.exists():
        raise FileNotFoundError(f"Shared library not found: {lib_path}")

    lib = ctypes.CDLL(str(lib_path))

    # int add_ints(int a, int b);
    lib.add_ints.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.add_ints.restype = ctypes.c_int

    return lib


if __name__ == "__main__":
    logger = init_logging("python_c_demo")

    lib = load_add_lib()
    logger.info("Loaded C shared library /app/native/libadd.so")

    counter = 0
    while True:
        a = counter
        b = 10
        result = lib.add_ints(a, b)

        logger.info(f"add_ints({a}, {b}) = {result}")

        counter += 1
        time.sleep(1.0)