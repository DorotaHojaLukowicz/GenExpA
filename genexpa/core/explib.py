import pandas as pd
import numpy as np
import os

import scikit_posthocs
from scipy import stats

import itertools

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

from genexpa.core.normfinder import normfinder

def clean_name(name):
    # repalce dividing character for safety
    return name.replace("|", "_")

def sort_clean_grups(glist):
    cleaned = [clean_name(gr) for gr in glist]
    return sorted(cleaned)

def join_tuples(df, row=None, col=None):
    cp = df.copy()
    if row is not None:
        cp.index = cp.index.set_levels(cp.index.levels[row].map(" ".join), level=row)

    if col is not None:
        cp.columns = cp.columns.set_levels(cp.columns.levels[col].map(" ".join), level=col)

    return cp

def create_stat_matrix(pval, columns):
    vals = np.full([len(columns), len(columns)], pval)
    np.fill_diagonal(vals, 1.0)

    df = pd.DataFrame(vals, columns=columns, index=columns)
    return df
# ------

def full_excel_export(output_file, df_list):
    mean_df = join_tuples(df_list[0], row=0)
    best_ref_df = join_tuples(df_list[1], row=0)
    RQ_df = join_tuples(df_list[2], row=0)
    stat_df = join_tuples(df_list[3], row=0, col=1)
    comparison_df = join_tuples(df_list[4], row=0, col=1)
    coherence_df = join_tuples(df_list[5], col=1)

    dfs = [mean_df, best_ref_df, RQ_df, stat_df, comparison_df, coherence_df]
    names = ["mean RQ values", "best reference genes", "RQ values", "statistic", "comparison", "partial coherence"]

    writer = pd.ExcelWriter(output_file)
    for name, df in zip(names, dfs):
        df.to_excel(writer, name)
    writer.save()

def read_combined_input(ifile, format='excel', sep=","):
    """
    read combined data file in format:
           Line_1  Line_2  Line_3 ...
    GeneA    x        x      x
    GeneA    x        x      x
    ...
    GeneB    x        x      x
    ...

    and converting it into library internal format:
            Line_1  Line_1 Line_1 ... Line_2 ...
    GeneA     x       x      x          x
    GeneB     x       x      x          x
    ...
    """
    def split_to_cols(df_to_split):
        return [df_to_split[[col]] for col in df_to_split.columns]

    def df_flip_rename(df_to_flip):
        gene, line = df_to_flip.index[0], df_to_flip.columns[0]
        df_fliped = df_to_flip.T

        df_fliped.index = [gene]
        df_fliped.columns = [line for _ in df_fliped.columns]
        return df_fliped

    def transpose_gene(gene_df):
        col_dfs = split_to_cols(gene_df)
        fliped_dfs = [df_flip_rename(col_df) for col_df in col_dfs]
        return pd.concat(fliped_dfs, axis=1)

    def transpose_combined(raw_input):
        genes = raw_input.index.unique()
        return pd.concat([transpose_gene(raw_input.loc[gene]) for gene in genes])

    if format == 'csv':
        input_df = pd.read_csv(ifile, sep=sep, index_col=0)
    elif format == 'excel':
        input_df = pd.read_excel(ifile, index_col=0)
    else:
        ValueError("format: {}, is not supported!".format(format))

    input_df.columns = input_df.columns.astype(str)
    input_df.index = input_df.index.astype(str)

    return transpose_combined(input_df)

def append_group_index(df_ref):
    """
    append unique index for each cell lines (starting from 1)
    """
    group_int_code, _ = pd.factorize(pd.Series(df_ref.columns))
    group_int_code += 1

    group_df = pd.DataFrame(data=[group_int_code], columns=df_ref.columns)
    group_df.index = ["group"]

    return pd.concat([df_ref, group_df])

def flatten_mlvl_index(df, sep='_', arr_sep="|"):
    _df = df.copy()

    if isinstance(df.index, pd.MultiIndex):
        new_rows = []
        for row in df.index.values:
            new_row = []
            for row_value in row:
                if type(row_value) in [list, set, tuple, np.ndarray]:
                    new_row.append(arr_sep.join(row_value))
                else:
                    new_row.append(str(row_value))

            new_rows.append(sep.join(new_row))

        _df.index = pd.Index(new_rows)

    if  isinstance(df.columns, pd.MultiIndex):
        new_rows = []
        for row in df.columns.values:
            new_row = []
            for row_value in row:
                if type(row_value) in [list, set, tuple, np.ndarray]:
                    new_row.append(arr_sep.join(row_value))
                else:
                    new_row.append(str(row_value))

            new_rows.append(sep.join(new_row))

        _df.columns = pd.Index(new_rows)

    return _df

def calc_best_ref(df_ref, df_ref_norm, single_sample_rep, norm_algo, pair_sep=" "):
    """
    calculation of ref Ct values and returning best gene or combination
    """

    if df_ref_norm is None:
        best_genes, best_pairs = normfinder(df_ref)
    else:
        best_genes, best_pairs = normfinder(df_ref_norm.loc[df_ref.index][df_ref.columns.unique()])

    if best_genes[0][1] > best_pairs[0][2]:
        stability_value = best_pairs[0][2]
        best_gene1 = best_pairs[0][0]
        best_gene2 = best_pairs[0][1]
        best_gene = best_gene1 + pair_sep + best_gene2

        best_gene_arr1 = df_ref.loc[best_gene1].values
        best_gene_arr2 = df_ref.loc[best_gene2].values
        best_gene_arr = (best_gene_arr1 + best_gene_arr2)/2.0
    else:
        stability_value = best_genes[0][1]
        best_gene = best_genes[0][0]
        best_gene_arr = df_ref.loc[best_gene].values

    # single sample average over single_sample_rep
    sep_arr = best_gene_arr.reshape(-1, single_sample_rep)
    sep_mean_arr = np.mean(sep_arr, axis=1)
    mean_ref_arr = np.tile(sep_mean_arr.reshape(-1,1), single_sample_rep).reshape(-1)

    df_best_ref = pd.DataFrame(data=[mean_ref_arr], columns=df_ref.columns)
    df_best_ref.index = [best_gene]

    return df_best_ref, stability_value

def remove_worst_ref(df_ref, remove, df_ref_norm, norm_algo):
    if remove == 0:
        return df_ref

    if df_ref_norm is None:
        best_genes, best_pairs = normfinder(df_ref)
    else:
        best_genes, best_pairs = normfinder(df_ref_norm.loc[df_ref.index][df_ref.columns.unique()])

    worst_gene = best_genes[-1][0]

    df_trimed = df_ref[df_ref.index != worst_gene].copy()

    if remove > 1:
        df_trimed = remove_worst_ref(df_trimed, remove-1, df_ref_norm, norm_algo)

    return df_trimed

def calc_RQ(df_target, df_best_ref):
    delta_ct = df_target - df_best_ref.values.squeeze()
    return delta_ct.apply(lambda x: np.power(2,-x))

# ---------------------------------------------------
def stat_analyze(RQ, lines, alpha, mode):
    # p2_cut - The two-tailed p-value.
    # mode ["Kruskal-Wallis H-test", "Kolmogorov-Smirnov t-test", "Welch's t-test"]
    # return dictionary with analyze results, key - gene
    stat_dict = {}
    for gene in RQ.index:
        result_dict = {}
        means = {}
        for line in lines:
            # transpose for better analysis
            result_dict[line] = RQ.loc[gene,line].values
            means[line] = np.mean(RQ.loc[gene,line].values)

        df = pd.DataFrame(result_dict).dropna(1)
        active_lines = len(df.columns)

        pair_stat = [] # all gene comb
        if mode == 0: # Pairwise t-test, Holm adjustment
            if active_lines < 2:
                stat_matrix = pd.DataFrame()
            else:
                stat_matrix = scikit_posthocs.posthoc_ttest(df.melt(), group_col='variable', val_col='value', p_adjust='holm')

        elif mode == 1: # Kolmogorov-Smirnov / Kruskal-Wallis -> post Dunn's test
            if active_lines < 2:
                stat_matrix = pd.DataFrame()
            elif active_lines == 2:
                pval = stats.ks_2samp(*df.values.T).pvalue
                stat_matrix = create_stat_matrix(pval, df.columns)

            else:
                group_pval = stats.kruskal(*df.values.T).pvalue
                if group_pval < alpha:
                    stat_matrix = scikit_posthocs.posthoc_dunn(df.melt(), group_col='variable', val_col='value',
                                                               p_adjust="bonferroni")
                else:
                    stat_matrix = create_stat_matrix(group_pval, df.columns)

        elif mode == 2: # Mann-Whitney / Kruskal-Wallis -> post Dunn's test
            if active_lines < 2:
                stat_matrix = pd.DataFrame()
            elif active_lines == 2:
                pval = stats.mannwhitneyu(*df.values.T).pvalue
                stat_matrix = create_stat_matrix(pval, df.columns)

            else:
                group_pval = stats.kruskal(*df.values.T).pvalue
                if group_pval < alpha:
                    stat_matrix = scikit_posthocs.posthoc_dunn(df.melt(), group_col='variable', val_col='value',
                                                               p_adjust="bonferroni")
                else:
                    stat_matrix = create_stat_matrix(group_pval, df.columns)

        elif mode == 3: # Kruskal-Wallis
            if active_lines < 2:
                stat_matrix = pd.DataFrame()
            else:
                group_pval = stats.kruskal(*df.values.T).pvalue
                if group_pval < alpha:
                    stat_matrix = create_stat_matrix(1.0, df.columns)
                    for line_a, line_b in itertools.combinations(df.columns, 2):
                        pval = stats.kruskal(*df[[line_a, line_b]].values.T).pvalue
                        stat_matrix.loc[line_a, line_b] = pval
                        stat_matrix.loc[line_b, line_a] = pval
                else:
                    stat_matrix = create_stat_matrix(group_pval, df.columns)

        for line_a, line_b in itertools.combinations(lines, 2):
            if line_a in stat_matrix.index and line_b in stat_matrix.index:
                p_val = stat_matrix.loc[line_a][line_b]
            else:
                p_val = np.nan

            pair_stat.append([line_a, line_b, means[line_a], means[line_b], p_val])

        stat_dict[gene] = pair_stat

    return stat_dict

def calc_coherence(comparison_df):
    coherence_line = []
    for gene, pair in comparison_df.columns:
        value_list = comparison_df.loc[:, gene][pair].dropna()
        value_set = set(value_list)

        if 1 in value_set and -1 in value_set:
            coherence_line.append(0)

        else:
            coherence_line.append(1)

    coherence_df = pd.DataFrame(
        data=[coherence_line],
        index=["coherence"],
        columns=comparison_df.columns
    )

    return coherence_df

def full_analyze(df_ref, df_target, models, remove_num, single_sample_rep, stat_mode, alpha, df_ref_norm, norm_algo, sort_lines=True):
    target_genes = df_target.index.tolist()

    mean_df_list = []
    RQ_df_list = []
    stat_df_list = []
    comparison_df_list = []

    best_ref_df_list = []
    best_ref_col_index = ["best", "value"]

    if df_ref_norm is not None:
        df_ref_norm = pd.concat([df_ref_norm, df_ref.loc[["group"]]])

    for model in models:
        df_sel_ref = df_ref.loc[:,model]
        df_sel_target = df_target.loc[:,model]

        best_ref_rm_list = []
        mean_rm_list = []
        RQ_rm_list = []
        stat_rm_list = []
        comparison_rm_list = []

        for rm_num in range(remove_num+1):
            local_df_sel_ref = remove_worst_ref(df_sel_ref, rm_num, df_ref_norm, norm_algo) # explib
            df_best_ref, stability_value = calc_best_ref(local_df_sel_ref, df_ref_norm, single_sample_rep, norm_algo) # explib

            best_ref_gene = df_best_ref.index[0]
            best_ref_rm_list.append([best_ref_gene, stability_value])

            RQ = calc_RQ(df_sel_target, df_best_ref) # explib
            gene_stat_dict = stat_analyze(RQ, model, alpha, stat_mode) # explib


            mean_local = []
            RQ_local = []
            stat_local = []
            comparison_local = []
            for target_gene in target_genes:
                mean_helper_dict = {}
                for gr1, gr2, m1, m2, pval in gene_stat_dict[target_gene]:
                    mean_helper_dict[gr1] = m1
                    mean_helper_dict[gr2] = m2

                    stat_local.append(pval)
                    if np.isnan(m1) or np.isnan(m2):
                        comparison_local.append(np.nan)
                        continue

                    if pval < alpha:
                        if m1 > m2:
                            comparison_local.append(1)
                        else:
                            comparison_local.append(-1)

                    else:
                        comparison_local.append(0)

                mean_local.extend([mean_helper_dict[key] for key in model])

                for key in model:
                    RQ_local.append(RQ.loc[target_gene][key].values.reshape(-1,1))

            mean_rm_list.append(mean_local)
            RQ_rm_list.append(np.concatenate(RQ_local, axis=1))
            stat_rm_list.append(stat_local)
            comparison_rm_list.append(comparison_local)

        # BEST REF DF
        model_str = "|".join(model)
        row_mlvl_index = pd.MultiIndex.from_product(
            [[model],list(range(remove_num+1))], names=["model", 'removal'])

        _df_best = pd.DataFrame(
            data=best_ref_rm_list,
            index=row_mlvl_index,
            columns=best_ref_col_index)
        best_ref_df_list.append(_df_best)

        # MEAN DF
        mean_col_mlvl_index =  pd.MultiIndex.from_product(
            [target_genes, model], names=['target', 'group'])
        _mean_df = pd.DataFrame(
            data=mean_rm_list,
            index=row_mlvl_index,
            columns=mean_col_mlvl_index)
        mean_df_list.append(_mean_df)

        # RQ DF
        RQ_data = np.concatenate(RQ_rm_list)
        RQ_row_mlvl_index = pd.MultiIndex.from_product(
            [[model],
             list(range(remove_num+1)),
             range(RQ_data.shape[0]//(remove_num+1))], names=["model", 'removal', 'measurment'])

        _RQ_df = pd.DataFrame(
            data=RQ_data,
            index=RQ_row_mlvl_index,
            columns=mean_col_mlvl_index)
        RQ_df_list.append(_RQ_df)

        # stat DF
        model_pair = list(itertools.combinations(model, 2))
        stat_col_mlvl_index = pd.MultiIndex.from_product(
            [target_genes, model_pair],
            names=['target', 'pair'])
        _stat_df = pd.DataFrame(
            data=stat_rm_list,
            index=row_mlvl_index,
            columns=stat_col_mlvl_index)
        stat_df_list.append(_stat_df)

        # comparison DF
        _comparison_df = pd.DataFrame(
            data=comparison_rm_list,
            index=row_mlvl_index,
            columns=stat_col_mlvl_index)
        comparison_df_list.append(_comparison_df)

    best_ref_df = pd.concat(best_ref_df_list)
    mean_df = pd.concat(mean_df_list)
    RQ_df = pd.concat(RQ_df_list)

    stat_df = pd.concat(stat_df_list)
    stat_df.stat_model = stat_mode
    stat_df.alpha = alpha

    comparison_df = pd.concat(comparison_df_list)

    if sort_lines:
        # prepare new column order for dataframes
        models_lengths = [len(_m) for _m in models]
        final_model = list(models[np.argsort(models_lengths)[-1]])

        unique_lines = list(set([item for sublist in models for item in sublist]))

        for _line in unique_lines:
            if _line not in final_model:
                final_model.append(_line)

        _dfs = []
        _keys = []

        for _gene in mean_df.columns.levels[0]:
            _dfs.append(mean_df[_gene][final_model])
            _keys.append(_gene)
        mean_df = pd.concat(_dfs, axis=1, keys=_keys)

        _dfs = []
        _keys = []

        for _gene in RQ_df.columns.levels[0]:
            _dfs.append(RQ_df[_gene][final_model])
            _keys.append(_gene)
        RQ_df = pd.concat(_dfs, axis=1, keys=_keys)

    return mean_df, best_ref_df, RQ_df, stat_df, comparison_df

def get_best_series_remove(best_ref_df):
    mask = []
    for model in best_ref_df.index.get_level_values(0).unique():
        model_df = best_ref_df.loc[model]

        _mask = np.zeros(model_df.shape[0], bool)

        _mask[model_df.value.values.argmin()] = True
        mask.extend(_mask)

    return np.array(mask)

def expand_mask(mask, df):
    full_mask = []
    i = 0
    for model in df.index.get_level_values(0).unique():
        for rm_lvl in df.loc[model].index.get_level_values(0).unique():
            samples = df.loc[model].loc[rm_lvl].shape[0]
            full_mask.extend([mask[i]]*samples)
            i+=1
            
    return np.array(full_mask)

def write_excel(df, opath):
    # Create a Pandas Excel writer using XlsxWriter as the engine. '/tmp/pandas_simple.xlsx'
    writer = pd.ExcelWriter(opath, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def print_combination(res, alpha, single=None, retstr=False):
    ostr = ""
    for gene in res:
        if single:
            if gene != single:
                continue
        ostr += "----------------------\n{}\n----------------------".format(gene)
        ostr += ("\n{:<20}{:<3}{:<3}{:<3}".format("Pair", "g1", "g2", "ins"))

        for pair in res[gene]:
            gr1_larger = 0
            gr2_larger = 0
            insig = 0
            for case in res[gene][pair]:
                if case[2] > alpha:
                    insig += 1
                elif case[0] > case[1]:
                    gr1_larger += 1
                else:
                    gr2_larger += 1
            pair_str = "{:<10}{:<10}".format(pair[0], pair[1])
            ostr += "\n{:<20}{:<3}{:<3}{:<3}".format(pair_str, gr1_larger, gr2_larger, insig)

        ostr += "\n"
    if retstr:
        return ostr

def plot_gene_analyze(pair_stat, df, ax=None, gene_name=""):
    if ax is not None:
        bplot = df.boxplot(column=list(df.columns), ax=ax)
    else:
        fig, ax = plt.subplots(1,1, figsize=(16,16))
        bplot = df.boxplot(column=list(df.columns), ax=ax)

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    pair_stat = sorted(pair_stat, key=lambda x: x[2])
    box_text = "  The two-tailed p-value:\n"
    box_text += "\n".join( "{a[0]: <10}{a[1]: <10} = {a[2]:.2e}".format(a=x) for x in pair_stat)

    # add place on y for text
    y_min, y_max = ax.get_ylim()
    y_max = y_max+(y_max-y_min)*0.4
    ax.set_ylim([y_min, y_max])

    #font.set_family("monospace")
    font = FontProperties()
    font.set_family("monospace")
    ax.set_title(gene_name)
    ax.text(0.02, 0.98, box_text, transform=ax.transAxes, bbox=props, verticalalignment='top',
           fontproperties=font)

def box_plot(RQ, df_stat, model, title="", savefig=None, alpha=0.05, line_color='#ff1b00ff', axsize=(6,6), figsize=None, columns=2, line_width_frac=0.01, interline=2):
    RQ = RQ.dropna(1)
    df_stat = df_stat.dropna(0)

    genes = RQ.columns.get_level_values(0).unique().tolist()
    genes_cnt = len(genes)

    rows = int(np.ceil(genes_cnt/float(columns)))
    if figsize is None:
        figsize=(axsize[0]*columns, axsize[1]*rows)


    fig, axes = plt.subplots(rows, columns, figsize=figsize)
    fig.suptitle(title)

    i = 0
    for gene in genes:
        if rows == 1:
            ax = axes[i]
        else:
            ax = axes[i//columns][i%columns]

        ax.set_title(gene)

        valid_model = []
        for _line in model:
            if _line in RQ[gene].columns:
                valid_model.append(_line)

        if gene not in df_stat:
            continue

        RQ_sel = RQ[gene]
        if len(RQ_sel.columns) < 2:
            continue
        RQ_sel.boxplot(column=valid_model, ax=ax)
        x_group = dict(zip(valid_model, range(1,len(valid_model)+1)))

        ymin, ymax = ax.get_ylim()
        ax_height = ymax-ymin

        y_current = ymin

        line_width = line_width_frac*ax_height
        
        # draw connections

        for pair, value in df_stat[gene].iteritems():
            if type(alpha) is str:
                continue

            if value > alpha:
                continue

            left_group, right_group = pair
            if right_group not in x_group or left_group not in x_group:
                continue

            x_start = x_group[left_group]
            x_len = x_group[right_group]-x_group[left_group]

            ax.add_patch(
                patches.Rectangle((x_start, y_current), x_len, line_width, facecolor=line_color, zorder=-100)
            )
            y_current -= interline*line_width

        ax.set_ylim(y_current, ymax)

        i += 1

    axes_flat = axes.flatten()
    for rm_ax in axes_flat[i:]:
        fig.delaxes(rm_ax)

    if savefig:
        fig.savefig(savefig)
        fig.clear()
        plt.close()

def create_boxplots(RQ, df_stat, base):
    try:
        os.mkdir(base)
    except:
        pass

    if hasattr(df_stat, "alpha"):
        alpha = df_stat.alpha
    else:
        alpha = "None"

    if hasattr(df_stat, "stat_model"):
        stat_model = df_stat.stat_model
    else:
        stat_model = "None"

    models = RQ.index.get_level_values(0).unique().tolist()

    for model in models:
        rmlvls = RQ.loc[model].index.get_level_values(0).unique().values
        for rmlvl in rmlvls:
            name = " ".join(model)
            title = "{}\nmodel={},\nalpha={}, removed={}".format(name, stat_model, alpha, rmlvl)
            _RQ = RQ.loc[model].loc[rmlvl]
            _df_stat = df_stat.loc[model].loc[rmlvl]

            save_dir = os.path.join(base, "model_{}__removed_{}.png".format(name, rmlvl))
            box_plot(_RQ, _df_stat, model = model, title=title, savefig=save_dir, alpha=alpha)
