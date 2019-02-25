from inspect import getargspec, getcallargs

def type_definition(*types):
    def type_checker(func):
        argspec = getargspec(func)

        arg_length = len(argspec.args)

        kwargs_index = -1 if argspec.keywords else 0
        vargs_index = -1 + kwargs_index if argspec.varargs else 0

        arg_type = zip(argspec.args, types[:arg_length])
        vargs_type = types[vargs_index] if vargs_index else None
        kwargs_type = types[kwargs_index] if kwargs_index else None

        def new_func(*args, **kwargs):
            argdetail = getcallargs(func, *args, **kwargs)

            # check type of args
            for name, _type in arg_type:
                if name in argdetail:
                    if not type(argdetail[name]) == _type:
                        raise ValueError(
                           "Invalid Type: " + name + " is not " + str(_type)
                            )

            if vargs_type:
                for value in argdetail[argspec.varargs]:
                    if not type(value) == vargs_type:
                        raise ValueError(
                           "Invalid Type: " + argspec.varargs \
                             + " is not " + str(vargs_type)
                           )

            if kwargs_type:
                for value in argdetail[argspec.keywords].values():
                    if not type(value) == kwargs_type:
                        raise ValueError(
                           "Invalid Type: " + argspec.keywords \
                             + " is not " + str(kwargs_type)
                           )

            # do func
            return func(*args, **kwargs)

        return new_func
    return type_checker
