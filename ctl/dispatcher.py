import yaml

from ctl.say_hello_v1 import SayHelloV1
from ctl.say_hello_v2 import SayHelloV2
from ctl.say_yes_v1 import SayYesV1


def dispatch(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
        kind = data["kind"]
        api_version = data["apiVersion"]
        match kind, api_version:
            case "SayHello", "v1":
                SayHelloV1().process(data['spec'])
            case "SayHello", "v2":
                SayHelloV2().process(data['spec'])
            case "SayYes", "v1":
                SayYesV1().process(data['spec'])
            case _:
                print('Unknown specification')
