from ..bep_pcb_check import model_path, BEPPCBCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest


@pytest.fixture(autouse=True, scope='module')
def bp_rt(test_root):
    # SQL state builder tests
    rt = RegressionTester(BEPPCBCheck, model_path, 
                          "bep_pcb_test_spec.json",
                          test_root=test_root, sub_dir='sql')
    rt.run_models(state_builder='sql')
    return rt

# Prediction tests

@pytest.mark.parametrize('load', all_loads)
def test_prediction(bp_rt, answer_store, load):
    if not answer_store:
        bp_rt.run_test("prediction", load)
    else:
        pass

# Validation tests


@pytest.mark.parametrize('load', all_loads)
def test_validation(bp_rt, answer_store, load):
    if not answer_store:
        bp_rt.run_test("validation", load)
    else:
        pass
