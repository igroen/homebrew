from homebrew import logger


def test_print_title(capsys):
    logger.print_title("Installed packages:")
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert len(lines[0]) == len(lines[1])


def test_print_blank_line(capsys):
    logger.print_blank_line()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0] == ""


def test_print_overview(capsys, expected_log_output):
    logger.print_overview(
        installed=["foo", "bar"],
        packages_not_needed_by_other=["bar"],
        packages_needed_by_other={"foo": ["bar"]},
        package_dependencies={"bar": ["foo"]},
    )
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines == expected_log_output
