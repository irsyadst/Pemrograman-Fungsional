def false_position(f, a, b, tol=1e-9, maxiter=100):

    """
    f : Function for which we are trying to find a root.
    a, b : Interval in which the root is sought.
    tol : Tolerance for the root. The default value is 1e-9.
    maxiter : Maximum number of iterations to perform.
    """

    #Regular Falsi Method [By Bottom Science]

    for i in range(maxiter):
        # Compute the value of the function at the midpoint of the interval
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)

        if fc == 0 or (b - a) / 2 < tol:
            # If the function at the midpoint is zero or the interval is small enough,
            # then we have found the root
            return c

        # Compute the function at the endpoints of the interval
        fa = f(a)
        fb = f(b)

        if (fa > 0 and fc > 0) or (fa < 0 and fc < 0):
            # If the signs of the function at the endpoints and at the midpoint are the same,
            # then we can narrow down the interval to [c, b]
            a = c
        else:
            # Otherwise, we can narrow down the interval to [a, c]
            b = c

    # If we reach this point, then the maximum number of iterations has been exceeded
    raise Exception("Maximum number of iterations exceeded")

root = false_position(lambda x: (2*x**2-20)/2, 3, 4)

print(root)