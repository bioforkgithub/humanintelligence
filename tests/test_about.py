import humanintelligence as hi


def test_about_names_the_package_and_version(capsys):
    text = hi.about()
    assert text.startswith(f"humanintelligence {hi.__version__}")
    assert text in capsys.readouterr().out
