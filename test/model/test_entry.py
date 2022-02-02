import pytest

from jentry.model import JavaEntry


@pytest.mark.unittest
class TestModelEntry:
    def test_java_entry(self):
        e = JavaEntry('src/Main.java', 'main.package', 'MainClazz')
        assert e.filename == 'src/Main.java'
        assert e.package == 'main.package'
        assert e.clazz == 'MainClazz'
        assert e.full_name == 'main.package.MainClazz'
        assert str(e) == 'main.package.MainClazz'
        assert repr(e) == "<JavaEntry class: main.package.MainClazz, filename: 'src/Main.java'>"

    def test_java_entry_without_package(self):
        e = JavaEntry('src/Main.java', None, 'MainClazz')
        assert e.filename == 'src/Main.java'
        assert e.package is None
        assert e.clazz == 'MainClazz'
        assert e.full_name == 'MainClazz'
        assert str(e) == 'MainClazz'
        assert repr(e) == "<JavaEntry class: MainClazz, filename: 'src/Main.java'>"

    def test_java_entry_without_filename(self):
        e = JavaEntry(None, 'main.package', 'MainClazz')
        assert e.filename is None
        assert e.package == 'main.package'
        assert e.clazz == 'MainClazz'
        assert e.full_name == 'main.package.MainClazz'
        assert str(e) == 'main.package.MainClazz'
        assert repr(e) == "<JavaEntry class: main.package.MainClazz>"
