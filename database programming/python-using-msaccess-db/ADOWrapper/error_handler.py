
def print_error(err):
    print ('Error description: %s' % err.Description)
    print ('Error number: %s' % err.Number)
    print ('Error source: %s' % err.Source)
    print ('Error SQLState: %s' % err.SQLState)
    print ('Error native error: %s' % err.NativeError)