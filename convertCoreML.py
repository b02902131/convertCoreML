
from coremltools.models.utils import load_spec

model_coreml = load_spec('aa7e3f5e4629417d9d6ba063fb9a659e.mlmodel')
from winmltools import convert_coreml

model_onnx = convert_coreml(model_coreml)


from winmltools.utils import save_model
save_model(model_onnx, 'aa7e3f5e4629417d9d6ba063fb9a659e.onnx')
