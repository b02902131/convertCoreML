import sys

if len(sys.argv) < 3:
    print("Usage: python convertCoreML.py [coreML model name] [onnx model name]")
    exit()
else:
    coreML_name = sys.argv[1]
    onnx_name = sys.argv[2]

from coremltools.models.utils import load_spec
model_coreml = load_spec(coreML_name)

from winmltools import convert_coreml
model_onnx = convert_coreml(model_coreml)

from winmltools.utils import save_model
save_model(model_onnx, onnx_name)
