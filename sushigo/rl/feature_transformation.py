
FEATURE_MEANS = {

}

FEATURE_STDS = {

}

def transform_observation_space():
    """
    Given some vector of observations k x 1, subtract each entry by its corresponding mean and divide by its SD

    This means we will have to store the mean and SD somewhere
    """