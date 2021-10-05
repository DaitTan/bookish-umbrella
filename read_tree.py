import matplotlib.pyplot as plt
import pickle
import numpy as np
from partx.partx_options import partx_options
import pathlib
from matplotlib.patches import Rectangle

# def save_trees_plots(q, tree_dir, im_dir, options):
    
#     f = open(tree_dir, "rb")
#     ftree = pickle.load(f)
#     f.close()

#     leaves = ftree.leaves()
#     fig = plt.figure()

#     # print("*******************************************************")
#     points_in_list = []
#     node_id = []
#     points_class = []
    
#     for x,i in enumerate(leaves):
#         # fig = plt.figure()
#         x_1, y_1, x_2,y_2,x_3,y_3,x_4,y_4 = plotRegion(i.data.region_support)
#         plt.plot(x_1,y_1)
#         plt.plot(x_2,y_2)
#         plt.plot(x_3,y_3)
#         plt.plot(x_4,y_4)
#         points_class.append(i.data.region_class)
#         points_in_list.append((i.data.samples_in).shape[1])
#         node_id.append(i.identifier)
#         if i.data.region_class == "+":
#             plt.plot(i.data.samples_in[0,:,0], i.data.samples_in[0,:,1], 'g.')
#         elif i.data.region_class == "-":
#             plt.plot(i.data.samples_in[0,:,0], i.data.samples_in[0,:,1], 'r.')

#     plt.title("Function Budget = {} -- BO Grid {} x {}".format(options.max_budget, options.number_of_BO_samples[0], options.number_of_samples_gen_GP))
#     plt.savefig(im_dir)
#     print("*****************************")
#     print("Points in Replication {} = {}".format(q, sum(points_in_list)))



def save_trees_plots(q, tree_dir, im_dir, options):
    
    f = open(tree_dir, "rb")
    ftree = pickle.load(f)
    f.close()

    leaves = ftree.leaves()
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    # print("*******************************************************")
    points_in_list = []
    node_id = []
    points_class = []
    ax.set_ylim(options.initial_region_support[0][0,0], options.initial_region_support[0][0,1])
    ax.set_xlim(options.initial_region_support[0][1,0], options.initial_region_support[0][1,1]) 
    for x,i in enumerate(leaves):
        # fig = plt.figure()
        # x_1, y_1, x_2,y_2,x_3,y_3,x_4,y_4 = plotRegion(i.data.region_support)
        r_support = np.array(i.data.region_support[0])
        x = r_support[0,0]
        y = r_support[1,0]
        w = r_support[0,1] - r_support[0,0]
        h = r_support[1,1] - r_support[1,0]

        if y+h != options.initial_region_support[0][0,1]:
            if x+w != options.initial_region_support[0][1,1] or x != options.initial_region_support[0][1,0]:
                val_x = [r_support[0,0],  r_support[0,1]]
                val_y = [r_support[1,1], r_support[1,1]]
                plt.plot(val_x, val_y, 'k', linewidth = 1.5)
        
        if x+w != options.initial_region_support[0][1,1]:
            if y+h != options.initial_region_support[0][0,1] or y != options.initial_region_support[0][0,0]:
                val_y = [r_support[1,0],  r_support[1,1]]
                val_x = [r_support[0,1], r_support[0,1]]
                plt.plot(val_x, val_y, 'k', linewidth = 1.5)
        

        points_class.append(i.data.region_class)
        points_in_list.append((i.data.samples_in).shape[1])
        node_id.append(i.identifier)
        if i.data.region_class == "+":
            ax.add_patch( Rectangle((x,y),
                            w, h,
                            fc ='green',
                            alpha = 0.4))
            ax.plot(i.data.samples_in[0,:,0], i.data.samples_in[0,:,1], 'g.', markersize = 2)
        elif i.data.region_class == "-":
            ax.add_patch( Rectangle((x,y),
                            w, h,
                            ec = 'black',
                            fc ='red',
                            alpha = 0.4))
            ax.plot(i.data.samples_in[0,:,0], i.data.samples_in[0,:,1], 'r.', markersize = 2)
        elif i.data.region_class == "r" or i.data.region_class == "r+" or i.data.region_class == "r-":
            ax.add_patch( Rectangle((x,y),
                            w, h,
                            ec = 'black',
                            fc ='blue',
                            alpha = 0.4))
            ax.plot(i.data.samples_in[0,:,0], i.data.samples_in[0,:,1], 'b.', markersize = 2)

    plt.savefig(im_dir)
    print("*****************************")
    print("Points in Replication {} = {}".format(q, sum(points_in_list)))


BENCHMARK_NAME = "Goldstein_price_1"

result_directory = pathlib.Path().joinpath('result_files').joinpath(BENCHMARK_NAME).joinpath(BENCHMARK_NAME + "_result_generating_files")

f = open(result_directory.joinpath(BENCHMARK_NAME + "_options.pkl"), "rb")
options = pickle.load(f)
f.close()


from partx.utils_partx import plotRegion

for i in range(5):
    tree_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+".pkl")
    im_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+".png")
    save_trees_plots(i, tree_dir, im_dir, options)