import pandas as pd

transition_matrix = {"Macro Layer 1": [[0., 0.28571429, 0.71428571],
                                        [0., 0., 1.],
                                        [1., 0., 0.]],
                     "Macro Layer 2": [[0., 0.57142857, 0.42857143],
                                        [0.47619048, 0., 0.52380952],
                                        [0.29411765, 0.70588235, 0.]],
                     "Macro Layer 3": [[0., 0.25, 0.3125, 0.4375],
                                        [0.33333333, 0., 0.66666667, 0.],
                                        [0.41666667, 0.16666667, 0., 0.41666667],
                                        [0.58333333, 0.25, 0.16666667, 0.]],
                     "Macro Layer 4": [[0., 0.57142857,  0.28571429,  0.14285714],
                                        [0.36363636, 0., 0.63636364, 0.],
                                        [0.4, 0.6, 0., 0.],
                                        [0., 1., 0., 0.]],
                     "Macro Layer 5": [[0., 0.28571429, 0.71428571],
                                        [0., 0., 1.],
                                        [1., 0., 0.]],
                     "Macro Layer 6": [[0., 0.57142857, 0.42857143],
                                        [0.47619048, 0., 0.52380952],
                                        [0.29411765, 0.70588235, 0.]],
                     "Macro Layer 7": [[0., 0.25, 0.3125, 0.4375],
                                        [0.33333333, 0., 0.66666667, 0.],
                                        [0.41666667, 0.16666667, 0., 0.41666667],
                                        [0.58333333, 0.25, 0.16666667, 0.]],
                     "Macro Layer 8": [[0., 0.57142857,  0.28571429,  0.14285714],
                                        [0.36363636, 0., 0.63636364, 0.],
                                        [0.4, 0.6, 0., 0.],
                                        [0., 1., 0., 0.]],
                    }

lambda_MacroLayers = {"Macro Layer 1": [0.19546225, 3.4657359, 0.25398282],
            "Macro Layer 2": [0.33500492, 0.7616348, 0.57967196],
            "Macro Layer 3": [0.82642141, 1.32593452, 0.42293198, 1.34284288],
            "Macro Layer 4": [0.77390524, 1.11190655, 0.23288008, 18.42068074],
            "Macro Layer 5": [0.33500492, 0.7616348, 0.57967196],
            "Macro Layer 6": [0.82642141, 1.32593452, 0.42293198, 1.34284288],
            "Macro Layer 7": [0.77390524, 1.11190655, 0.23288008, 18.42068074],
            "Macro Layer 8": [0.77390524, 1.11190655, 0.23288008, 18.42068074],
            }

def lambda_dataframe(array_1d):
    # Convert the 1D array to a data frame
    df = pd.DataFrame(array_1d.reshape(1, -1))

    # Rename the columns if desired
    df.columns = ['Litho {}'.format(i) for i in range(0, df.shape[1])]
    # Rename the index
    df.rename(index={0: 'lambda (1/m)'}, inplace=True)
    # Output the resulting data frame
    return df