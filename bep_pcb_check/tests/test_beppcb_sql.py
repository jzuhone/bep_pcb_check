from ..bep_pcb_check import model_path, BEPPCBCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest


beppcb_rt = RegressionTester(BEPPCBCheck, model_path, "bep_pcb_test_spec.json")

# SQL state builder tests

beppcb_rt.run_models(state_builder='sql')

# Prediction tests


@pytest.mark.parametrize('load', all_loads)
def test_prediction(answer_store, load):
    if not answer_store:
        beppcb_rt.run_test("prediction", load)
    else:
        pass

# Validation tests


@pytest.mark.parametrize('load', all_loads)
def test_validation(answer_store, load):
    if not answer_store:
        beppcb_rt.run_test("validation", load)
    else:
        pass
