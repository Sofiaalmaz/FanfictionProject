import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_linreg_plot(
    predictions: pd.DataFrame, x_data: pd.Series, y_data: pd.Series, x_label: str, y_label: str
) -> None:
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=x_data, y=y_data)
    plt.plot(x_data, predictions, color="red", linewidth=2)
    plt.title(f"{x_label} vs. {y_label} with Regression Line")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def plot_stats_per_year(grouped: pd.DataFrame) -> None:
    # Plot the data
    fig, axes = plt.subplots(3, 3, figsize=(18, 12), sharex=True)

    # Plot mean values
    axes[0, 0].plot(grouped["year"], grouped["favs_mean"], marker="o")
    axes[0, 0].set_title("Average Favorites per Year")
    axes[0, 0].set_ylabel("Mean Favorites")

    axes[0, 1].plot(grouped["year"], grouped["follows_mean"], marker="o")
    axes[0, 1].set_title("Average Follows per Year")
    axes[0, 1].set_ylabel("Mean Follows")

    axes[0, 2].plot(grouped["year"], grouped["reviews_mean"], marker="o")
    axes[0, 2].set_title("Average Reviews per Year")
    axes[0, 2].set_ylabel("Mean Reviews")

    # Plot median values
    axes[1, 0].plot(grouped["year"], grouped["favs_median"], marker="o")
    axes[1, 0].set_title("Median Favorites per Year")
    axes[1, 0].set_ylabel("Median Favorites")

    axes[1, 1].plot(grouped["year"], grouped["follows_median"], marker="o")
    axes[1, 1].set_title("Median Follows per Year")
    axes[1, 1].set_ylabel("Median Follows")

    axes[1, 2].plot(grouped["year"], grouped["reviews_median"], marker="o")
    axes[1, 2].set_title("Median Reviews per Year")
    axes[1, 2].set_ylabel("Median Reviews")

    # Plot sum values
    axes[2, 0].plot(grouped["year"], grouped["favs_sum"], marker="o")
    axes[2, 0].set_title("Total Favorites per Year")
    axes[2, 0].set_ylabel("Total Favorites")

    axes[2, 1].plot(grouped["year"], grouped["follows_sum"], marker="o")
    axes[2, 1].set_title("Total Follows per Year")
    axes[2, 1].set_ylabel("Total Follows")

    axes[2, 2].plot(grouped["year"], grouped["reviews_sum"], marker="o")
    axes[2, 2].set_title("Total Reviews per Year")
    axes[2, 2].set_ylabel("Total Reviews")

    for ax in axes.flat:
        ax.set_xlabel("Year")

    fig.tight_layout()
    plt.show()
