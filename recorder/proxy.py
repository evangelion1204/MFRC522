def RecordWithOutPassthrough(DecoratedClass):
    class InnerClass(object):
        def __init__(self, *args, **kwargs):
            self.decoratedClass = DecoratedClass(*args,**kwargs)
        def __getattribute__(self, name):
            try:
                attribute = super(InnerClass, self).__getattribute__(name)
            except AttributeError:
                pass
            else:
                return attribute

            attribute = self.decoratedClass.__getattribute__(name)
            if type(attribute) == type(self.__init__):
                def decoratedFunction(*args,**kwargs):
                    return {
                        'method': name,
                        'args': args,
                        'kwargs': kwargs,
                    }

                return decoratedFunction
            else:
                return attribute
    return InnerClass

# class Proxy(object):
#     def __init__(self, subject):
#         self._subject = subject
#
#     def __getattr__(self, attrName):
#         return getattr(self._subject, attrName)
#
#     def __setattr__(self, attrName, value):
#         object.__setattr__(self, attrName, value)
#
#     def __delattr__(self, attrName):
#         delattr(self._subject, attrName)
#
#     def __call__(self,*args,**keys):
#         print(args, keys)
#         object.__getattribute__(self, '_subject')(*args,**keys)
#
#     def __getitem__(self,key):
#         return object.__getattribute__(self, '_subject')[key]