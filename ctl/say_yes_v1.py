from dataclasses import dataclass

from ctl.processor import Processor


@dataclass
class SayYesV1Spec:
    name: str
    prefix: str


class SayYesV1(Processor):
    def process(self, spec_in: dict):
        try:
            spec = self.spec(spec_in)
            print(f"Yes {spec.prefix} {spec.name}")
        except KeyError as e:
            print(f"Required parameter was not found: {e.args[0]}")

    @staticmethod
    def spec(spec: dict) -> SayYesV1Spec:
        return SayYesV1Spec(
            spec["params"]["name"],
            spec["params"]["prefix"],
        )
