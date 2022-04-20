from ClientConnectionManager import ClientConnectionManager

ccm = ClientConnectionManager(2)
ccm.add('foo')
ccm.add('bar')
ccm.start()

ccm.add('moo')
