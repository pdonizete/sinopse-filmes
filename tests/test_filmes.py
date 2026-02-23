import sys
import types
import unittest


if "requests" not in sys.modules:
    requests_stub = types.ModuleType("requests")
    exceptions_stub = types.SimpleNamespace(
        Timeout=Exception,
        ConnectionError=Exception,
        RequestException=Exception,
    )
    requests_stub.exceptions = exceptions_stub
    sys.modules["requests"] = requests_stub

if "dotenv" not in sys.modules:
    dotenv_stub = types.ModuleType("dotenv")
    dotenv_stub.load_dotenv = lambda: None
    sys.modules["dotenv"] = dotenv_stub

from filmes import formatar_nota


class TestFilmes(unittest.TestCase):
    def test_formatar_nota_excelente(self):
        self.assertEqual(formatar_nota("8.5"), "⭐ 8.5/10 (Excelente)")


if __name__ == "__main__":
    unittest.main()
