import sys
from textwrap import dedent

import pytest

import select_jobs


@pytest.mark.parametrize(
    ("version", "docs", "android"),
    [
        # Tags
        ("v3.13.0a1", "false", "false"),
        ("v3.13.0rc1", "true", "false"),
        ("v3.13.0", "true", "false"),
        ("v3.13.1", "true", "false"),
        ("v3.14.0b2", "false", "true"),
        ("v3.14.0rc1", "true", "true"),
        ("v3.14.0", "true", "true"),
        ("v3.14.1", "true", "true"),
        ("v3.15.0a1", "false", "true"),
        ("v3.15.0", "true", "true"),
        # Branches
        ("3.13", "true", "false"),
        ("3.14", "true", "true"),
        ("main", "true", "true"),
    ],
)
def test_select_jobs(
    version: str,
    docs: str,
    android: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["select_jobs.py", version])
    select_jobs.main()
    assert capsys.readouterr().out == dedent(
        f"""\
            docs={docs}
            android={android}
        """
    )
