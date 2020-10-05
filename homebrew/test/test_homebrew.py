from homebrew import HomeBrew


def test_homebrew(capsys, expected_log_output):
    hb = HomeBrew()

    assert len(hb.installed_packages) == 2
    assert hb.installed_packages[0] == "foo"
    assert hb.installed_packages[1] == "bar"

    assert len(hb._uses) == 2
    assert hb._uses["foo"] == ["bar"]
    assert hb._uses["bar"] == []

    assert hb.packages_not_needed_by_other == ["bar"]
    assert hb.packages_needed_by_other == {"foo": ["bar"]}
    assert hb.package_dependencies == {"bar": ["foo"]}

    hb.info
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines == expected_log_output
