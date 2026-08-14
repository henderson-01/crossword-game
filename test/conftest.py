import importlib.util
import os
import sys

import pytest


@pytest.fixture(autouse=True)
def headless_tkinter():
    """
    Ensures Tkinter runs in headless mode during tests.
    Automatically starts Xvfb on Linux if no display is found.
    """
    if sys.platform.startswith("linux") and "DISPLAY" not in os.environ:
        if importlib.util.find_spec("xvfbwrapper") is not None:
            # noinspection PyPackageRequirements, PyUnresolvedReferences
            import xvfbwrapper

            display = xvfbwrapper.Xvfb()
            display.start()
            yield
            display.stop()
            return
        else:
            # Fallback for zero-install headless environments
            os.environ["DISPLAY"] = ":0"

    # Fallback yield for Windows/Mac or if xvfbwrapper is missing
    yield
