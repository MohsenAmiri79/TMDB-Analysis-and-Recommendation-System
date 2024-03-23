import numpy as np
import seaborn as sns
import matplotlib.colors as mcolors


# Colormaps
def SET_PALETTE():
    sns.set_palette(sns.cubehelix_palette(start=-1.3, rot=-.0))


def DIS_CMAP(bins=30, r=False):
    if r:
        return list(reversed([CON_CMAP(i) for i in np.linspace(0, 1, bins)]))
    return [CON_CMAP(i) for i in np.linspace(0, 1, bins)]


CON_CMAP = sns.cubehelix_palette(start=-1.3, rot=-.0, as_cmap=True)
DIV_CMAP = mcolors.LinearSegmentedColormap.from_list(
    "mirrored_cmap",
    colors=np.concatenate((CON_CMAP(np.linspace(0, 1, 128)),
                           CON_CMAP(np.linspace(1, 0, 128)))))


# Column Lists
NON_STR_COLS = [
    'budget', 'popularity', 'runtime', 'vote_average',
    'vote_count', 'Action', 'Adventure', 'Animation', 'Comedy',
    'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Foreign',
    'History', 'Horror', 'Music', 'Mystery', 'Romance',
    'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western',
    'language_code', 'status_code', 'year', 'month', 'day',
    'actor_1_code', 'actor_2_code', 'actor_3_code', 'actor_4_code',
    'actor_5_code', 'production_company_code',
]
CREW_COLS = [
    'actor_1_code', 'actor_2_code', 'actor_3_code',
    'actor_4_code', 'actor_5_code', 'production_company_code',
]
GENRE_COLS = [
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
    'Documentary', 'Drama', 'Family', 'Fantasy', 'Foreign',
    'History', 'Horror', 'Music', 'Mystery', 'Romance',
    'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western'
]
NON_GENRECREW_COLS = list(set(NON_STR_COLS) - set(GENRE_COLS) - set(CREW_COLS))
NON_GENRE_COLS = list(set(NON_STR_COLS) - set(GENRE_COLS))
NUMERICAL_COLS = list(set(NON_GENRECREW_COLS)
                      - set(['language_code', 'status_code']))
LABEL_ENC_COLS = CREW_COLS + ['language_code', 'status_code']
