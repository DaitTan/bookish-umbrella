import pathlib
from partx.generate_statistics import generate_statistics

BENCHMARK_NAME = "Goldstein_price_1"

quantiles_at = [0.5, 0.95, 0.99]
number_of_macro_replications = 5
start_seed = 5000
points_for_unif_sampling = 10000
confidence_at = 0.95
result_dictionary = generate_statistics(BENCHMARK_NAME, number_of_macro_replications, quantiles_at, confidence_at, "result_files")
print("******************")

for key, value in result_dictionary.items():
    print("{} : {}".format(key, value))

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

print("{};{}\n{};{}\n{};{}\n{};{}\n{}".format(result_dictionary['mean_fv_wo_gp_classified_unclassified'],
                result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
                result_dictionary['mean_fv_with_gp_quan0_5'],
                result_dictionary['std_dev_fv_with_gp_quan0_5'],
                result_dictionary['mean_fv_with_gp_quan0_95'],
                result_dictionary['std_dev_fv_with_gp_quan0_95'],
                result_dictionary['mean_fv_with_gp_quan0_99'],
                result_dictionary['std_dev_fv_with_gp_quan0_99'],
                result_dictionary['true_fv']
                ))

print("********************")
