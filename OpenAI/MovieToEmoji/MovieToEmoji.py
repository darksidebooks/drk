import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

import openai
openai.api_key = secrets["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"]