from main import main


def test_main_function_exists():
    """Test that main function exists and is callable."""
    assert callable(main)


def test_main_prints_startup_message(capsys):
    """Test that main function prints the expected startup message."""
    main()
    captured = capsys.readouterr()
    assert "🤖 Agent starting..." in captured.out
    assert "✅ Agent ready" in captured.out


def test_main_runs_without_error():
    """Test that main function runs without raising any exceptions."""
    try:
        main()
    except Exception as e:
        raise AssertionError(f"main() raised an exception: {e}") from e