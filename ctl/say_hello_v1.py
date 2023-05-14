from ctl.processor import Processor


class SayHelloV1(Processor):
    @staticmethod
    def process(spec):
        print(f"Hello {spec['params']['name']}")
