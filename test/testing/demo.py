import os

import pytest

DEMO_PROJECT_PATH = os.environ.get('DEMO_PROJECT_PATH', None)
demo_mark = pytest.mark.unittest if DEMO_PROJECT_PATH and os.path.exists(DEMO_PROJECT_PATH) else pytest.mark.ignore

DEMO_COMPLEX_PROJECT_PATH = os.environ.get('DEMO_COMPLEX_PROJECT_PATH', None)
demo_complex_mark = pytest.mark.unittest if DEMO_COMPLEX_PROJECT_PATH \
                                            and os.path.exists(DEMO_COMPLEX_PROJECT_PATH) else pytest.mark.ignore

DEMO_ALL_PROJECT_PATH = os.environ.get('DEMO_ALL_PROJECT_PATH', None)
demo_all_mark = pytest.mark.unittest if DEMO_ALL_PROJECT_PATH \
                                        and os.path.exists(DEMO_ALL_PROJECT_PATH) else pytest.mark.ignore
