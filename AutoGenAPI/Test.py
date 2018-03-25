class GenSDKFiles:
    def __init__(self, sdk_name, func_list):
        self.sdk_file_obj = open(sdk_name+'.c', 'w+')


class FuncParse:
    def __init__(self, foo):
        self.foo = foo 
        self.name = ''
        self.ret_type = 'void'
        self.argv = ''
        self.is_ptr = False

if  '__main__'  == __name__:
    print('------------->\nBegin:')