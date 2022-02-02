import json

import pytest
from click.testing import CliRunner

from jentry.entry.cli import cli
from ...testing import DEMO_PROJECT_PATH, demo_mark, DEMO_COMPLEX_PROJECT_PATH, demo_complex_mark, \
    DEMO_ALL_PROJECT_PATH, demo_all_mark


class TestEntryCliCli:
    @pytest.mark.unittest
    def test_version(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-v'])

        assert result.exit_code == 0
        assert "jentry" in result.stdout.lower()

    @demo_mark
    def test_common_demo(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=[DEMO_PROJECT_PATH])

        assert result.exit_code == 0
        assert result.stdout.rstrip() == 'homework.Main'

    @demo_complex_mark
    def test_common_demo_complex(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=[DEMO_COMPLEX_PROJECT_PATH])

        assert result.exit_code == 0
        assert result.stdout.rstrip() == 'Main'

    @demo_all_mark
    def test_common_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=[DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert set(map(lambda x: x.rstrip(), result.stdout.splitlines())) == {'Main', 'homework.Main'}

    @demo_all_mark
    def test_entry_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'entry', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert set(map(lambda x: x.rstrip(), result.stdout.splitlines())) == {'Main', 'homework.Main'}

    @demo_all_mark
    def test_json_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == [
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            },
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            }
        ]

    @demo_all_mark
    def test_table_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'table', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert "Entry" in result.stdout
        assert "Package" in result.stdout
        assert "Class" in result.stdout
        assert "Filename" in result.stdout

        assert "Main" in result.stdout
        assert "demo/2018_spring_16061104_10/src/Main.java" in result.stdout

        assert 'homework.Main' in result.stdout
        assert "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java" in result.stdout

    @demo_mark
    def test_file_demo(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['demo/oo_course_2019_17373331_homework_2/src/homework/Main.java'])

        assert result.exit_code == 0
        assert result.stdout.rstrip() == 'homework.Main'

    @demo_all_mark
    def test_common_first_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-F', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert set(map(lambda x: x.rstrip(), result.stdout.splitlines())) == {'Main'}

    @demo_all_mark
    def test_entry_first_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'entry', '-F', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert set(map(lambda x: x.rstrip(), result.stdout.splitlines())) == {'Main'}

    @demo_all_mark
    def test_json_first_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-F', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == {
            "entrance": "Main",
            "package": None,
            "class": "Main",
            "file": "demo/2018_spring_16061104_10/src/Main.java"
        }

    @demo_all_mark
    def test_table_first_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'table', '-F', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert "Entry" in result.stdout
        assert "Package" in result.stdout
        assert "Class" in result.stdout
        assert "Filename" in result.stdout

        assert "Main" in result.stdout
        assert "demo/2018_spring_16061104_10/src/Main.java" in result.stdout

    @demo_all_mark
    def test_json_sorted_by_file_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-s', 'file', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == [
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            },
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            }
        ]

    @demo_all_mark
    def test_json_sorted_by_package_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-s', 'package', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == [
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            },
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            }
        ]

    @demo_all_mark
    def test_json_sorted_by_entry_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-s', 'entry', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == [
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            },
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            }
        ]

    @demo_all_mark
    def test_json_sorted_by_class_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-s', 'class', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert (json.loads(result.stdout) == [
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            },
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            }
        ]) or (json.loads(result.stdout) == [
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            },
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            }
        ])

    @demo_all_mark
    def test_json_sorted_by_file_reverse_demo_all(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-f', 'json', '-s', 'file', '-r', DEMO_ALL_PROJECT_PATH])

        assert result.exit_code == 0
        assert json.loads(result.stdout) == [
            {
                "entrance": "homework.Main",
                "package": "homework",
                "class": "Main",
                "file": "demo/oo_course_2019_17373331_homework_2/src/homework/Main.java"
            },
            {
                "entrance": "Main",
                "package": None,
                "class": "Main",
                "file": "demo/2018_spring_16061104_10/src/Main.java"
            }
        ]

    @pytest.mark.unittest
    def test_no_entry(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['test'])
        assert result.exit_code == 0
        assert not result.stdout.strip()

        runner = CliRunner()
        result = runner.invoke(cli, args=['-F', 'test'])
        assert result.exit_code == 1
