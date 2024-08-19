if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    # Define your query
    query = {
        "query": {
            "match": {
                "text": "When is the next cohort?"  # Replace 'text' with the field you are querying against
            }
        },
        "size": 1  # Limit to top result
    }

    return query


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'