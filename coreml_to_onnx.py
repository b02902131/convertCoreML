import sys

##################
## Check package
##################


##################
## Check arguments
##################

if len(sys.argv) != 3:
    print("\t (!) Usage: python convertCoreML.py [coreML model name] [onnx model name]")
    print("\t\t * coreML_model : The name of the model you want to convert, ended with \".mlmodel\".")
    print("\t\t * onnx_model \t: The output name of the onnx model.")
    exit()
else:
    coreML_name = sys.argv[1]
    onnx_name = sys.argv[2]

if len(coreML_name) <= len(".mlmodel") or coreML_name[-len(".mlmodel"):] != ".mlmodel":
    print("\t (!) File name error: ", coreML_name, "is not a coreMLmodel. It's not ended with \".mlmodel\"")
    exit()

from coremltools.models.utils import load_spec
model_coreml = load_spec(coreML_name)

from winmltools import convert_coreml
model_onnx = convert_coreml(model_coreml)

from winmltools.utils import save_model
save_model(model_onnx, onnx_name)
