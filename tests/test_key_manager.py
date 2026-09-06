from src.key_manager import generate_key, load_key

def test_generate_key():
    generate_key()
    key = load_key()

    assert key is not None
    assert len(key) > 0