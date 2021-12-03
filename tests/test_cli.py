import os


def test_binary_file_exists():
    assert os.path.exists('.venv/bin/page-loader'), \
        'Binary file page-loader not found'
