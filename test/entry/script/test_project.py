from jentry.entry.script import load_entries_from_project
from ...testing import demo_mark, DEMO_PROJECT_PATH, demo_complex_mark, DEMO_COMPLEX_PROJECT_PATH, demo_all_mark, \
    DEMO_ALL_PROJECT_PATH


class TestEntryScriptProject:
    @demo_mark
    def test_load_entries_from_project_demo(self):
        entries = list(load_entries_from_project(DEMO_PROJECT_PATH))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package == 'homework'
        assert entry.clazz == 'Main'

    @demo_complex_mark
    def test_load_entries_from_project_demo_complex(self):
        entries = list(load_entries_from_project(DEMO_COMPLEX_PROJECT_PATH))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package is None
        assert entry.clazz == 'Main'

    @demo_all_mark
    def test_load_entries_from_project_demo_all(self):
        entries = list(load_entries_from_project(DEMO_ALL_PROJECT_PATH))
        assert len(entries) == 2
