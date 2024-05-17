import llm
import pytest
from llm.plugins import pm


class LengthSummary(llm.Model):
    model_id = "length-summary"

    def execute(self, prompt, stream, response, conversation):
        return [f"System: {len(prompt.system)} - Prompt: {len(prompt.prompt)}"]


@pytest.fixture(autouse=True)
def register_models():
    class ModelsPlugin:
        __name__ = "ModelsPlugin"

        @llm.hookimpl
        def register_models(self, register):
            register(LengthSummary())

    pm.register(ModelsPlugin(), name="undo-demo-plugin")
    try:
        yield
    finally:
        pm.unregister(name="undo-demo-plugin")
