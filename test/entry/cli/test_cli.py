import pytest
from click.testing import CliRunner

from jentry.entry.cli import cli


@pytest.mark.unittest
class TestEntryCliCli:
    def test_version(self):
        runner = CliRunner()
        result = runner.invoke(cli, args=['-v'])

        assert result.exit_code == 0
        assert "jentry" in result.stdout.lower()
