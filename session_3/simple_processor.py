import pandas as pd  # data handling
from sklearn.preprocessing import StandardScaler  # rescaling data before pca
from sklearn.decomposition import PCA  # actual PCA
from matplotlib import pyplot as plt  # for creating plot
import argparse  # making command-line script
import os  # to deal with filepaths


def protein_counts(df: pd.DataFrame) -> pd.Series:
    """Given a DataFrame of samples by proteins, computes the number of non-zero protein in a sample."""
    # Get the values that are greater than 0
    gt0 = df > 0
    return gt0.apply(sum, axis=1)


def protein_fraction(df: pd.DataFrame) -> pd.Series:
    """Given a DataFrame of samples by proteins, computes the fraction of cells in which each protein is found."""
    gt0 = df > 0
    return gt0.apply(sum, axis=0) / gt0.shape[0]


def total_protein(df: pd.DataFrame) -> pd.Series:
    """Given a DataFrame of samples by proteins, computes the total protein quantity for each sample."""
    return df.apply(sum, axis=1)


def pca(df: pd.DataFrame):
    """Performs rescale + PCA on the input DataFrame"""
    rescaled = StandardScaler().fit_transform(df)
    pcaer = PCA(n_components=2)
    pc = pcaer.fit_transform(rescaled)
    return pc


def plot_pc(pcs,
            output_name: str = "pca_plt.png"):
    """Creates a scatter plot for the data points"""
    plt.figure()
    plt.scatter(pcs[:,0], pcs[:,1])
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA Plot")
    plt.savefig(output_name)
    return


def produce_report(save_path: str,
                   counts: pd.Series,
                   fracs: pd.Series,
                   totals: pd.Series):
    """Saves the counts, fracs, and totals into the text file specified by save_path."""
    f = open(save_path, "w")
    f.write("Protein counts per sample: \n")
    f.write(counts.to_string())
    f.write("\n-------------------------\n\n\n")

    f.write("Fraction of cells by protein:\n")
    f.write(fracs.to_string())
    f.write("\n-------------------------\n\n")

    f.write("Total protein quantity per sample:\n")
    f.write(totals.to_string())
    f.write("\n-------------------------")
    f.close()
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Protein Processing",
                                     usage=f"{os.path.basename(__file__)} data_file.csv out_report.txt out_plot.png",
                                     description="Processes a .csv data file containing samples x proteins to produce"
                                                 "a brief report and a PCA plot.")
    parser.add_argument("data_file", help="Path to the .csv file containing the data to process.")
    parser.add_argument("out_report", help="Path where the report should be saved.")
    parser.add_argument("out_plot", help="Path where the report should be saved. Should be .png file.")

    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.data_file, index_col="sample")

    prot_counts = protein_counts(df)  # Get protein counts
    prot_frac = protein_fraction(df)  # Get protein fraction
    prot_total = total_protein(df)  # Get protein totals

    # Deal with pcs
    pcs = pca(df)  # compute components
    plot_pc(pcs, output_name=args.out_plot)  # Plot pcs

    # Write report
    produce_report(args.out_report, counts=prot_counts, fracs=prot_frac, totals=prot_total)

    # Done!

