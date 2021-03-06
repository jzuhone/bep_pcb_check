from ..bep_pcb_check import model_path, BEPPCBCheck
from acis_thermal_check.regression_testing import \
    RegressionTester
import os


def test_JUL3019A_viols(answer_store, test_root):
    answer_data = os.path.join(os.path.dirname(__file__), "answers",
                               "JUL2919A_viol.json")
    beppcb_rt = RegressionTester(BEPPCBCheck, model_path,
                                 "bep_pcb_test_spec.json",
                                 test_root=test_root, sub_dir='viols')
    beppcb_rt.check_violation_reporting("JUL2919A", answer_data,
                                        answer_store=answer_store)