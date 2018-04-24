# CoreML to ONNX converter
Just a simple snippet which input the coreML model and output onnx models

## GUI application release
* 4/24/2018: [Developing version release](https://github.com/b02902131/coreml_to_onnx/releases/tag/v0.1.0)

![GUI Application](https://github.com/b02902131/coreml_to_onnx/blob/master/image/GUI.PNG)

## Usage
```
$ python coreml_to_onnx.py [coreML_model] [onnx_model]
```

* `coreML_model` : The name of the model you want to convert, ended with ".mlmodel".
* `onnx_model` : The output name of the onnx model.

## Requirement
 - coremltools
 - winmltools

You can install the packages by the command below:
```
$ pip install -r requirements.txt
```

**Note:**
CoreMLTools is a Python package provided by Apple, but is not available on Windows. If you need to install the package on Windows, install the package directly from the repo:

```
$ pip install git+https://github.com/apple/coremltools
```
