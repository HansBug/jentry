import codecs
import os

from jentry.entry.script import load_entries_from_file, load_entry_classes_from_code
from ...testing import demo_mark, DEMO_PROJECT_PATH, demo_complex_mark, DEMO_COMPLEX_PROJECT_PATH


class TestEntryScriptProject:
    @demo_mark
    def test_load_entries_from_file_demo(self):
        entries = list(load_entries_from_file(os.path.join(DEMO_PROJECT_PATH, 'src/homework/Main.java')))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package == 'homework'
        assert entry.clazz == 'Main'

    @demo_complex_mark
    def test_load_entries_from_file_demo_complex(self):
        entries = list(load_entries_from_file(os.path.join(DEMO_COMPLEX_PROJECT_PATH, 'src/Main.java')))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package is None
        assert entry.clazz == 'Main'

    @demo_mark
    def test_load_entry_classes_from_code_demo(self):
        with codecs.open(os.path.join(DEMO_PROJECT_PATH, 'src/homework/Main.java'), 'r') as sf:
            classes = list(load_entry_classes_from_code(sf.read()))

            assert len(classes) == 1
            clx = classes[0]
            assert clx == ('homework', 'Main')

    @demo_complex_mark
    def test_load_entry_classes_from_code_demo_complex(self):
        with codecs.open(os.path.join(DEMO_COMPLEX_PROJECT_PATH, 'src/Main.java'), 'r') as sf:
            classes = list(load_entry_classes_from_code(sf.read()))

            assert len(classes) == 1
            clx = classes[0]
            assert clx == (None, 'Main')
