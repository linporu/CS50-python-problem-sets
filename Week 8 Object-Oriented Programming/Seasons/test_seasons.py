import pytest
import seasons


def test_seasons_1_year(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '2023-09-30')
    from seasons import main
    main()
    captured = capsys.readouterr()
    assert "Five hundred twenty-seven thousand forty minutes" in captured.out


def test_seasons_2_years(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '2022-09-30')
    from seasons import main
    main()
    captured = capsys.readouterr()
    assert "One million, fifty-two thousand, six hundred forty minutes" in captured.out
