import pytest

from tests.archive_fixture import build_archive


@pytest.fixture
def archive(tmp_path):
    return build_archive(tmp_path / "archive")
