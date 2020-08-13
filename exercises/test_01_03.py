def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "pd.read_csv" in __solution__, "Are you using pandas to read in your data"
    assert data.shape == len(DATA), "Are you getting the correct length?"

    __msg__.good("Well done!")
