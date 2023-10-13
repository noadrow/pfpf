from pandas import DataFrame,read_pickle,read_csv,cut
from numpy import arange, polyfit, poly1d
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from time import time
import sys

plotting = False

def read_cgs(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file]
    return lines

def loading_file():
    import argparse
    if(len(sys.argv) > 1):
        INPUT_control = str(sys.argv[1])
        CPG_PATH = str(sys.argv[2])
        # number of coefficients for the polynomial
        cof_num = int(sys.argv[3])
        # number of amplitude of a peak to be counted as a real gaussian peak
        threshold = int(sys.argv[4])
        group = str(sys.argv[5])
        plotting = False

        if (len(sys.argv) > 6):
            plotting = True


    else:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        from tkinter.simpledialog import askinteger
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import askyesno

        Tk().withdraw()
        print('waiting for dataset...')
        INPUT_control = askopenfilename(title='pick a pickle',filetypes=[("Pickles", "*.pickle")])
        print('waiting for CpG list...')
        CPG_PATH = askopenfilename(title='pick a CpG list',filetypes=[("Text File", "*.txt")])
        print('waiting for number of coefficients for the polynomial...')
        cof_num = askinteger(title='coeff num',prompt='number of coefficients for the polynomial')
        threshold = askinteger(title='threshold',prompt='threshold for amplitude to include the peak count')
        group = askstring(title='experiment name',prompt='name the experiment')
        plotting = askyesno(title='do you want to plot? (yes) or save counting (no)', message=None)

    print('loading data...')
    time0 = time()
    df = read_pickle(INPUT_control)
    df.index = df.iloc[:,0]
    df = df.drop(df.columns[0], axis=1)
    CpG_list = read_cgs(CPG_PATH)
    print(f'finished loading data in {time()-time0} sec')
    return [df,CpG_list,cof_num,threshold,group,plotting]

def barplot_range_count(df, group, cgs):
    range_counts = []
    for cg in cgs:
        cg = cg.replace(" ", "")
        if (cg in df.index):
            working_df = df.loc[cg]
            new_pd = DataFrame({
                'range': cut(working_df, arange(0, 1, 0.01)),
                'val': working_df,
                'index': working_df.index,
                'counter': [1] * len(working_df)
            })
            range_count = new_pd.groupby('range')['counter'].count()
            range_counts.append(range_count)
    return range_counts

def load_data(data_path):
  #load data
  data = read_csv(data_path)
  # take axis from data
  x = data['range']
  y = data['counter']

  return [x,y]

def polyfit_to_peak(x,y):

  # Fit a polynomial to the data
  coefficients = polyfit(x, y, cof_num)
  poly = poly1d(coefficients)

  # Evaluate the polynomial at x_values
  y_curve = poly(x)

  # Find peaks in the curve using find_peaks
  peaks, _ = find_peaks(y_curve)

  # Retrieve the y-values of the detected peaks
  y_peak_values = y_curve[peaks]

  return [x,y,y_curve,y_peak_values,peaks]

def plot_everthing(x,y,y_curve,y_peak_values,peaks,cg,peak_num,peak_vals):
  plt.clf()
  # Plot the data, fitted curve, and peaks
  plt.title(f'cg:{cg}, peak_num: {peak_num}')
  plt.suptitle(peak_vals)
  plt.figure(figsize=(8, 6))
  plt.plot(x, y, label='Original Data')
  plt.plot(x, y_curve, label='Fitted Polynomial Curve')
  plt.scatter(x[peaks], y_peak_values, c='red', marker='x', label='Peaks')
  plt.legend()
  plt.savefig(f'./results_poly/{cg}_{peak_num}.png')

def real_peaker(y_peak_values):
  counter = 0
  peak_vals = []
  for peak in y_peak_values:
    if (peak>threshold):
      peak_vals.append(peak)
      counter = counter+1
      peak_state = True

  return [counter,peak_vals]



if __name__ == '__main__':
    if "--help" in sys.argv or "-h" in sys.argv:

        print('''
                -arge1 = dataset
                -arg2 = CpG list
                -arg3 = coefficient numebr for polyfit
                -arg4 = threashold for peak detection
                -arg5 = name the experiment
                --plot = for plotting results, empty for filtered CpG list only
        ''')
    else:
        cgs = []
        df,CpG_list,cof_num,threshold,group,plotting = loading_file()
        #df_filt = df.loc[df.index.intersection(CpG_list)]
        print('making pdfs...')
        time0 = time()
        range_counts = barplot_range_count(df,group,CpG_list)
        print(f'finished ordering to pdf in {time()-time0} sec')
        time0 = time()
        print('calc and plot results...')
        for count,cg in zip(range_counts,CpG_list):
            data = DataFrame({
                'range': [l.mid for l in count.index],
                'counter': count.values
            })

            x, y = data['range'],data['counter']
            x, y, y_curve, y_peak_values, peaks = polyfit_to_peak(x, y)
            counter,peak_vals = real_peaker(y_peak_values)
            if(counter>1):
                cgs.append(cg)

            if plotting:
                plot_everthing(x,y,y_curve,y_peak_values,peaks,cg,counter,peak_vals)

        if not plotting:
            with open(f"./results_poly/{group}.txt", 'w') as f:
                f.write("\n".join(map(str, cgs)))

        print(f'finished successfully in {time() - time0}')


