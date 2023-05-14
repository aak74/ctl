from dataclasses import dataclass
from enum import Enum

from ctl.processor import Processor


class SupportedLang(Enum):
    ENGLISH = "english"
    DEUTSCH = "deutsch"
    SPANISH = "spanish"


@dataclass
class SayHelloV2Spec:
    name: str
    lang: str


class SayHelloV2(Processor):
    greetings = {
        SupportedLang.ENGLISH: "Hello",
        SupportedLang.DEUTSCH: "Hallo",
        SupportedLang.SPANISH: "Hola",
    }

    def process(self, spec_in: dict):
        try:
            spec = self._spec(spec_in["params"]["name"], spec_in["params"]["lang"])
            print(f"{spec.lang} {spec.name}")
        except ValueError:
            print(f"{spec_in['params']['lang']} is not supported")

    def _spec(self, name: str, lang: str) -> SayHelloV2Spec:
        return SayHelloV2Spec(
            name,
            self.greetings.get(SupportedLang(lang)),
        )
