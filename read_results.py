import pathlib
import pickle
from partx.models.partx_options import partx_options
from partx.executables.generate_statistics import generate_statistics
import matplotlib.pyplot as plt
import numpy as np
# from read_UR_results import read_UR_results
import logging
from partx.executables.exp_statistics import falsification_volume_using_gp


log = logging.getLogger()
log.setLevel(logging.INFO) 
fh = logging.FileHandler(filename = pathlib.Path().joinpath("nlf_result_logs.log"))
formatter = logging.Formatter(
                fmt = '%(message)s'
                )
fh.setFormatter(formatter)
log.addHandler(fh)


# BENCHMARK_NAME = "Himmelblaus_1"

quantiles_at = [0.5, 0.95, 0.99]
number_of_macro_replications = 2
start_seed = 5000
# points_for_unif_sampling = 10000
confidence_at = 0.95
# result_dictionary_h = generate_statistics("Himmelblaus_3", number_of_macro_replications, quantiles_at, confidence_at, "result_files")
# result_dictionary_r = generate_statistics("Rosenbrock_3", number_of_macro_replications, quantiles_at, confidence_at, "result_files")
result_dictionary_g = generate_statistics("Goldstein_price_1", number_of_macro_replications, quantiles_at, confidence_at, "result_files_testing")
print(result_dictionary_g)
print("******************")


# log.info("{};{};{};{};{};{}".format(result_dictionary_r['mean_fv_wo_gp_classified_unclassified'],
#                             result_dictionary_r['std_dev_fv_wo_gp_classified_unclassified'],
#                             result_dictionary_g['mean_fv_wo_gp_classified_unclassified'],
#                             result_dictionary_g['std_dev_fv_wo_gp_classified_unclassified'],
#                             result_dictionary_h['mean_fv_wo_gp_classified_unclassified'],
#                             result_dictionary_h['std_dev_fv_wo_gp_classified_unclassified']))

# log.info("{};{};{};{};{};{}".format(result_dictionary_r['mean_fv_with_gp_quan0_5'],
#                             result_dictionary_r['std_dev_fv_with_gp_quan0_5'],
#                             result_dictionary_g['mean_fv_with_gp_quan0_5'],
#                             result_dictionary_g['std_dev_fv_with_gp_quan0_5'],
#                             result_dictionary_h['mean_fv_with_gp_quan0_5'],
#                             result_dictionary_h['std_dev_fv_with_gp_quan0_5']))

# log.info("{};{};{};{};{};{}".format(result_dictionary_r['mean_fv_with_gp_quan0_95'],
#                             result_dictionary_r['std_dev_fv_with_gp_quan0_95'],
#                             result_dictionary_g['mean_fv_with_gp_quan0_95'],
#                             result_dictionary_g['std_dev_fv_with_gp_quan0_95'],
#                             result_dictionary_h['mean_fv_with_gp_quan0_95'],
#                             result_dictionary_h['std_dev_fv_with_gp_quan0_95']))

# log.info("{};{};{};{};{};{}".format(result_dictionary_r['mean_fv_with_gp_quan0_99'],
#                             result_dictionary_r['std_dev_fv_with_gp_quan0_99'],
#                             result_dictionary_g['mean_fv_with_gp_quan0_99'],
#                             result_dictionary_g['std_dev_fv_with_gp_quan0_99'],
#                             result_dictionary_h['mean_fv_with_gp_quan0_99'],
#                             result_dictionary_h['std_dev_fv_with_gp_quan0_99']))

# log.info("{};{};{}".format(result_dictionary_r['true_fv'],
#                             result_dictionary_g['true_fv'],
#                             result_dictionary_h['true_fv']))

# print("{};{}\n{};{}\n{};{}\n{};{}\n{}".format(result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_5'],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_95'],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_99'],
#                 result_dictionary['true_fv']
#                 ))

# for key, value in result_dictionary.items():
#     print("{} : {}".format(key, value))

# print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_5'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_95'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_99'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1],))


# print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1]))

# print("{};{}\n{};{}\n{};{}\n{};{}\n{}".format(result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_5'],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_95'],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_99'],
#                 result_dictionary['true_fv']
#                 ))

# print("********************")
