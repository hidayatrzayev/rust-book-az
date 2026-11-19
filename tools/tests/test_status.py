import subprocess

import pytest

from status import STATUSES, init_rows, latest_commit, load_rows, outdated, set_status, translated_rows, write_rows


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True,
                   env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
                        "GIT_COMMITTER_EMAIL": "t@t", "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin"})


@pytest.fixture
def en_repo(tmp_path):
    repo = tmp_path / "en"
    (repo / "src").mkdir(parents=True)
    git(repo, "init", "-q")
    (repo / "src" / "a.md").write_text("one\n")
    (repo / "src" / "b.md").write_text("one\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "first")
    return repo


def test_init_rows_lists_every_file_not_started(en_repo, tmp_path):
    az_src = tmp_path / "az" / "src"
    az_src.mkdir(parents=True)
    for n in ("a.md", "b.md"):
        (az_src / n).write_text("x")
    rows = init_rows(az_src, en_repo, {})
    assert [(r.file, r.status) for r in rows] == [("a.md", "başlanmayıb"), ("b.md", "başlanmayıb")]
    assert all(len(r.commit) == 40 for r in rows)


def test_outdated_detected(en_repo):
    c1 = latest_commit(en_repo, "a.md")
    rows = [type("R", (), {"file": "a.md", "status": "qaralama", "commit": c1})(),
            type("R", (), {"file": "b.md", "status": "yoxlanılıb", "commit": latest_commit(en_repo, "b.md")})()]
    assert outdated(rows, en_repo) == []
    (en_repo / "src" / "a.md").write_text("two\n")
    git(en_repo, "commit", "-qam", "change a")
    assert [r.file for r in outdated(rows, en_repo)] == ["a.md"]


def test_not_started_never_outdated(en_repo):
    rows = [type("R", (), {"file": "a.md", "status": "başlanmayıb", "commit": "0" * 40})()]
    assert outdated(rows, en_repo) == []


def test_set_stamps_commit(en_repo, tmp_path):
    path = tmp_path / "STATUS.md"
    az_src = tmp_path / "src"
    az_src.mkdir()
    for n in ("a.md", "b.md"):
        (az_src / n).write_text("x")
    write_rows(path, init_rows(az_src, en_repo, {}))
    (en_repo / "src" / "a.md").write_text("two\n")
    git(en_repo, "commit", "-qam", "change a")
    set_status(path, "a.md", "qaralama", en_repo)
    rows = {r.file: r for r in load_rows(path)}
    assert rows["a.md"].status == "qaralama"
    assert rows["a.md"].commit == latest_commit(en_repo, "a.md")
    assert rows["b.md"].status == "başlanmayıb"


def test_set_rejects_bad_status_and_file(en_repo, tmp_path):
    path = tmp_path / "STATUS.md"
    az_src = tmp_path / "src"
    az_src.mkdir()
    (az_src / "a.md").write_text("x")
    write_rows(path, init_rows(az_src, en_repo, {}))
    with pytest.raises(ValueError):
        set_status(path, "a.md", "done", en_repo)
    with pytest.raises(ValueError):
        set_status(path, "zzz.md", "qaralama", en_repo)
    assert "yoxlanılıb" in STATUSES


def test_init_keeps_existing_rows(en_repo, tmp_path):
    az_src = tmp_path / "src"
    az_src.mkdir()
    for n in ("a.md", "b.md"):
        (az_src / n).write_text("x")
    first = init_rows(az_src, en_repo, {})
    first[0].status = "qaralama"
    again = init_rows(az_src, en_repo, {r.file: r for r in first})
    assert again[0].status == "qaralama"


def test_translated_rows_excludes_not_started():
    rows = [type("R", (), {"file": f, "status": s})() for f, s in
            (("a.md", "başlanmayıb"), ("b.md", "qaralama"), ("c.md", "yoxlanılıb"))]
    assert [r.file for r in translated_rows(rows)] == ["b.md", "c.md"]
