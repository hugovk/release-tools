import sys
from textwrap import dedent

import pytest

import select_jobs


@pytest.mark.parametrize(
    ("version", "docs", "android", "ios", "macos"),
    [
        ("3.13.0a1", "false", "false", "false", "false"),
        ("3.13.0rc1", "true", "false", "false", "false"),
        ("3.13.0", "true", "false", "false", "false"),
        ("3.13.1", "true", "false", "false", "false"),
        ("3.14.0b2", "false", "true", "false", "true"),
        ("3.14.0rc1", "true", "true", "false", "true"),
        ("3.14.0", "true", "true", "false", "true"),
        ("3.14.1", "true", "true", "false", "true"),
        ("3.15.0a1", "false", "true", "true", "true"),
        ("3.15.0", "true", "true", "true", "true"),
    ],
)
def test_select_jobs(
    version: str,
    docs: str,
    android: str,
    ios: str,
    macos: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["select_jobs.py", version])
    select_jobs.main()
    assert capsys.readouterr().out == dedent(
        f"""\
            docs={docs}
            android={android}
            ios={ios}
            macos={macos}
        """
    )


@pytest.mark.parametrize(
    "version",
    [
        "3.13.0a1",
        "3.13.0",
        "3.14.0b2",
        "3.15.0a1",
    ],
)
def test_select_jobs_test_mode(
    version: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["select_jobs.py", "--test", version])
    select_jobs.main()
    assert capsys.readouterr().out == dedent(
        """\
            docs=true
            android=true
            ios=true
            macos=true
        """
    )
